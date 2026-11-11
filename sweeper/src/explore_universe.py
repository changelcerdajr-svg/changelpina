"""Backtest ex-ante sobre el UNIVERSO COMPLETO (sin filtro de volumen final).

Usa las ventanas de 2h donde tenemos todos los mercados resueltos: volumen >= $1,000 (universe.db)
mas su complemento < $1,000 (universe_low.db). Filtrar por volumen final sesga el resultado (las
sorpresas generan volumen), asi que aqui no se filtra por nada que no se supiera de antemano.

- Momento de decision definido con datos conocidos de antemano: horas antes/despues de la fecha de
  fin publicada (fin) o antes del inicio del partido (juego). Solo si el mercado seguia abierto y el
  precio tenia < 3h de antiguedad.
- Edge = gano - precio (comprar al precio medio visto; un maker compraria igual o mas barato).
- Error estandar agrupado por evento. ic_bajo/ic_alto = edge +- 1.96*EE.
- "tocada": version con seleccion adversa; solo cuentan las ordenes cuyo precio fue alcanzado despues.
- ENTRENA = 2/3 de ventanas mas antiguas; PRUEBA = 1/3 mas reciente.
- Sin resolver: mercados de las mismas ventanas que siguen abiertos (unresolved.db); se cuentan
  aparte y se usa el peor caso (todos pierden) como prueba de estres.
"""
import json, sqlite3, math, sys, csv, bisect, os, re
from collections import defaultdict

POINTS = [("fin-72h", "end", -72), ("fin-24h", "end", -24), ("fin-6h", "end", -6), ("fin-1h", "end", -1),
          ("fin+6h", "end", 6), ("fin+24h", "end", 24), ("fin+72h", "end", 72),
          ("juego-24h", "game", -24), ("juego-1h", "game", -1)]
BANDS = [(0.80, 0.90), (0.90, 0.95), (0.95, 0.97), (0.97, 0.99), (0.99, 0.995), (0.995, 0.9995)]
TOP = [(0.95, 0.97), (0.97, 0.99), (0.99, 0.995), (0.995, 0.9995), (0.99, 0.9995), (0.97, 0.9995)]


def cat2(cat, q):
    """Reclasifica con el texto de la pregunta: los mercados de clima y de tuits traen hora de
    'partido' y caian en deportes; los marcadores exactos se separan por ser de cotizacion muy fina."""
    ql = q.lower()
    if re.search(r"temperature|°c|°f|rain|snow|precipitation|hurricane", ql):
        return "clima"
    if re.search(r"tweets?|posts? \d|truth social", ql):
        return "tuits"
    if ql.startswith("exact score"):
        return "marcador_exacto"
    return cat


def bname(b):
    return f"{b[0]*100:g}-{b[1]*100:g}c"


def complete_windows():
    def cover(db):
        d = sqlite3.connect(db)
        return {w: (n, k) for w, n, k in d.execute(
            "select m.win,count(*),sum(h.id is not null) from markets m left join hist h on h.id=m.id group by 1")}
    a, b = cover("data/universe.db"), cover("data/universe_low.db")
    return {w for w in a if w in b and a[w][1] >= .97 * a[w][0] and b[w][1] >= .97 * b[w][0]}


def points_for(h, et, gt, ct):
    T = [x[0] for x in h]
    for name, base, off in POINTS:
        b = et if base == "end" else gt
        if not b:
            continue
        t = b + off * 3600
        if ct is not None and t >= ct - 600:
            continue
        i = bisect.bisect_right(T, t) - 1
        if i < 0 or t - T[i] > 3 * 3600:
            continue
        yield name, t, i


