# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 12.9 de 28 | corridas: 291
- Capital inicial: $1,000.00 | valor actual: $1,034.63 | P&L: $+34.63 (+3.46%)
- Efectivo libre: $414.16 | en ordenes abiertas: $465.26 (9) | en posiciones: $155.22 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 494 colocadas, 116 llenadas, 259 tocadas sin llenarse (sorteo 30%), 110 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 36 | 99.00c | 100.00% | 90.4-100.0% | +1.00 pts | $+18.23 | 0.29 |
| deportes_previo | 39 | 98.19c | 100.00% | 91.0-100.0% | +1.81 pts | $+36.19 | 0.35 |
| otros_cierre | 28 | 99.02c | 100.00% | 87.9-100.0% | +0.98 pts | $+14.29 | 0.40 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 113 | 98.45c | 99.06% | 95.2-99.8% | +0.61 pts | $+34.63 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.70 | 98.3c | 98.5c | deportes_previo |  | Stevenage FC vs. Sheffield Wednesday FC: O/U 6.5 |
| $51.71 | 97.7c | 97.7c | deportes_previo |  | Spread: Northampton Town FC (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4581 | abiertas: 489 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1338 | 98.73c | 99.25% | +0.52 pts | +0.06 a +0.98 | 10 |
| cripto_cierre | tocadas | 938 | 98.57c | 98.93% | +0.36 pts | -0.29 a +1.02 | 10 |
| deportes_previo | todas | 2513 | 98.30c | 98.89% | +0.59 pts | +0.18 a +0.99 | 29 |
| deportes_previo | tocadas | 2133 | 98.28c | 98.87% | +0.60 pts | +0.15 a +1.04 | 25 |
| otros_cierre | todas | 638 | 98.84c | 99.37% | +0.54 pts | -0.08 a +1.15 | 4 |
| otros_cierre | tocadas | 414 | 98.71c | 99.03% | +0.33 pts | -0.62 a +1.28 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 4581 | 98.45c | 98.95% | +0.50 pts | +0.21 a +0.79 | 49 |
| TOTAL | tocadas | 3568 | 98.35c | 98.77% | +0.42 pts | +0.06 a +0.78 | 45 |

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

Aun no hay veredicto: van 113 operaciones cerradas en 12.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
