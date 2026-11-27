# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 15.6 de 28 | corridas: 361
- Capital inicial: $1,000.00 | valor actual: $998.91 | P&L: $-1.09 (-0.11%)
- Efectivo libre: $403.86 | en ordenes abiertas: $352.16 (7) | en posiciones: $243.13 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 610 colocadas, 138 llenadas, 328 tocadas sin llenarse (sorteo 30%), 137 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 41 | 98.97c | 100.00% | 91.4-100.0% | +1.03 pts | $+21.56 | 0.28 |
| deportes_previo | 50 | 98.10c | 97.93% | 89.5-99.6% | -0.17 pts | $-4.75 | 0.32 |
| otros_cierre | 32 | 99.02c | 100.00% | 89.3-100.0% | +0.98 pts | $+16.41 | 0.37 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 133 | 98.42c | 98.43% | 94.7-99.6% | +0.01 pts | $-0.85 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |
| $-52.40 | 97.0c | 0.0 | deportes_previo | Spread: CF Cruz Azul (-3.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.30 | 98.8c | 98.8c | deportes_previo |  | FK Livyi Bereh vs. FK Kolos Kovalivka: O/U 6.5 |
| $44.49 | 97.7c | 97.0c | deportes_previo |  | Spread: Sisaket United FC (-2.5) |
| $49.95 | 98.1c | 98.2c | deportes_previo |  | Spread: Zira FK (-2.5) |
| $44.57 | 98.5c | 98.8c | otros_cierre |  | Will Alphabet Inc. (GOOGL) hit (LOW) $235 Week of November 23 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5620 | abiertas: 556 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1617 | 98.71c | 99.32% | +0.61 pts | +0.21 a +1.01 | 11 |
| cripto_cierre | tocadas | 1131 | 98.55c | 99.03% | +0.48 pts | -0.09 a +1.05 | 11 |
| deportes_previo | todas | 3140 | 98.31c | 98.68% | +0.37 pts | -0.03 a +0.76 | 43 |
| deportes_previo | tocadas | 2575 | 98.28c | 98.62% | +0.34 pts | -0.10 a +0.79 | 37 |
| otros_cierre | todas | 762 | 98.88c | 99.34% | +0.47 pts | -0.11 a +1.05 | 5 |
| otros_cierre | tocadas | 484 | 98.71c | 98.97% | +0.26 pts | -0.65 a +1.17 | 5 |
| post_fin_95_97 | todas | 101 | 95.90c | 94.06% | -1.84 pts | -6.47 a +2.80 | 6 |
| post_fin_95_97 | tocadas | 89 | 95.91c | 93.26% | -2.66 pts | -7.89 a +2.58 | 6 |
| TOTAL | todas | 5620 | 98.46c | 98.87% | +0.41 pts | +0.14 a +0.69 | 65 |
| TOTAL | tocadas | 4279 | 98.35c | 98.66% | +0.31 pts | -0.03 a +0.65 | 59 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Spread: Preston North End FC (-3.5)
- 99.2c -> pago 0.0 | deportes_previo | tocada | FC UTA Arad vs. Universitatea Craiova CS: O/U 7.5
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.9c -> pago 0.0 | deportes_previo | tocada | Dundee FC vs. Heart of Midlothian FC: O/U 7.5
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.8c -> pago 0.0 | deportes_previo | tocada | Spread: Charlton Athletic FC (-3.5)

## Veredicto

Aun no hay veredicto: van 133 operaciones cerradas en 15.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
