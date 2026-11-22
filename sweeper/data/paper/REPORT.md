# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 11.0 de 28 | corridas: 240
- Capital inicial: $1,000.00 | valor actual: $1,022.46 | P&L: $+22.46 (+2.25%)
- Efectivo libre: $411.57 | en ordenes abiertas: $403.39 (10) | en posiciones: $207.12 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 406 colocadas, 98 llenadas, 209 tocadas sin llenarse (sorteo 30%), 89 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 26 | 98.90c | 100.00% | 87.1-100.0% | +1.10 pts | $+15.05 | 0.28 |
| deportes_previo | 34 | 98.26c | 100.00% | 89.8-100.0% | +1.74 pts | $+31.04 | 0.34 |
| otros_cierre | 24 | 99.02c | 100.00% | 86.2-100.0% | +0.98 pts | $+12.21 | 0.44 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 93 | 98.41c | 98.88% | 94.2-99.8% | +0.47 pts | $+22.08 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.06 | 97.2c | 97.7c | deportes_previo |  | Spread: Real Valladolid CF (-3.5) |
| $7.32 | 98.6c | 98.7c | deportes_previo |  | Spread: CF Cruz Azul (-3.5) |
| $53.71 | 99.0c | 99.5c | cripto_cierre |  | Will Bitcoin reach $66,000 November 16-22? |
| $43.20 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3773 | abiertas: 457 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1064 | 98.73c | 99.06% | +0.33 pts | -0.25 a +0.91 | 10 |
| cripto_cierre | tocadas | 728 | 98.56c | 98.63% | +0.07 pts | -0.77 a +0.92 | 10 |
| deportes_previo | todas | 2100 | 98.31c | 98.95% | +0.65 pts | +0.21 a +1.08 | 23 |
| deportes_previo | tocadas | 1791 | 98.28c | 98.88% | +0.61 pts | +0.13 a +1.09 | 21 |
| otros_cierre | todas | 537 | 98.81c | 99.26% | +0.45 pts | -0.28 a +1.18 | 4 |
| otros_cierre | tocadas | 361 | 98.70c | 98.89% | +0.20 pts | -0.89 a +1.28 | 4 |
| post_fin_95_97 | todas | 72 | 95.91c | 91.67% | -4.25 pts | -10.68 a +2.18 | 6 |
| post_fin_95_97 | tocadas | 64 | 95.93c | 90.62% | -5.30 pts | -12.50 a +1.89 | 6 |
| TOTAL | todas | 3773 | 98.45c | 98.89% | +0.43 pts | +0.10 a +0.77 | 43 |
| TOTAL | tocadas | 2944 | 98.35c | 98.64% | +0.29 pts | -0.12 a +0.71 | 41 |

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

Aun no hay veredicto: van 93 operaciones cerradas en 11.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
