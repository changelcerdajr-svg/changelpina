"""Fase 3: escaner en vivo + simulador de PAPEL. No hay cuentas, llaves ni ordenes reales.

Cada corrida (pensada para ejecutarse cada hora):
  1. Liquida posiciones cuyos mercados ya cerraron.
  2. Revisa las ordenes limite virtuales abiertas: se llenan solo si (a) el precio del mercado
     bajo al menos 1 tick por debajo de nuestro limite despues de ponerla (alguien vendio ahi) y
     (b) la orden gano el sorteo del 30% (supuesto del plan: solo 30% de las ordenes se llenan).
  3. Escanea mercados activos y coloca ordenes limite virtuales (maker) segun las reglas que
     pasaron el backtest sin sesgo (ver README), con los limites de riesgo del plan.
  4. Guarda el estado en data/paper/ y regenera data/paper/REPORT.md.

Solo lee APIs publicas de Polymarket (Gamma y CLOB).
"""
import json, os, sys, re, math, hashlib, csv, datetime as dt
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from fetch_backtest import get, category, G, C

PROFILE = os.environ.get("PROFILE", "base")   # "base" (el del plan) o "agresivo" (experimento de comparacion)

CAPITAL0 = 1000.0          # capital virtual
MAX_MARKET = 0.05          # 5% del capital por mercado
MAX_EVENT = 0.10           # 10% por evento (mercados del mismo partido/dia estan correlacionados)
MAX_CAT = 0.20             # 20% por categoria
STOP_LOSS = 0.15           # parar si la perdida acumulada llega a 15%
FILL_PROB = 0.30           # solo 30% de las ordenes limite se llenan
MIN_LIQ = 1000             # liquidez minima del mercado
MAX_DAYS = 45              # solo mercados que cierran en <= 45 dias
MAX_SPREAD = 0.03
ORDER_TTL_H = 12           # una orden virtual vive como maximo 12h
STUCK_DAYS = 7             # posicion "inmovilizada": mercado abierto > 7 dias despues de su fecha de fin
PAPER_WEEKS = 4
SCAN_AHEAD_H = 30          # hasta cuantas horas antes del fin se buscan mercados
BID_AT_ASK = False         # False: orden al punto medio. True: 1 tick por debajo del ask (primero en la fila)
DIR = "data/paper"

# Reglas: (nombre, categorias, horas hasta la fecha de fin [min, max], banda de precio [min, max))
# Vienen de data/universe_rules.csv: pasan en entrena y prueba, con seleccion adversa y en el peor caso.
RULES = [
    ("cripto_cierre", {"cripto"}, (0.0, 24.0), (0.97, 0.9995)),
    ("deportes_previo", {"deportes"}, (6.0, 30.0), (0.97, 0.9995)),
    ("otros_cierre", {"otros"}, (0.0, 24.0), (0.97, 0.9995)),
    ("post_fin_95_97", {"clima", "deportes", "otros", "cripto"}, (-12.0, -3.0), (0.95, 0.97)),
]

if PROFILE == "agresivo":
    # Mismo capital, el doble de tamano por jugada y por categoria, bandas mas anchas (desde 95c y,
    # con la fecha de fin ya pasada, desde 90c), ventanas mas largas (hasta 72h antes del fin), entra
    # tambien a clima, acepta mercados menos liquidos y puja mas alto para que le llenen mas seguido.
    # Varias de estas reglas NO pasaron todas las pruebas del backtest: es un experimento, no una mejora.
    MAX_MARKET, MAX_EVENT, MAX_CAT, STOP_LOSS = 0.10, 0.20, 0.40, 0.30
    FILL_PROB, MIN_LIQ, MAX_SPREAD, ORDER_TTL_H = 0.50, 500, 0.05, 24
    SCAN_AHEAD_H, BID_AT_ASK = 72, True
    DIR = "data/paper_agresivo"
    RULES = [
        ("cripto_cierre", {"cripto"}, (0.0, 72.0), (0.95, 0.9995)),
        ("deportes_previo", {"deportes"}, (1.0, 72.0), (0.95, 0.9995)),
        ("otros_cierre", {"otros"}, (0.0, 72.0), (0.95, 0.9995)),
        ("clima_cierre", {"clima"}, (6.0, 48.0), (0.95, 0.9995)),
        ("post_fin_90_97", {"clima", "deportes", "otros", "cripto"}, (-24.0, -3.0), (0.90, 0.97)),
    ]

