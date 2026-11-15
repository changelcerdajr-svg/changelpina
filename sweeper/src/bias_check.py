"""Prueba del sesgo de seleccion por volumen final.

Junta la muestra de volumen >= $1,000 (universe.db) con su complemento < $1,000 (universe_low.db)
en las ventanas donde ambas tienen historial casi completo, y compara la calibracion del favorito.
"""
import sqlite3, json, bisect, collections, sys

def cover(db):
    d = sqlite3.connect(db)
    return {w: (n, k) for w, n, k in d.execute("select m.win,count(*),sum(h.id is not null) from markets m left join hist h on h.id=m.id group by 1")}

def samples(db, wins):
    d = sqlite3.connect(db); out = []
    for win, cat, ct, et, gt, won0, vol, smt, hj in d.execute("select m.win,m.cat,m.closed_ts,m.end_ts,m.game_ts,m.won0,m.volume,m.smt,h.json from markets m join hist h on m.id=h.id"):
        if win not in wins: continue
        h = json.loads(hj); T = [x[0] for x in h]
        for name, b, off in (("fin-24h", et, -24), ("fin-1h", et, -1), ("juego-1h", gt, -1)):
            if not b: continue
            t = b + off * 3600
            if t >= ct - 600: continue
            i = bisect.bisect_right(T, t) - 1
            if i < 0 or t - T[i] > 3 * 3600: continue
            p0 = h[i][1]; fp, w = (p0, won0) if p0 >= .5 else (1 - p0, 1 - won0)
            out.append((name, cat, fp, w, vol, smt))
    return out

def main():
    a, b = cover("data/universe.db"), cover("data/universe_low.db")
    wins = {w for w in a if w in b and a[w][1] >= .97 * a[w][0] and b[w][1] >= .97 * b[w][0]}
    print("ventanas completas en ambas muestras:", len(wins))
    hi, lo = samples("data/universe.db", wins), samples("data/universe_low.db", wins)
    print("muestras vol>=1000:", len(hi), "| vol<1000:", len(lo))
    bands = [(.5, .7), (.7, .8), (.8, .9), (.9, .95), (.95, .97), (.97, .99), (.99, .999)]
    for name in ("fin-24h", "fin-1h", "juego-1h"):
        print(f"\n{name}: banda | n, precio, pago, edge  para  vol<1000 | vol>=1000 | TODO")
        for x, y in bands:
            row = []
            for ss in (lo, hi, lo + hi):
                s = [q for q in ss if q[0] == name and x <= q[2] < y]
                n = len(s)
                if n == 0: row.append("-"); continue
                p = sum(q[2] for q in s) / n * 100; w = sum(q[3] for q in s) / n * 100
                row.append(f"{n:6d} {p:5.1f} {w:5.1f} {w-p:+5.1f}")
            print(f"  {int(x*100)}-{y*100:g}c | " + " | ".join(row))

if __name__ == "__main__":
    main()
