# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 13.3 de 28 | corridas: 302
- Capital inicial: $1,000.00 | valor actual: $1,036.64 | P&L: $+36.64 (+3.66%)
- Efectivo libre: $415.09 | en ordenes abiertas: $466.17 (9) | en posiciones: $155.48 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 511 colocadas, 118 llenadas, 270 tocadas sin llenarse (sorteo 30%), 114 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 36 | 99.00c | 100.00% | 90.4-100.0% | +1.00 pts | $+18.23 | 0.29 |
| deportes_previo | 41 | 98.18c | 100.00% | 91.4-100.0% | +1.82 pts | $+38.30 | 0.35 |
| otros_cierre | 28 | 99.02c | 100.00% | 87.9-100.0% | +0.98 pts | $+14.29 | 0.40 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 115 | 98.44c | 99.08% | 95.2-99.8% | +0.63 pts | $+36.75 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.83 | 99.6c | 99.6c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 24, 2026? |
| $51.83 | 99.4c | 99.4c | cripto_cierre |  | Will Ethereum reach $1,800 on November 24? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4839 | abiertas: 354 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1353 | 98.73c | 99.26% | +0.53 pts | +0.07 a +0.98 | 10 |
| cripto_cierre | tocadas | 942 | 98.57c | 98.94% | +0.37 pts | -0.28 a +1.03 | 10 |
| deportes_previo | todas | 2717 | 98.31c | 98.75% | +0.44 pts | +0.03 a +0.86 | 35 |
| deportes_previo | tocadas | 2274 | 98.28c | 98.77% | +0.49 pts | +0.04 a +0.94 | 29 |
| otros_cierre | todas | 677 | 98.88c | 99.41% | +0.53 pts | -0.05 a +1.11 | 4 |
| otros_cierre | tocadas | 428 | 98.73c | 99.07% | +0.34 pts | -0.58 a +1.26 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 4839 | 98.46c | 98.88% | +0.42 pts | +0.13 a +0.72 | 55 |
| TOTAL | tocadas | 3727 | 98.35c | 98.71% | +0.36 pts | +0.00 a +0.72 | 49 |

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

Aun no hay veredicto: van 115 operaciones cerradas en 13.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