STATE = f"{DIR}/state.json"
LOG = f"{DIR}/log.jsonl"
REPORT = f"{DIR}/REPORT.md"
SHADOW_CSV = f"{DIR}/shadow_closed.csv"   # todas las oportunidades ya resueltas (sin limite de capital)
SHADOW_HDR = ["id", "rule", "cat", "px", "touched", "result", "ts", "end_ts", "closed_ts", "q"]


def cat2(cat, q):
    ql = q.lower()
    if re.search(r"temperature|°c|°f|\brain\b|\bsnow\b|precipitation|hurricane", ql):
        return "clima"
    if re.search(r"tweets?|posts? \d|truth social", ql):
        return "tuits"
    if ql.startswith("exact score"):
        return "marcador_exacto"
    return cat


def now_utc():
    return dt.datetime.now(dt.timezone.utc)


def iso(t):
    return t.strftime('%Y-%m-%dT%H:%M:%SZ')


def parse_ts(s):
    if not s:
        return None
    try:
        s = s.replace(' ', 'T').replace('Z', '+00:00')
        if s.endswith('+00'):
            s += ':00'
        return dt.datetime.fromisoformat(s).timestamp()
    except Exception:
        return None


def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE, encoding="utf-8"))
    return dict(capital0=CAPITAL0, cash=CAPITAL0, started=iso(now_utc()), orders=[], positions=[], closed=[],
                runs=[], halted=False, stats=dict(placed=0, filled=0, expired=0, touched_not_filled=0))


def log(ev, **kw):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(dict(ts=iso(now_utc()), ev=ev, **kw), ensure_ascii=False) + "\n")


def quote(m):
    """Devuelve (lado, bid, ask, mid) del resultado favorito, a partir del libro del token 0."""
    bb, ba = m.get("bestBid"), m.get("bestAsk")
    if bb is None or ba is None or ba <= 0 or bb <= 0 or ba < bb:
        return None
    if (bb + ba) / 2 >= 0.5:
        side, bid, ask = 0, bb, ba
    else:
        side, bid, ask = 1, 1 - ba, 1 - bb
    return side, bid, ask, (bid + ask) / 2


def disputed(m):
    return "disput" in (m.get("umaResolutionStatuses") or "").lower() or "disput" in (m.get("umaResolutionStatus") or "").lower()


def match_rule(m, now):
    q = m.get("question") or ""
    et = parse_ts(m.get("endDate"))
    qt = quote(m)
    if not et or not qt:
        return None
    if m.get("closed") or m.get("acceptingOrders") is False or disputed(m):
        return None
    if (m.get("liquidityNum") or 0) < MIN_LIQ:
        return None
    try:
        if len(json.loads(m["outcomes"])) != 2 or len(json.loads(m["clobTokenIds"])) != 2:
            return None
    except Exception:
        return None
    h = (et - now) / 3600
    if h > MAX_DAYS * 24:
        return None
    side, bid, ask, mid = qt
    if ask - bid > MAX_SPREAD:
        return None
    cat = cat2(category(m), q)
    for name, cats, (h0, h1), (p0, p1) in RULES:
        if cat in cats and h0 < h <= h1 and p0 <= mid < p1:
            tick = float(m.get("orderPriceMinTickSize") or 0.001)
            px = math.floor((ask - tick if BID_AT_ASK else mid) / tick + 1e-9) * tick
            if px >= ask:
                px = ask - tick
            px = round(max(px, bid), 4)
            if not (p0 <= px < p1):
                return None
            return dict(rule=name, cat=cat, side=side, bid=round(bid, 4), ask=round(ask, 4), mid=round(mid, 4), px=px, tick=tick, hours=round(h, 2))
    return None


