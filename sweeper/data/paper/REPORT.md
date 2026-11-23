# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 11.9 de 28 | corridas: 265
- Capital inicial: $1,000.00 | valor actual: $1,027.30 | P&L: $+27.30 (+2.73%)
- Efectivo libre: $360.62 | en ordenes abiertas: $461.71 (10) | en posiciones: $205.75 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 454 colocadas, 107 llenadas, 235 tocadas sin llenarse (sorteo 30%), 102 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 31 | 98.95c | 100.00% | 89.0-100.0% | +1.05 pts | $+16.90 | 0.31 |
| deportes_previo | 37 | 98.20c | 100.00% | 90.6-100.0% | +1.80 pts | $+34.14 | 0.34 |
| otros_cierre | 26 | 99.02c | 100.00% | 87.1-100.0% | +0.98 pts | $+13.24 | 0.41 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 103 | 98.44c | 98.98% | 94.7-99.8% | +0.54 pts | $+28.08 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.40 | 96.0c | 96.0c | post_fin_95_97 |  | Will the highest temperature in Austin be between 56-57°F on November 23? |
| $51.12 | 98.7c | 98.9c | deportes_previo |  | Alcorn State Braves vs. Michigan State Spartans (W) |
| $51.40 | 98.9c | 97.5c | cripto_cierre |  | Microsoft (MSFT) Up or Down on November 23? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4204 | abiertas: 461 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1212 | 98.73c | 99.17% | +0.45 pts | -0.06 a +0.96 | 10 |
| cripto_cierre | tocadas | 839 | 98.56c | 98.81% | +0.25 pts | -0.48 a +0.98 | 10 |
| deportes_previo | todas | 2335 | 98.31c | 98.97% | +0.66 pts | +0.26 a +1.07 | 25 |
| deportes_previo | tocadas | 1987 | 98.28c | 98.89% | +0.61 pts | +0.16 a +1.06 | 23 |
| otros_cierre | todas | 573 | 98.82c | 99.30% | +0.49 pts | -0.20 a +1.17 | 4 |
| otros_cierre | tocadas | 375 | 98.69c | 98.93% | +0.24 pts | -0.81 a +1.29 | 4 |
| post_fin_95_97 | todas | 84 | 95.88c | 92.86% | -3.02 pts | -8.56 a +2.52 | 6 |
| post_fin_95_97 | tocadas | 75 | 95.90c | 92.00% | -3.90 pts | -10.08 a +2.28 | 6 |
| TOTAL | todas | 4204 | 98.45c | 98.95% | +0.50 pts | +0.20 a +0.81 | 45 |
| TOTAL | tocadas | 3276 | 98.35c | 98.72% | +0.37 pts | -0.01 a +0.75 | 43 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.2c -> pago 0.0 | deportes_previo | tocada | FC UTA Arad vs. Universitatea Craiova CS: O/U 7.5
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.9c -> pago 0.0 | deportes_previo | tocada | Dundee FC vs. Heart of Midlothian FC: O/U 7.5
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $56,000 on November 20?

## Veredicto

Aun no hay veredicto: van 103 operaciones cerradas en 11.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
