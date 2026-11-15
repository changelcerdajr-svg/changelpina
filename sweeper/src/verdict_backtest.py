"""Fase 2: criterio de paso/fallo, descontando el supuesto de 30% de llenado.

Dos lecturas del "30% de llenado", ambas reportadas por categoria x banda x horizonte:

A) Llenado al azar: de n oportunidades solo se llenan 0.30*n. El edge por operacion llenada no
   cambia, pero la muestra efectiva (y el IC de Wilson) se calcula con n_ef = 0.30*n.
B) Llenado con seleccion adversa (mas realista para una orden maker): pongo una compra limite al
   precio visto en el horizonte H. Solo se llena si el precio horario posterior toca ese nivel o
   mas abajo (alguien me vendio). Las ordenes que nunca se tocan no se llenan y no ganan nada.

PASA un grupo si, con n_ef >= 300: edge >= 1 punto Y el limite inferior del IC95 queda por encima
del precio medio pagado. "PASA estricto" exige que el limite inferior supere al precio por >= 1 punto.
"""
import json, sqlite3, sys, csv
sys.path.insert(0, "src")
from analyze_backtest import wilson, HORIZONS_H, BANDS, DB

FILL = 0.30
MIN_N = 300


def load():
    db = sqlite3.connect(DB)
    rows = db.execute("select m.id, m.cat, m.closed_ts, m.end_ts, m.won0, h.json from markets m join hist h on m.id=h.id").fetchall()
    samples = []  # (hh, cat, price, won, touched)
    for mid, cat, cts, ets, won0, hj in rows:
        hist = json.loads(hj)
        if not hist:
            continue
        for hh in HORIZONS_H:
            t = cts - hh * 3600
            p0 = None; later = []
            for pt in hist:
                if pt["t"] <= t:
                    p0 = pt["p"]
                else:
                    later.append(pt["p"])
            if p0 is None:
                continue
            if p0 >= 0.5:
                p, won = p0, won0
            else:
                p, won = 1 - p0, 1 - won0
                later = [1 - x for x in later]
            if 0.90 <= p < 0.99:
                # tocada: el precio posterior bajo al menos 1 tick (0.1c) por debajo de mi orden
                touched = int(any(x <= p - 0.001 for x in later))
                samples.append((hh, cat, p, won, touched))
    return len(rows), samples


def stats(ss, n_eff):
    n = len(ss)
    k = sum(s[3] for s in ss)
    avgp = sum(s[2] for s in ss) / n
    pay = k / n
    lo, hi = wilson(pay * n_eff, n_eff)
    return avgp * 100, pay * 100, lo * 100, hi * 100


def main():
    nm, samples = load()
    print(f"mercados con historial: {nm} | muestras 90-99c: {len(samples)}")
    cats = sorted({s[1] for s in samples}) + ["TODAS"]
    bands = BANDS + [(0.90, 0.99)]
    out = []
    for hh in HORIZONS_H:
        for cat in cats:
            for b in bands:
                ss = [s for s in samples if s[0] == hh and (cat == "TODAS" or s[1] == cat) and b[0] <= s[2] < b[1]]
                if len(ss) < 30:
                    continue
                band = f"{int(b[0]*100)}-{int(b[1]*100)}c"
                # A) llenado al azar
                nA = len(ss) * FILL
                pA, payA, loA, hiA = stats(ss, nA)
                # B) seleccion adversa
                tt = [s for s in ss if s[4]]
                fill_rate = len(tt) / len(ss)
                if tt:
                    pB, payB, loB, hiB = stats(tt, len(tt))
                else:
                    pB = payB = loB = hiB = 0

                def verdict(n_eff, p, pay, lo):
                    if n_eff < MIN_N:
                        return "n insuficiente"
                    if lo - p >= 1:
                        return "PASA estricto"
                    if pay - p >= 1 and lo > p:
                        return "PASA"
                    return "no pasa"

                out.append([f"{hh}h", cat, band, len(ss), round(pA, 2), round(payA, 2), round(payA - pA, 2),
                            round(nA), round(loA, 2), verdict(nA, pA, payA, loA),
                            round(fill_rate * 100, 1), len(tt), round(pB, 2), round(payB, 2), round(payB - pB, 2),
                            round(loB, 2), verdict(len(tt), pB, payB, loB)])
    hdr = ["horizonte", "cat", "banda", "n", "precio_c", "pago_pct", "edge_pts",
           "A_n_ef", "A_ic_bajo", "A_veredicto",
           "B_llenado_pct", "B_n_llenadas", "B_precio_c", "B_pago_pct", "B_edge_pts", "B_ic_bajo", "B_veredicto"]
    with open("data/backtest_verdict.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(hdr); w.writerows(out)
    w = csv.writer(sys.stdout, delimiter="|"); w.writerow(hdr); w.writerows(out)
    pa = [r for r in out if r[9].startswith("PASA")]
    pb = [r for r in out if r[16].startswith("PASA")]
    print(f"\ngrupos evaluados: {len(out)}")
    print(f"PASAN con llenado al azar (A): {len(pa)}")
    for r in pa: print("  A:", r[:10])
    print(f"PASAN con seleccion adversa (B): {len(pb)}")
    for r in pb: print("  B:", r[:4], r[10:])
    both = [r for r in out if r[9].startswith("PASA") and r[16].startswith("PASA")]
    print(f"PASAN en ambas lecturas: {len(both)}")
    print("VEREDICTO FASE 2:", "PASA" if both else ("DUDOSO: solo pasa sin seleccion adversa" if pa else "NO PASA"))


if __name__ == "__main__":
    main()