def scan(now):
    out = {}
    t0 = dt.datetime.fromtimestamp(now, dt.timezone.utc) - dt.timedelta(hours=12)
    for k in range(0, 12 + SCAN_AHEAD_H, 3):
        a, b = t0 + dt.timedelta(hours=k), t0 + dt.timedelta(hours=k + 3)
        for off in range(0, 2100, 100):
            ms = get(f"{G}/markets?limit=100&offset={off}&closed=false&end_date_min={iso(a)}&end_date_max={iso(b)}&liquidity_num_min={MIN_LIQ}")
            if not ms:
                break
            for m in ms:
                out[m["id"]] = m
            if len(ms) < 100:
                break
    return list(out.values())


def lucky(oid):
    return int(hashlib.sha256(oid.encode()).hexdigest(), 16) % 100 < FILL_PROB * 100


def exposure(st):
    cat, ev = {}, {}
    for o in st["orders"] + st["positions"]:
        cat[o["cat"]] = cat.get(o["cat"], 0) + o["cost"]
        ev[o["event"]] = ev.get(o["event"], 0) + o["cost"]
    return cat, ev


def equity(st):
    return st["cash"] + sum(o["cost"] for o in st["orders"]) + sum(p["shares"] * p.get("mark", p["px"]) for p in st["positions"])


def settle(st, now):
    keep = []
    for p in st["positions"]:
        m = get(f"{G}/markets/{p['id']}")
        if not m:
            keep.append(p); continue
        try:
            pr = [float(x) for x in json.loads(m["outcomePrices"])]
        except Exception:
            pr = None
        if m.get("closed") and pr and len(pr) == 2:
            pay = p["shares"] * pr[p["side"]]
            st["cash"] += pay
            c = dict(p, payout=round(pay, 4), pnl=round(pay - p["cost"], 4), result=pr[p["side"]], closed_ts=iso(now_utc()),
                     days=round((now - p["fill_ts"]) / 86400, 2))
            st["closed"].append(c)
            log("settle", id=p["id"], q=p["q"], rule=p["rule"], px=p["px"], result=pr[p["side"]], pnl=c["pnl"], days=c["days"])
        else:
            qt = quote(m)
            if qt:
                side, bid, ask, mid = qt
                p["mark"] = round(mid if side == p["side"] else 1 - mid, 4)
            p["stuck"] = bool(now > p["end_ts"] + STUCK_DAYS * 86400)
            p["disputed"] = disputed(m)
            keep.append(p)
    st["positions"] = keep


def check_orders(st, now):
    keep = []
    for o in st["orders"]:
        h = get(f"{C}/prices-history?market={o['token']}&startTs={int(o['ts'])}&endTs={int(now)}&fidelity=1")
        pts = [x["p"] for x in ((h or {}).get("history") or []) if x["t"] > o["ts"]]
        touched = any(p <= o["px"] - o["tick"] + 1e-9 for p in pts)
        if touched and lucky(o["oid"]):
            st["positions"].append(dict(o, fill_ts=now, mark=o["px"]))
            st["stats"]["filled"] += 1
            log("fill", id=o["id"], q=o["q"], rule=o["rule"], px=o["px"], cost=o["cost"])
            continue
        if touched:
            st["cash"] += o["cost"]; st["stats"]["touched_not_filled"] += 1
            log("touched_not_filled", id=o["id"], rule=o["rule"], px=o["px"])
            continue
        if now - o["ts"] > ORDER_TTL_H * 3600 or now > o["end_ts"] + 12 * 3600:
            st["cash"] += o["cost"]; st["stats"]["expired"] += 1
            log("expire", id=o["id"], rule=o["rule"], px=o["px"])
            continue
        keep.append(o)
    st["orders"] = keep


