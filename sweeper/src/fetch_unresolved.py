"""Sesgo de supervivencia: para las mismas ventanas de la muestra, baja los mercados que TODAVIA
no han cerrado (closed=false) aunque su fecha de fin cayo en la ventana. Guarda precio actual e
historial alrededor de la fecha de fin para poder incluirlos en el backtest como capital inmovilizado."""
import json, sqlite3, sys, datetime as dt
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "src")
from fetch_backtest import get, category, G, C
from fetch_universe import ts, F

DB = "data/unresolved.db"

def main():
    wins = [r[0] for r in sqlite3.connect("data/universe_low.db").execute("select a from windows")]
    db = sqlite3.connect(DB)
    db.execute("create table if not exists markets(id text primary key, question text, cat text, end_ts real, game_ts real, p0 real, token0 text, volume real, event text, uma text, win text)")
    db.execute("create table if not exists hist(id text primary key, json text)")
    def do(a):
        A = dt.datetime.fromisoformat(a.replace('Z', '+00:00')); out = []
        for off in range(0, 2100, 100):
            ms = get(f"{G}/markets?limit=100&offset={off}&closed=false&end_date_min={a}&end_date_max={F(A + dt.timedelta(hours=2))}")
            if not ms: break
            out += ms
            if len(ms) < 100: break
        return a, out
    with ThreadPoolExecutor(6) as ex:
        for a, ms in ex.map(do, wins):
            for m in ms:
                try:
                    pr = [float(x) for x in json.loads(m['outcomePrices'])]; tk = json.loads(m['clobTokenIds'])
                    if len(pr) != 2: continue
                    ev = (m.get('events') or [{}])[0]
                    db.execute("insert or ignore into markets values(?,?,?,?,?,?,?,?,?,?,?)", (m['id'], m['question'], category(m), ts(m['endDate']),
                               ts(m.get('gameStartTime')), pr[0], tk[0], m.get('volumeNum') or 0, str(ev.get('id') or ''), m.get('umaResolutionStatuses') or '', a))
                except Exception: continue
    db.commit()
    todo = db.execute("select id,token0,end_ts from markets where id not in (select id from hist)").fetchall()
    print("mercados sin resolver en las ventanas:", len(todo), flush=True)
    def job(r):
        mid, tok, et = r
        h = get(f"{C}/prices-history?market={tok}&startTs={int(et - 4*86400)}&endTs={int(et + 8*86400)}&fidelity=60")
        return mid, (h or {}).get('history')
    with ThreadPoolExecutor(8) as ex:
        for mid, h in ex.map(job, todo):
            if h is not None: db.execute("insert or replace into hist values(?,?)", (mid, json.dumps([[p['t'], p['p']] for p in h])))
    db.commit()
    print(db.execute("select count(*), sum(max(p0,1-p0)>=0.9), sum(max(p0,1-p0)>=0.99) from markets").fetchone())
    print(db.execute("select cat,count(*) from markets group by 1").fetchall())

if __name__ == "__main__":
    main()
