# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 13.8 de 28 | corridas: 314
- Capital inicial: $1,000.00 | valor actual: $1,040.50 | P&L: $+40.50 (+4.05%)
- Efectivo libre: $417.86 | en ordenes abiertas: $519.17 (10) | en posiciones: $103.68 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 541 colocadas, 123 llenadas, 289 tocadas sin llenarse (sorteo 30%), 119 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 38 | 98.96c | 100.00% | 90.8-100.0% | +1.04 pts | $+20.03 | 0.28 |
| deportes_previo | 43 | 98.18c | 100.00% | 91.8-100.0% | +1.82 pts | $+40.15 | 0.34 |
| otros_cierre | 30 | 99.07c | 100.00% | 88.6-100.0% | +0.93 pts | $+14.60 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 121 | 98.46c | 99.12% | 95.5-99.9% | +0.67 pts | $+40.71 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.86 | 98.7c | 98.5c | cripto_cierre |  | Will the price of Bitcoin be less than $54,000 on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4989 | abiertas: 451 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1403 | 98.72c | 99.29% | +0.57 pts | +0.13 a +1.01 | 10 |
| cripto_cierre | tocadas | 988 | 98.56c | 98.99% | +0.43 pts | -0.19 a +1.06 | 10 |
| deportes_previo | todas | 2768 | 98.30c | 98.72% | +0.41 pts | -0.00 a +0.83 | 37 |
| deportes_previo | tocadas | 2308 | 98.28c | 98.72% | +0.45 pts | -0.01 a +0.90 | 31 |
| otros_cierre | todas | 726 | 98.89c | 99.45% | +0.56 pts | +0.02 a +1.10 | 4 |
| otros_cierre | tocadas | 454 | 98.72c | 99.12% | +0.40 pts | -0.47 a +1.26 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 4989 | 98.46c | 98.89% | +0.43 pts | +0.14 a +0.71 | 57 |
| TOTAL | tocadas | 3833 | 98.35c | 98.71% | +0.36 pts | +0.00 a +0.71 | 51 |

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

Aun no hay veredicto: van 121 operaciones cerradas en 13.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