def place(st, now, markets):
    eq = equity(st)
    held = {o["id"] for o in st["orders"] + st["positions"]}
    recent = {c["id"] for c in st["closed"]}
    cands = []
    for m in markets:
        if m["id"] in held or m["id"] in recent:
            continue
        r = match_rule(m, now)
        if r:
            cands.append((m, r))
    cands.sort(key=lambda x: (abs(x[1]["hours"]), x[0]["id"]))
    n = 0
    for m, r in cands:
        cat, ev = exposure(st)
        event = str(((m.get("events") or [{}])[0]).get("id") or m["id"])
        budget = min(MAX_MARKET * eq, MAX_CAT * eq - cat.get(r["cat"], 0), MAX_EVENT * eq - ev.get(event, 0), st["cash"])
        if budget < 5:
            continue
        tokens = json.loads(m["clobTokenIds"])
        oid = f"{m['id']}-{int(now)}"
        o = dict(oid=oid, id=m["id"], q=m["question"], cat=r["cat"], rule=r["rule"], event=event, side=r["side"],
                 token=tokens[r["side"]], px=r["px"], tick=r["tick"], mid=r["mid"], bid=r["bid"], ask=r["ask"],
                 shares=round(budget / r["px"], 4), cost=round(budget, 4), ts=now, end_ts=parse_ts(m["endDate"]), hours=r["hours"],
                 liq=round(m.get("liquidityNum") or 0))
        st["cash"] -= o["cost"]
        st["orders"].append(o)
        st["stats"]["placed"] += 1
        n += 1
        log("order", id=o["id"], q=o["q"], rule=o["rule"], cat=o["cat"], px=o["px"], bid=o["bid"], ask=o["ask"], cost=o["cost"], hours=o["hours"])
    return len(cands), n