def load():
    wins = complete_windows()
    S = []
    srcs = [("data/universe.db", "m.won0,m.neg_risk,m.smt"), ("data/universe_low.db", "m.won0,m.neg_risk,m.smt")]
    if os.path.exists("data/voided.db"):
        srcs.append(("data/voided.db", "m.pay0,0,'anulado'"))   # pago fraccionario (p.ej. 0.5)
    for dbn, cols in srcs:
        db = sqlite3.connect(dbn)
        for mid, q, cat, ct, et, gt, vol, ev, win, won0, neg, smt, hj in db.execute(
                f"select m.id,m.question,m.cat,m.closed_ts,m.end_ts,m.game_ts,m.volume,m.event,m.win,{cols},h.json from markets m join hist h on m.id=h.id"):
            if win not in wins:
                continue
            cat = cat2(cat, q)
            h = json.loads(hj)
            if len(h) < 2:
                continue
            for name, t, i in points_for(h, et, gt, ct):
                p0 = h[i][1]
                later = [x[1] for x in h[i + 1:]]
                if p0 >= 0.5:
                    p, won = p0, won0
                else:
                    p, won = 1 - p0, 1 - won0
                    later = [1 - x for x in later]
                if p < 0.80:
                    continue
                S.append(dict(id=mid, q=q, pt=name, cat=cat, p=p, won=won, touched=int(any(x <= p - 0.001 for x in later)),
                              ev=ev or mid, vol=vol, neg=neg, smt=smt, win=win, days=(ct - t) / 86400))
    return S, wins


def load_unresolved(wins):
    U = []
    if not os.path.exists("data/unresolved.db"):
        return U
    db = sqlite3.connect("data/unresolved.db")
    for mid, q, cat, et, gt, pnow, win, hj in db.execute(
            "select m.id,m.question,m.cat,m.end_ts,m.game_ts,m.p0,m.win,h.json from markets m join hist h on m.id=h.id"):
        if win not in wins:
            continue
        h = json.loads(hj)
        if len(h) < 2:
            continue
        for name, t, i in points_for(h, et, gt, None):
            p0 = h[i][1]
            p = max(p0, 1 - p0)
            if p < 0.80:
                continue
            now_fav = pnow if p0 >= 0.5 else 1 - pnow
            U.append(dict(id=mid, q=q, pt=name, cat=cat2(cat, q), p=p, now=now_fav, win=win))
    return U


def stat(ss):
    n = len(ss)
    if n == 0:
        return None
    mp = sum(s["p"] for s in ss) / n
    pay = sum(s["won"] for s in ss) / n
    edge = pay - mp
    cl = defaultdict(lambda: [0.0, 0])
    for s in ss:
        c = cl[s["ev"]]; c[0] += s["won"] - s["p"]; c[1] += 1
    G = len(cl)
    var = sum((a - k * edge) ** 2 for a, k in cl.values()) / (n * n)
    if G > 1:
        var *= G / (G - 1)
    se = math.sqrt(var)
    d = sorted(s["days"] for s in ss)
    return dict(n=n, ev=G, precio=mp * 100, pago=pay * 100, edge=edge * 100, lo=(edge - 1.96 * se) * 100,
                hi=(edge + 1.96 * se) * 100, dias=sum(d) / n, d90=d[int(n * 0.9)], perdidas=sum(s["won"] < 1 for s in ss), anulados=sum(0 < s["won"] < 1 for s in ss))


HDR = ["grupo", "n", "eventos", "perdidas", "precio_c", "pago_pct", "edge_pts", "ic_bajo", "ic_alto", "dias_prom", "dias_p90"]


def row(label, st):
    return [label, st["n"], st["ev"], st["perdidas"], round(st["precio"], 2), round(st["pago"], 2), round(st["edge"], 3),
            round(st["lo"], 3), round(st["hi"], 3), round(st["dias"], 2), round(st["d90"], 2)]


