"""Mercados cerrados que NO pagaron 0/1 (anulados, 50/50, etc.) en las mismas ventanas de la muestra.
El fetch original los descartaba; para un sweeper son la peor perdida posible (comprar a 99c y cobrar 50c)."""
import json, sqlite3, sys, datetime as dt
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "src")
from fetch_backtest import get, category, G, C
from fetch_universe import ts, F

DB = "data/voided.db"

def main():
    wins = [r[0] for r in sqlite3.connect("data/universe_low.db").execute("select a from windows")]
    db = sqlite3.connect(DB)
    db.execute("create table if not exists markets(id text primary key, question text, cat text, closed_ts real, end_ts real, game_ts real, pay0 real, token0 text, volume real, event text, uma text, win text)")
    db.execute("create table if not exists hist(id text primary key, json text)")
    def do(a, lo=None, hi=None, depth=0):
        A = lo or dt.datetime.fromisoformat(a.replace('Z', '+00:00')); B = hi or A + dt.timedelta(hours=2); out = []
        for off in range(0, 2100, 100):
            ms = get(f"{G}/markets?limit=100&offset={off}&closed=true&end_date_min={F(A)}&end_date_max={F(B)}")
            if not ms: break
            for m in ms:
                try:
                    pr = [float(x) for x in json.loads(m['outcomePrices'])]
                    if len(pr) == 2 and sorted(pr) != [0.0, 1.0]: out.append(m)
                except Exception: pass
            if len(ms) < 100: return a, out, False
        if depth < 5:
            mid = A + (B - A) / 2
            x = do(a, A, mid, depth + 1); y = do(a, mid, B, depth + 1)
            return a, x[1] + y[1], x[2] or y[2]
        return a, out, True
    trunc = 0
    with ThreadPoolExecutor(6) as ex:
        for a, ms, t in ex.map(do, wins):
            trunc += t
            for m in ms:
                try:
                    pr = [float(x) for x in json.loads(m['outcomePrices'])]; tk = json.loads(m['clobTokenIds'])
                    ct, et = ts(m.get('closedTime')), ts(m.get('endDate'))
                    if not ct or not et: continue
                    ev = (m.get('events') or [{}])[0]
                    db.execute("insert or ignore into markets values(?,?,?,?,?,?,?,?,?,?,?,?)", (m['id'], m['question'], category(m), ct, et, ts(m.get('gameStartTime')),
                               pr[0], tk[0], m.get('volumeNum') or 0, str(ev.get('id') or ''), m.get('umaResolutionStatuses') or '', a))
                except Exception: continue
    db.commit()
    todo = db.execute("select id,token0,closed_ts,end_ts from markets where id not in (select id from hist)").fetchall()
    print("ventanas truncadas:", trunc, "| mercados cerrados sin pago 0/1:", len(todo), flush=True)
    def job(r):
        mid, tok, ct, et = r
        start = max(min(et, ct) - 4 * 86400, ct - 30 * 86400)
        h = get(f"{C}/prices-history?market={tok}&startTs={int(start)}&endTs={int(ct)}&fidelity=60")
        return mid, (h or {}).get('history')
    with ThreadPoolExecutor(8) as ex:
        for mid, h in ex.map(job, todo):
            if h is not None: db.execute("insert or replace into hist values(?,?)", (mid, json.dumps([[p['t'], p['p']] for p in h])))
    db.commit()
    print(db.execute("select round(pay0,2),count(*) from markets group by 1 order by 2 desc limit 8").fetchall())
    print(db.execute("select cat,count(*) from markets group by 1").fetchall())

if __name__ == "__main__":
    main()