def shadow_rows():
    if not os.path.exists(SHADOW_CSV):
        return []
    with open(SHADOW_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def shadow_add(st, now, markets):
    """Registro sombra: cada oportunidad que detecta el escaner, una vez por mercado, sin limite de
    capital. Sirve para medir el edge con muestra grande; no mueve el capital virtual."""
    seen = {r["id"] for r in shadow_rows()} | {x["id"] for x in st["shadow"]}
    n = 0
    for m in markets:
        if m["id"] in seen:
            continue
        r = match_rule(m, now)
        if not r:
            continue
        st["shadow"].append(dict(id=m["id"], rule=r["rule"], cat=r["cat"], side=r["side"], token=json.loads(m["clobTokenIds"])[r["side"]],
                                 px=r["px"], tick=r["tick"], ts=int(now), end_ts=int(parse_ts(m["endDate"])), q=m["question"][:90], touched=None))
        n += 1
    return n


def shadow_update(st, now):
    # a) cuando la orden habria expirado, ver si el precio llego a tocarla
    due = [x for x in st["shadow"] if x["touched"] is None and now - x["ts"] >= ORDER_TTL_H * 3600]

    def touch(x):
        h = get(f"{C}/prices-history?market={x['token']}&startTs={x['ts']}&endTs={x['ts'] + ORDER_TTL_H * 3600}&fidelity=1", tries=2)
        if h is None:
            return x, None
        pts = [p["p"] for p in (h.get("history") or []) if p["t"] > x["ts"]]
        return x, int(any(p <= x["px"] - x["tick"] + 1e-9 for p in pts))

    with ThreadPoolExecutor(8) as ex:
        for x, t in ex.map(touch, due):
            x["touched"] = t
    # b) liquidar las que ya cerraron
    ready = [x for x in st["shadow"] if x["touched"] is not None and now > x["end_ts"] - 3600]
    closed = {}
    for i in range(0, len(ready), 50):
        ms = get(f"{G}/markets?limit=100&closed=true&" + "&".join(f"id={x['id']}" for x in ready[i:i + 50]), tries=2) or []
        for m in ms:
            try:
                pr = [float(v) for v in json.loads(m["outcomePrices"])]
                if len(pr) == 2:
                    closed[m["id"]] = (pr, parse_ts(m.get("closedTime")) or now)
            except Exception:
                pass
    if closed:
        new = not os.path.exists(SHADOW_CSV)
        with open(SHADOW_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(SHADOW_HDR)
            for x in st["shadow"]:
                if x["id"] in closed:
                    pr, ct = closed[x["id"]]
                    w.writerow([x["id"], x["rule"], x["cat"], x["px"], x["touched"], pr[x["side"]], x["ts"], x["end_ts"], int(ct), x["q"]])
        st["shadow"] = [x for x in st["shadow"] if x["id"] not in closed]
    return len(closed)


def shadow_report(st, L, now):
    rows = shadow_rows()
    L.append("\n## Registro sombra: todas las oportunidades detectadas, sin limite de capital\n")
    L.append("Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "
             "\"Tocadas\" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).\n")
    stuck = [x for x in st["shadow"] if now > x["end_ts"] + STUCK_DAYS * 86400]
    L.append(f"- Resueltas: {len(rows)} | abiertas: {len(st['shadow'])} | abiertas mas de {STUCK_DAYS} dias despues de su fecha de fin: {len(stuck)}")
    if not rows:
        return
    L.append("\n| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |")
    L.append("|---|---|---|---|---|---|---|---|")
    for g in sorted({r["rule"] for r in rows}) + ["TOTAL"]:
        for label, f in (("todas", lambda r: True), ("tocadas", lambda r: r["touched"] == "1")):
            ss = [r for r in rows if (g == "TOTAL" or r["rule"] == g) and f(r)]
            n = len(ss)
            if not n:
                continue
            e = [float(r["result"]) - float(r["px"]) for r in ss]
            mean = sum(e) / n
            sd = math.sqrt(sum((v - mean) ** 2 for v in e) / (n - 1)) if n > 1 else 0
            se = sd / math.sqrt(n)
            px = sum(float(r["px"]) for r in ss) / n
            L.append(f"| {g} | {label} | {n} | {px*100:.2f}c | {(px+mean)*100:.2f}% | {mean*100:+.2f} pts | {(mean-1.96*se)*100:+.2f} a {(mean+1.96*se)*100:+.2f} | {sum(float(r['result']) < 1 for r in ss)} |")
    bad = sorted([r for r in rows if float(r["result"]) < 1], key=lambda r: float(r["result"]) - float(r["px"]))[:10]
    if bad:
        L.append("\nPeores casos del registro sombra:\n")
        for r in bad:
            L.append(f"- {float(r['px'])*100:.1f}c -> pago {r['result']} | {r['rule']} | {'tocada' if r['touched']=='1' else 'no tocada'} | {r['q']}")


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    ph = k / n; d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def report(st):
    eq = equity(st); cap = st["capital0"]
    cl = st["closed"]; n = len(cl)
    started = dt.datetime.fromisoformat(st["started"].replace("Z", "+00:00"))
    days = (now_utc() - started).total_seconds() / 86400
    L = []
    L.append(f"# Sweeper de Polymarket: reporte del simulador de papel (perfil {PROFILE})\n")
    L.append("Dinero virtual. Ninguna orden real. Se regenera en cada corrida.\n")
    L.append(f"- Inicio: {st['started']} | dias corridos: {days:.1f} de {PAPER_WEEKS*7} | corridas: {len(st['runs'])}")
    L.append(f"- Capital inicial: ${cap:,.2f} | valor actual: ${eq:,.2f} | P&L: ${eq-cap:+,.2f} ({(eq/cap-1)*100:+.2f}%)")
    locked = sum(p["cost"] for p in st["positions"]); stuck = [p for p in st["positions"] if p.get("stuck")]
    L.append(f"- Efectivo libre: ${st['cash']:,.2f} | en ordenes abiertas: ${sum(o['cost'] for o in st['orders']):,.2f} ({len(st['orders'])}) | en posiciones: ${locked:,.2f} ({len(st['positions'])})")
    L.append(f"- Capital inmovilizado (mercado abierto > {STUCK_DAYS} dias tras su fecha de fin): ${sum(p['cost'] for p in stuck):,.2f} en {len(stuck)} posiciones")
    s = st["stats"]
    L.append(f"- Ordenes virtuales: {s['placed']} colocadas, {s['filled']} llenadas, {s['touched_not_filled']} tocadas sin llenarse (sorteo 30%), {s['expired']} expiradas")
    if st["halted"]:
        L.append(f"\n**SIMULACION DETENIDA: la perdida acumulada llego al {STOP_LOSS*100:.0f}%.**")
    L.append("\n## Operaciones cerradas: pago real contra precio pagado\n")
    if n:
        L.append("| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |")
        L.append("|---|---|---|---|---|---|---|---|")
        groups = sorted({c["rule"] for c in cl}) + ["TOTAL"]
        for g in groups:
            ss = [c for c in cl if g == "TOTAL" or c["rule"] == g]
            k = len(ss); w = sum(c["cost"] for c in ss)
            avgp = sum(c["px"] * c["cost"] for c in ss) / w
            pay = sum(c["result"] * c["cost"] for c in ss) / w
            lo, hi = wilson(sum(c["result"] for c in ss), k)
            L.append(f"| {g} | {k} | {avgp*100:.2f}c | {pay*100:.2f}% | {lo*100:.1f}-{hi*100:.1f}% | {(pay-avgp)*100:+.2f} pts | ${sum(c['pnl'] for c in ss):+,.2f} | {sum(c['days'] for c in ss)/k:.2f} |")
        worst = sorted(cl, key=lambda c: c["pnl"])[:10]
        L.append("\n## Peores casos\n")
        L.append("| P&L | Precio | Pago | Regla | Mercado |")
        L.append("|---|---|---|---|---|")
        for c in worst:
            if c["pnl"] < 0:
                L.append(f"| ${c['pnl']:+.2f} | {c['px']*100:.1f}c | {c['result']} | {c['rule']} | {c['q'][:90]} |")
    else:
        L.append("Todavia no hay operaciones cerradas.")
    if st["positions"]:
        L.append("\n## Posiciones abiertas\n")
        L.append("| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |")
        L.append("|---|---|---|---|---|---|")
        for p in sorted(st["positions"], key=lambda p: p["end_ts"])[:40]:
            L.append(f"| ${p['cost']:.2f} | {p['px']*100:.1f}c | {p.get('mark', p['px'])*100:.1f}c | {p['rule']} | {'si' if p.get('stuck') else ''} | {p['q'][:80]} |")
    shadow_report(st, L, now_utc().timestamp())
    L.append("\n## Veredicto\n")
    if n < 100 or days < PAPER_WEEKS * 7:
        L.append(f"Aun no hay veredicto: van {n} operaciones cerradas en {days:.1f} dias. El plan pide {PAPER_WEEKS} semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.")
    else:
        w = sum(c["cost"] for c in cl)
        edge = sum(c["pnl"] for c in cl) / w * 100
        ret = (eq / cap - 1) * 100
        if ret > 0 and edge > 0 and not st["halted"]:
            L.append(f"Positivo en papel: edge {edge:+.2f} pts por dolar invertido y {ret:+.2f}% sobre el capital, ya con el supuesto de 30% de llenado. Ojo: es simulacion; el llenado real, la profundidad del libro y los mercados que se quedan sin resolver pueden cambiar el resultado.")
        else:
            L.append(f"Sin ventaja en papel: edge {edge:+.2f} pts por dolar invertido y {ret:+.2f}% sobre el capital. No pasar a dinero real.")
    open(REPORT, "w", encoding="utf-8").write("\n".join(L) + "\n")


def main():
    os.makedirs(DIR, exist_ok=True)
    st = load_state()
    st.setdefault("shadow", [])
    now = now_utc().timestamp()
    nsh = shadow_update(st, now)
    settle(st, now)
    check_orders(st, now)
    eq = equity(st)
    if eq <= st["capital0"] * (1 - STOP_LOSS) and not st["halted"]:
        st["halted"] = True
        for o in st["orders"]:
            st["cash"] += o["cost"]
        st["orders"] = []
        log("halt", equity=round(eq, 2))
    started = dt.datetime.fromisoformat(st["started"].replace("Z", "+00:00")).timestamp()
    finished = now - started > PAPER_WEEKS * 7 * 86400
    nc = npl = nm = 0
    if not st["halted"] and not finished:
        markets = scan(now)
        nm = len(markets)
        nc, npl = place(st, now, markets)
        shadow_add(st, now, markets)
    st["cash"] = round(st["cash"], 4)
    st["runs"].append(dict(ts=iso(now_utc()), equity=round(equity(st), 2), cash=round(st["cash"], 2), orders=len(st["orders"]),
                           positions=len(st["positions"]), closed=len(st["closed"]), scanned=nm, candidates=nc, placed=npl,
                           shadow_open=len(st["shadow"]), shadow_closed=nsh))
    json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    report(st)
    r = st["runs"][-1]
    print(f"{PROFILE} corrida {len(st['runs'])}: escaneados {nm}, candidatos {nc}, ordenes nuevas {npl} | abiertas {r['orders']}, posiciones {r['positions']}, cerradas {r['closed']} | sombra abiertas {r['shadow_open']} | valor ${r['equity']}"
          + (" | DETENIDA por perdida" if st["halted"] else "") + (" | periodo de papel terminado" if finished else ""))


if __name__ == "__main__":
    main()
