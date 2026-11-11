"""Fase 2: descarga mercados resueltos y su historial de precios (solo API publica)."""
import json, urllib.request, datetime as dt, time, re, sqlite3, sys
from concurrent.futures import ThreadPoolExecutor
G="https://gamma-api.polymarket.com"; C="https://clob.polymarket.com"
DB="data/backtest.db"
def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'sweeper-research'}),timeout=40) as r: return json.load(r)
        except Exception as e:
            if i==tries-1: return None
            time.sleep(1.5*(i+1))
def category(m):
    q=(m.get('question') or '').lower()
    if m.get('gameStartTime') or m.get('sportsMarketType') or re.search(r' vs\.? |counter-strike|valorant|league of legends|dota|nba|nfl|mlb|nhl|ufc|tennis|premier league|la liga|serie a|o/u|spread|handicap|win on 20',q): return 'deportes'
    if re.search(r'bitcoin|btc|ethereum|\beth\b|solana|\bsol\b|xrp|crypto|up or down|price of',q): return 'cripto'
    if re.search(r'elect|president|senate|house|governor|minister|party|vote|congress|mayor|parliament|nominee|primary|seat',q): return 'politica'
    if re.search(r'war|ceasefire|iran|israel|ukraine|russia|china|taiwan|strike|invade|treaty|nato|peace',q): return 'geopolitica'
    if re.search(r'fed|rate|cpi|inflation|gdp|stock|s&p|nasdaq|earnings|ipo',q): return 'economia'
    return 'otros'
def main(weeks=36, per_week=300):
    db=sqlite3.connect(DB)
    db.execute("create table if not exists markets(id text primary key, question text, cat text, closed_ts real, end_ts real, won0 int, token0 text, volume real, fees int)")
    db.execute("create table if not exists hist(id text primary key, json text)")
    now=dt.datetime.now(dt.timezone.utc)
    for w in range(1,weeks+1):
        a=(now-dt.timedelta(weeks=w)).strftime('%Y-%m-%dT%H:%M:%SZ'); b=(now-dt.timedelta(weeks=w-1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        got=0
        for off in range(0,per_week,100):
            ms=get(f"{G}/markets?limit=100&offset={off}&closed=true&end_date_min={a}&end_date_max={b}&volume_num_min=5000&order=volumeNum&ascending=false")
            if not ms: break
            for m in ms:
                try:
                    pr=[float(x) for x in json.loads(m['outcomePrices'])]; tk=json.loads(m['clobTokenIds'])
                    if len(pr)!=2 or sorted(pr)!=[0.0,1.0] or not m.get('closedTime'): continue
                    ct=dt.datetime.fromisoformat(m['closedTime'].replace(' ','T').replace('+00','+00:00')).timestamp()
                    et=dt.datetime.fromisoformat(m['endDate'].replace('Z','+00:00')).timestamp()
                except Exception: continue
                db.execute("insert or ignore into markets values(?,?,?,?,?,?,?,?,?)",(m['id'],m['question'],category(m),ct,et,int(pr[0]==1.0),tk[0],m.get('volumeNum') or 0,int(bool(m.get('feesEnabled')))))
                got+=1
            if len(ms)<100: break
        db.commit(); print('semana',w,'mercados',got,flush=True)
    todo=[r for r in db.execute("select id,token0,closed_ts from markets where id not in (select id from hist)")]
    print('historiales a bajar',len(todo),flush=True)
    def job(r):
        mid,tok,ct=r
        h=get(f"{C}/prices-history?market={tok}&startTs={int(ct-10*86400)}&endTs={int(ct)}&fidelity=60")
        return mid,(h or {}).get('history')
    with ThreadPoolExecutor(8) as ex:
        for i,(mid,h) in enumerate(ex.map(job,todo)):
            if h is not None: db.execute("insert or replace into hist values(?,?)",(mid,json.dumps(h)))
            if i%300==0: db.commit(); print('hist',i,flush=True)
    db.commit()
if __name__=="__main__": main(int(sys.argv[1]) if len(sys.argv)>1 else 36, int(sys.argv[2]) if len(sys.argv)>2 else 300)
