# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 12.1 de 28 | corridas: 270
- Capital inicial: $1,000.00 | valor actual: $1,029.60 | P&L: $+29.60 (+2.96%)
- Efectivo libre: $362.87 | en ordenes abiertas: $563.61 (11) | en posiciones: $103.22 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 462 colocadas, 110 llenadas, 238 tocadas sin llenarse (sorteo 30%), 103 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 34 | 98.97c | 100.00% | 89.8-100.0% | +1.03 pts | $+17.60 | 0.29 |
| deportes_previo | 38 | 98.21c | 100.00% | 90.8-100.0% | +1.79 pts | $+34.81 | 0.35 |
| otros_cierre | 27 | 99.04c | 100.00% | 87.5-100.0% | +0.96 pts | $+13.50 | 0.40 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 108 | 98.47c | 99.02% | 94.9-99.8% | +0.55 pts | $+29.71 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.40 | 96.0c | 96.0c | post_fin_95_97 |  | Will the highest temperature in Austin be between 56-57°F on November 23? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4345 | abiertas: 344 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1216 | 98.72c | 99.18% | +0.45 pts | -0.05 a +0.96 | 10 |
| cripto_cierre | tocadas | 843 | 98.55c | 98.81% | +0.26 pts | -0.47 a +0.99 | 10 |
| deportes_previo | todas | 2434 | 98.31c | 98.97% | +0.67 pts | +0.27 a +1.06 | 26 |
| deportes_previo | tocadas | 2072 | 98.28c | 98.94% | +0.65 pts | +0.22 a +1.09 | 23 |
| otros_cierre | todas | 606 | 98.83c | 99.34% | +0.51 pts | -0.14 a +1.16 | 4 |
| otros_cierre | tocadas | 395 | 98.71c | 98.99% | +0.28 pts | -0.71 a +1.27 | 4 |
| post_fin_95_97 | todas | 89 | 95.88c | 93.26% | -2.62 pts | -7.86 a +2.62 | 6 |
| post_fin_95_97 | tocadas | 80 | 95.90c | 92.50% | -3.40 pts | -9.21 a +2.41 | 6 |
| TOTAL | todas | 4345 | 98.45c | 98.96% | +0.52 pts | +0.22 a +0.82 | 46 |
| TOTAL | tocadas | 3390 | 98.34c | 98.76% | +0.42 pts | +0.05 a +0.79 | 43 |

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

Aun no hay veredicto: van 108 operaciones cerradas en 12.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
