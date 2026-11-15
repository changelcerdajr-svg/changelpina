"""Fase 2, punto 4: sesgo de supervivencia / capital inmovilizado.

Lista mercados binarios que SIGUEN ABIERTOS aunque su fecha de fin ya paso y cuyo favorito
cotiza >= 90c. El backtest solo ve mercados ya resueltos; estos son los que un sweeper
tendria comprados sin cobrar. Solo API publica de Gamma.
"""
import json, urllib.request, datetime as dt, time, csv, sys
sys.path.insert(0, "src")
from fetch_backtest import get, category, G

OUT = "data/stuck_markets.csv"


def main(min_days_late=1.0):
    now = dt.datetime.now(dt.timezone.utc)
    cutoff = (now - dt.timedelta(days=min_days_late)).strftime('%Y-%m-%dT%H:%M:%SZ')
    rows = []
    for off in range(0, 5000, 100):
        ms = get(f"{G}/markets?limit=100&offset={off}&closed=false&end_date_max={cutoff}&volume_num_min=5000&order=volumeNum&ascending=false")
        if not ms:
            break
        for m in ms:
            try:
                pr = [float(x) for x in json.loads(m['outcomePrices'])]
                if len(pr) != 2:
                    continue
                et = dt.datetime.fromisoformat(m['endDate'].replace('Z', '+00:00'))
            except Exception:
                continue
            fav = max(pr)
            if fav < 0.90:
                continue
            uma = m.get('umaResolutionStatus') or ''
            rows.append([m['id'], category(m), round(fav * 100, 1), round((now - et).total_seconds() / 86400, 1),
                         round(m.get('volumeNum') or 0), round(m.get('liquidityNum') or 0), uma,
                         int(bool(m.get('acceptingOrders'))), m['question'][:110]])
        if len(ms) < 100:
            break
    rows.sort(key=lambda r: -r[3])
    hdr = ["id", "cat", "favorito_c", "dias_pasada_fecha_fin", "volumen", "liquidez", "uma", "acepta_ordenes", "pregunta"]
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f); w.writerow(hdr); w.writerows(rows)
    n = len(rows)
    print(f"mercados abiertos pasada su fecha de fin con favorito >= 90c: {n}")
    if not n:
        return
    late = sorted(r[3] for r in rows)
    print(f"dias de retraso: mediana {late[n//2]}, p90 {late[int(n*0.9)]}, max {late[-1]}")
    for lo, hi in [(90, 95), (95, 97), (97, 99), (99, 100.1)]:
        ss = [r for r in rows if lo <= r[2] < hi]
        print(f"  banda {lo}-{int(hi)}c: {len(ss)} mercados, >7d tarde: {sum(r[3] > 7 for r in ss)}, >30d tarde: {sum(r[3] > 30 for r in ss)}")
    print("con estado UMA (propuesta/disputa):", sum(1 for r in rows if r[6]))
    cats = {}
    for r in rows:
        cats[r[1]] = cats.get(r[1], 0) + 1
    print("por categoria:", cats)


if __name__ == "__main__":
    main()
