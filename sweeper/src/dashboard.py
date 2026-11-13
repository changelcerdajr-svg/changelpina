"""Genera sweeper/dashboard.html: una pagina sola (se abre con doble clic) con el estado del simulador."""
import json, os, csv, math, datetime as dt

PROFILES = [("base", "data/paper"), ("agresivo", "data/paper_agresivo")]
TEMPLATE = "src/dashboard_template.html"
OUT = "dashboard.html"


def build(DIR, now):
    if not os.path.exists(f"{DIR}/state.json"):
        return None
    st = json.load(open(f"{DIR}/state.json"))
    started = dt.datetime.fromisoformat(st["started"].replace("Z", "+00:00"))
    # bitacora: ultimos eventos, con el nombre del mercado aunque el evento no lo traiga
    names, events = {}, []
    if os.path.exists(f"{DIR}/log.jsonl"):
        for line in open(f"{DIR}/log.jsonl"):
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("q"):
                names[e.get("id")] = e["q"]
            events.append(dict(t=e["ts"], ev=e["ev"], q=e.get("q") or names.get(e.get("id"), ""), px=e.get("px"),
                               pnl=e.get("pnl"), result=e.get("result")))
    # registro sombra: edge de las oportunidades "tocadas"
    shadow = None
    p = f"{DIR}/shadow_closed.csv"
    if os.path.exists(p):
        rows = list(csv.DictReader(open(p, newline="")))
        tt = [float(r["result"]) - float(r["px"]) for r in rows if r["touched"] == "1"]
        if tt:
            n = len(tt); mean = sum(tt) / n
            se = math.sqrt(sum((v - mean) ** 2 for v in tt) / (n - 1)) / math.sqrt(n) if n > 1 else 0
            shadow = dict(n=len(rows), n_t=n, edge_t=round(mean * 100, 2), lo_t=round((mean - 1.96 * se) * 100, 2),
                          hi_t=round((mean + 1.96 * se) * 100, 2),
                          losses_t=sum(1 for r in rows if r["touched"] == "1" and float(r["result"]) < 1))
    eq = st["cash"] + sum(o["cost"] for o in st["orders"]) + sum(x["shares"] * x.get("mark", x["px"]) for x in st["positions"])
    slim = lambda x: dict(q=x["q"], px=x["px"], cost=x["cost"], rule=x["rule"])
    data = dict(
        started=st["started"], capital0=st["capital0"], equity=round(eq, 2),
        days=(now - started).total_seconds() / 86400, halted=st["halted"],
        n_orders=len(st["orders"]), n_pos=len(st["positions"]), n_closed=len(st["closed"]),
        wins=sum(1 for c in st["closed"] if c["pnl"] >= 0), losses=sum(1 for c in st["closed"] if c["pnl"] < 0),
        runs=[[r["ts"], r["equity"]] for r in st["runs"]],
        positions=[slim(x) for x in st["positions"]], orders=[slim(x) for x in st["orders"]],
        closed=[dict(q=c["q"], px=c["px"], pnl=c["pnl"], rule=c["rule"]) for c in st["closed"][-12:][::-1]],
        events=events[-60:], shadow=shadow)
    return data


def main():
    now = dt.datetime.now(dt.timezone.utc)
    profiles = {k: d for k, d in ((k, build(p, now)) for k, p in PROFILES) if d}
    data = dict(updated=now.strftime("%Y-%m-%dT%H:%M:%SZ"), profiles=profiles)
    html = open(TEMPLATE).read().replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    open(OUT, "w").write(html)
    print("dashboard.html actualizado")


if __name__ == "__main__":
    main()
