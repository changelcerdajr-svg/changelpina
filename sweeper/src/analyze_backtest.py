"""Fase 2: calibracion. Un resultado que cotiza entre 90 y 99 centavos, ¿paga $1 mas seguido que su precio?

Para cada mercado resuelto y cada horizonte antes del cierre, toma el ultimo precio conocido
del resultado favorito. Si cae en la banda, registra (precio, gano). El edge por operacion es
gano - precio (comprar a ese precio y cobrar $1 o $0). Sin comisiones: el plan solo usa ordenes maker.
"""
import json, sqlite3, math, sys, csv
from collections import defaultdict

DB = "data/backtest.db"
HORIZONS_H = [1, 6, 24, 72]
BANDS = [(0.90, 0.95), (0.95, 0.97), (0.97, 0.99)]


def price_at(hist, ts):
    p = None
    for pt in hist:
        if pt["t"] <= ts:
            p = pt["p"]
        else:
            break
    return p


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def main():
    db = sqlite3.connect(DB)
    rows = db.execute(
        "select m.id, m.cat, m.closed_ts, m.end_ts, m.won0, h.json from markets m join hist h on m.id=h.id"
    ).fetchall()
    samples = []  # (horizon, cat, post_end, price, won)
    for mid, cat, cts, ets, won0, hj in rows:
        hist = json.loads(hj)
        if not hist:
            continue
        for hh in HORIZONS_H:
            t = cts - hh * 3600
            p0 = price_at(hist, t)
            if p0 is None:
                continue
            # favorito: el lado con precio >= 0.5
            if p0 >= 0.5:
                p, won = p0, won0
            else:
                p, won = 1 - p0, 1 - won0
            if 0.90 <= p < 0.99:
                samples.append((hh, cat, int(t > ets), p, won))
    print(f"mercados con historial: {len(rows)} | muestras en banda 90-99c: {len(samples)}")

    out = []

    def report(label, ss):
        n = len(ss)
        if n == 0:
            return
        k = sum(s[4] for s in ss)
        avgp = sum(s[3] for s in ss) / n
        lo, hi = wilson(k, n)
        edge = k / n - avgp
        out.append([label, n, round(avgp * 100, 2), round(k / n * 100, 2), round(lo * 100, 2), round(hi * 100, 2), round(edge * 100, 2)])

    for hh in HORIZONS_H:
        report(f"{hh}h | todas", [s for s in samples if s[0] == hh])
    for hh in [6, 24]:
        for b in BANDS:
            report(f"{hh}h | {int(b[0]*100)}-{int(b[1]*100)}c", [s for s in samples if s[0] == hh and b[0] <= s[3] < b[1]])
        for cat in sorted({s[1] for s in samples}):
            report(f"{hh}h | {cat}", [s for s in samples if s[0] == hh and s[1] == cat])
        report(f"{hh}h | ya paso la fecha de fin", [s for s in samples if s[0] == hh and s[2] == 1])
        report(f"{hh}h | antes de la fecha de fin", [s for s in samples if s[0] == hh and s[2] == 0])

    hdr = ["grupo", "n", "precio_prom_c", "pago_pct", "ic95_bajo", "ic95_alto", "edge_pts"]
    w = csv.writer(sys.stdout, delimiter="|")
    w.writerow(hdr)
    w.writerows(out)
    with open("data/backtest_results.csv", "w", newline="") as f:
        cw = csv.writer(f)
        cw.writerow(hdr)
        cw.writerows(out)


if __name__ == "__main__":
    main()
