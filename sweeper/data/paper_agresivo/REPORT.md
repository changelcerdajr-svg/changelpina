# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 10.4 de 28 | corridas: 231
- Capital inicial: $1,000.00 | valor actual: $914.41 | P&L: $-85.59 (-8.56%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $349.86 (5) | en posiciones: $576.50 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 463 colocadas, 209 llenadas, 199 tocadas sin llenarse (sorteo 30%), 50 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 61 | 98.78c | 100.00% | 94.1-100.0% | +1.22 pts | $+50.10 | 0.17 |
| deportes_previo | 96 | 98.03c | 96.15% | 91.2-98.9% | -1.88 pts | $-145.75 | 0.27 |
| otros_cierre | 36 | 99.66c | 100.00% | 90.4-100.0% | +0.34 pts | $+8.42 | 0.35 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 201 | 98.50c | 98.02% | 95.7-99.5% | -0.48 pts | $-73.64 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 87.8c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $90.05 | 97.9c | 97.9c | deportes_previo |  | Spread: Al Gharafa SC (-2.5) |
| $73.33 | 97.9c | 97.3c | deportes_previo |  | Spread: Pakhtakor (-1.5) |
| $90.52 | 97.6c | 99.4c | deportes_previo |  | Spread: AD Ceuta FC (-2.5) |
| $90.52 | 96.8c | 96.8c | deportes_previo |  | Spread: UD Almería (-3.5) |
| $17.67 | 99.8c | 100.0c | deportes_previo |  | Virginia Tech Hokies vs. UT Martin Skyhawks (W) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 12166 | abiertas: 2251 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3273 | 98.83c | 98.99% | +0.16 pts | -0.18 a +0.50 | 33 |
| clima_cierre | tocadas | 3030 | 98.85c | 98.91% | +0.06 pts | -0.31 a +0.43 | 33 |
| cripto_cierre | todas | 1589 | 98.69c | 98.17% | -0.51 pts | -1.17 a +0.14 | 29 |
| cripto_cierre | tocadas | 1446 | 98.74c | 97.99% | -0.75 pts | -1.46 a -0.03 | 29 |
| deportes_previo | todas | 5811 | 98.04c | 97.41% | -0.63 pts | -1.04 a -0.23 | 153 |
| deportes_previo | tocadas | 5676 | 98.08c | 97.38% | -0.69 pts | -1.10 a -0.28 | 151 |
| otros_cierre | todas | 1269 | 99.00c | 97.08% | -1.91 pts | -2.83 a -0.99 | 37 |
| otros_cierre | tocadas | 1184 | 98.96c | 96.88% | -2.09 pts | -3.07 a -1.10 | 37 |
| post_fin_90_97 | todas | 224 | 94.02c | 92.86% | -1.17 pts | -4.50 a +2.17 | 16 |
| post_fin_90_97 | tocadas | 189 | 94.13c | 91.53% | -2.59 pts | -6.51 a +1.33 | 16 |
| TOTAL | todas | 12166 | 98.36c | 97.82% | -0.55 pts | -0.80 a -0.29 | 268 |
| TOTAL | tocadas | 11525 | 98.39c | 97.71% | -0.68 pts | -0.95 a -0.41 | 266 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) finish week of November 16 above $270?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Amazon (AMZN) close at $245-$250 on the final day of trading of the week of Nov 16 – 

## Veredicto

Aun no hay veredicto: van 201 operaciones cerradas en 10.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
