# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 11.5 de 28 | corridas: 254
- Capital inicial: $1,000.00 | valor actual: $1,025.16 | P&L: $+25.16 (+2.52%)
- Efectivo libre: $410.30 | en ordenes abiertas: $466.10 (11) | en posiciones: $148.66 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 432 colocadas, 101 llenadas, 225 tocadas sin llenarse (sorteo 30%), 95 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 29 | 98.91c | 100.00% | 88.3-100.0% | +1.09 pts | $+16.45 | 0.31 |
| deportes_previo | 36 | 98.23c | 100.00% | 90.4-100.0% | +1.77 pts | $+32.61 | 0.34 |
| otros_cierre | 24 | 99.02c | 100.00% | 86.2-100.0% | +0.98 pts | $+12.21 | 0.44 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 98 | 98.42c | 98.93% | 94.4-99.8% | +0.51 pts | $+25.06 | 0.36 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.12 | 98.7c | 98.8c | deportes_previo |  | Alcorn State Braves vs. Michigan State Spartans (W) |
| $45.72 | 99.7c | 99.9c | cripto_cierre |  | Will the price of Ethereum be above $1,500 on November 23? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4067 | abiertas: 368 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1145 | 98.72c | 99.13% | +0.40 pts | -0.14 a +0.94 | 10 |
| cripto_cierre | tocadas | 792 | 98.55c | 98.74% | +0.19 pts | -0.59 a +0.97 | 10 |
| deportes_previo | todas | 2291 | 98.30c | 98.95% | +0.65 pts | +0.24 a +1.06 | 25 |
| deportes_previo | tocadas | 1952 | 98.28c | 98.87% | +0.60 pts | +0.13 a +1.06 | 23 |
| otros_cierre | todas | 554 | 98.81c | 99.28% | +0.47 pts | -0.24 a +1.18 | 4 |
| otros_cierre | tocadas | 369 | 98.70c | 98.92% | +0.22 pts | -0.84 a +1.28 | 4 |
| post_fin_95_97 | todas | 77 | 95.92c | 92.21% | -3.71 pts | -9.73 a +2.32 | 6 |
| post_fin_95_97 | tocadas | 69 | 95.93c | 91.30% | -4.63 pts | -11.32 a +2.07 | 6 |
| TOTAL | todas | 4067 | 98.45c | 98.92% | +0.47 pts | +0.16 a +0.79 | 45 |
| TOTAL | tocadas | 3182 | 98.34c | 98.68% | +0.34 pts | -0.06 a +0.73 | 43 |

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

Aun no hay veredicto: van 98 operaciones cerradas en 11.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
