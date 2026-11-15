"""Muestra SIN sesgo de volumen: universo completo de mercados binarios resueltos (volumen >= $1,000)
dentro de ventanas de 2 horas elegidas al azar (2 por dia), en vez del top por volumen de cada semana.

Guarda ademas campos conocidos de antemano (fecha de fin, inicio del partido, negRisk, evento) y el
historial horario desde 4 dias antes de la fecha de fin hasta el cierre. Solo API publica.
"""
import json, urllib.request, datetime as dt, time, sqlite3, sys, random
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, "src")
from fetch_backtest import get, category, G, C

import os
DB = os.environ.get("UDB", "data/universe.db")
VMIN = int(os.environ.get("VMIN", 1000))
VMAX = os.environ.get("VMAX")  # opcional: tope de volumen (para bajar el complemento de bajo volumen)
F = lambda x: x.strftime('%Y-%m-%dT%H:%M:%SZ')


def ts(s):
    if not s:
        return None
    try:
        s = s.replace(' ', 'T').replace('Z', '+00:00')
        if s.endswith('+00'):
            s += ':00'
        return dt.datetime.fromisoformat(s).timestamp()
    except Exception:
        return None


def window(a, b, depth=0):
    """Todos los mercados cerrados con endDate en [a,b). Parte la ventana si choca con el tope de offset."""
    out = []
    for off in range(0, 2100, 100):
        ms = get(f"{G}/markets?limit=100&offset={off}&closed=true&end_date_min={F(a)}&end_date_max={F(b)}&volume_num_min={VMIN}" + (f"&volume_num_max={VMAX}" if VMAX else ""))
        if not ms:
            break
        out += ms
        if len(ms) < 100:
            return out
    if len(out) >= 2000 and depth < 6:
        mid = a + (b - a) / 2
        return window(a, mid, depth + 1) + window(mid, b, depth + 1)
    return out


def main(days=252, per_day=2, skip_recent=7):
    db = sqlite3.connect(DB)
    db.execute("""create table if not exists markets(id text primary key, question text, cat text, closed_ts real, end_ts real,
        game_ts real, start_ts real, won0 int, token0 text, volume real, fees int, neg_risk int, event text, smt text, uma text, win text)""")
    db.execute("create table if not exists hist(id text primary key, json text)")
    db.execute("create table if not exists windows(a text primary key, n int)")
    rnd = random.Random(20261111)
    today = dt.datetime.now(dt.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    wins = []
    for d in range(skip_recent, skip_recent + days):
        day = today - dt.timedelta(days=d)
        for h in rnd.sample(range(12), per_day):
            wins.append(day + dt.timedelta(hours=2 * h))
    done = {r[0] for r in db.execute("select a from windows")}
    wins = [w for w in wins if F(w) not in done]

    def do(a):
        return a, window(a, a + dt.timedelta(hours=2))

    with ThreadPoolExecutor(6) as ex:
        for i, (a, ms) in enumerate(ex.map(do, wins)):
            n = 0
            seen = set()
            for m in ms:
                try:
                    if m['id'] in seen:
                        continue
                    seen.add(m['id'])
                    pr = [float(x) for x in json.loads(m['outcomePrices'])]
                    tk = json.loads(m['clobTokenIds'])
                    ct, et = ts(m.get('closedTime')), ts(m.get('endDate'))
                    if len(pr) != 2 or sorted(pr) != [0.0, 1.0] or not ct or not et:
                        continue
                    ev = (m.get('events') or [{}])[0]
                    db.execute("insert or ignore into markets values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               (m['id'], m['question'], category(m), ct, et, ts(m.get('gameStartTime')), ts(m.get('startDate')),
                                int(pr[0] == 1.0), tk[0], m.get('volumeNum') or 0, int(bool(m.get('feesEnabled'))),
                                int(bool(m.get('negRisk'))), str(ev.get('id') or ''), m.get('sportsMarketType') or '',
                                m.get('umaResolutionStatuses') or '', F(a)))
                    n += 1
                except Exception:
                    continue
            db.execute("insert or replace into windows values(?,?)", (F(a), n))
            if i % 20 == 0:
                db.commit(); print('ventana', i, 'de', len(wins), F(a), n, flush=True)
    db.commit()
    todo = db.execute("select id,token0,closed_ts,end_ts from markets where id not in (select id from hist)").fetchall()
    print('historiales a bajar', len(todo), flush=True)

    def job(r):
        mid, tok, ct, et = r
        start = max(min(et, ct) - 4 * 86400, ct - 30 * 86400)
        h = get(f"{C}/prices-history?market={tok}&startTs={int(start)}&endTs={int(ct)}&fidelity=60")
        return mid, (h or {}).get('history')

    with ThreadPoolExecutor(16) as ex:
        for i, (mid, h) in enumerate(ex.map(job, todo)):
            if h is not None:
                db.execute("insert or replace into hist values(?,?)", (mid, json.dumps([[p['t'], p['p']] for p in h])))
            if i % 1000 == 0:
                db.commit(); print('hist', i, flush=True)
    db.commit()


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 252, int(sys.argv[2]) if len(sys.argv) > 2 else 2)