def main():
    S, wins = load()
    U = load_unresolved(wins)
    ws = sorted(wins, key=lambda w: w)
    cut = sorted(ws)[int(len(ws) * 2 / 3)]
    print(f"ventanas completas: {len(wins)} | muestras (favorito >= 80c): {len(S)} | corte entrena/prueba: {cut}")
    out = []
    w = csv.writer(sys.stdout, delimiter="|")

    def rep(label, ss, minn=50):
        if len(ss) >= minn:
            r = row(label, stat(ss)); out.append(r); w.writerow(r)
            return r

    cats = sorted({s["cat"] for s in S}) + ["TODAS"]
    sel = lambda pt, cat, b: [s for s in S if s["pt"] == pt and (cat == "TODAS" or s["cat"] == cat) and b[0] <= s["p"] < b[1]]

    print("\n# 1. Calibracion del favorito, universo completo"); w.writerow(HDR)
    for name, _, _ in POINTS:
        for b in BANDS:
            rep(f"{name} | TODAS | {bname(b)}", sel(name, "TODAS", b))

    print("\n# 2. Reglas candidatas (bandas altas) con entrena/prueba, seleccion adversa y sin resolver")
    hdr2 = ["regla", "n", "perdidas", "precio_c", "edge", "ic_bajo", "E_n", "E_edge", "E_ic_bajo", "P_n", "P_edge", "P_ic_bajo",
            "toc_n", "toc_pct", "toc_edge", "toc_ic_bajo", "dias_prom", "dias_p90", "sin_resolver", "edge_peor_caso", "veredicto"]
    w.writerow(hdr2)
    rules = []
    for name, _, _ in POINTS:
        for cat in cats:
            for b in TOP:
                ss = sel(name, cat, b)
                if len(ss) < 300:
                    continue
                a = stat(ss)
                tr = stat([s for s in ss if s["win"] < cut]); te = stat([s for s in ss if s["win"] >= cut])
                tt = [s for s in ss if s["touched"]]
                tc = stat(tt)
                un = [u for u in U if u["pt"] == name and (cat == "TODAS" or u["cat"] == cat) and b[0] <= u["p"] < b[1]]
                # peor caso: todos los que siguen sin resolver acaban perdiendo
                worst = (sum(s["won"] - s["p"] for s in ss) + sum(-u["p"] for u in un)) / (len(ss) + len(un)) * 100
                ok = (tr and te and tr["n"] >= 150 and te["n"] >= 100 and tr["lo"] > 0 and te["edge"] > 0 and a["lo"] > 0)
                ok_adv = bool(tc) and tc["n"] >= 100 and tc["edge"] > 0
                ver = "PASA" if ok and ok_adv and worst > 0 else ("pasa sin estres" if ok and ok_adv else ("pasa solo sin seleccion adversa" if ok else "no"))
                r = [f"{name} | {cat} | {bname(b)}", a["n"], a["perdidas"], round(a["precio"], 2), round(a["edge"], 3), round(a["lo"], 3),
                     tr["n"] if tr else 0, round(tr["edge"], 3) if tr else "", round(tr["lo"], 3) if tr else "",
                     te["n"] if te else 0, round(te["edge"], 3) if te else "", round(te["lo"], 3) if te else "",
                     tc["n"] if tc else 0, round(100 * len(tt) / len(ss), 1), round(tc["edge"], 3) if tc else "", round(tc["lo"], 3) if tc else "",
                     round(a["dias"], 2), round(a["d90"], 2), len(un), round(worst, 3), ver]
                rules.append(r); w.writerow(r)
    with open("data/universe_calibration.csv", "w", newline="") as f:
        cw = csv.writer(f); cw.writerow(HDR); cw.writerows(out)
    with open("data/universe_rules.csv", "w", newline="") as f:
        cw = csv.writer(f); cw.writerow(hdr2); cw.writerows(rules)

    print("\n# 3. Reglas que pasan")
    for r in rules:
        if r[-1].startswith("PASA") or r[-1] == "pasa sin estres":
            print("  ", r[-1], "|", r[0], "| n", r[1], "perdidas", r[2], "edge", r[4], "ic_bajo", r[5], "| prueba", r[10], "| tocada", r[14], "| dias", r[16], "| sin resolver", r[18], "peor caso", r[19])

    print("\n# 4. Perdidas en la banda 99-99.95c (todas las del universo)")
    seen = set()
    for s in S:
        if s["p"] >= 0.99 and s["won"] < 1 and (s["id"], s["pt"]) not in seen:
            seen.add((s["id"], s["pt"]))
            print("  ", s["pt"], s["cat"], round(s["p"], 4), "pago", s["won"], "vol", round(s["vol"]), "|", s["q"][:90])
    print("\n# 5. Sin resolver con favorito >= 99c en el momento de decision")
    c = defaultdict(lambda: [0, 0])
    for u in U:
        if u["p"] >= 0.99:
            k = c[(u["pt"], u["cat"])]; k[0] += 1; k[1] += u["now"] < 0.9
    for k in sorted(c):
        print("  ", k, "sin resolver:", c[k][0], "| de esos, hoy el favorito cotiza < 90c:", c[k][1])


if __name__ == "__main__":
    main()
