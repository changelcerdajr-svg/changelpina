# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 12.0 de 28 | corridas: 267
- Capital inicial: $1,000.00 | valor actual: $1,023.13 | P&L: $+23.13 (+2.31%)
- Efectivo libre: $362.49 | en ordenes abiertas: $408.53 (8) | en posiciones: $257.74 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 456 colocadas, 110 llenadas, 236 tocadas sin llenarse (sorteo 30%), 102 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 31 | 98.95c | 100.00% | 89.0-100.0% | +1.05 pts | $+16.90 | 0.31 |
| deportes_previo | 38 | 98.21c | 100.00% | 90.8-100.0% | +1.79 pts | $+34.81 | 0.35 |
| otros_cierre | 26 | 99.02c | 100.00% | 87.1-100.0% | +0.98 pts | $+13.24 | 0.41 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 104 | 98.44c | 98.99% | 94.8-99.8% | +0.55 pts | $+28.75 | 0.36 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.40 | 96.0c | 96.0c | post_fin_95_97 |  | Will the highest temperature in Austin be between 56-57°F on November 23? |
| $51.40 | 98.9c | 92.5c | cripto_cierre |  | Microsoft (MSFT) Up or Down on November 23? |
| $46.10 | 99.8c | 95.0c | cripto_cierre |  | NVIDIA (NVDA) Up or Down on November 23? |
| $5.61 | 99.4c | 99.4c | cripto_cierre |  | Meta (META) Up or Down on November 23? |
| $51.40 | 99.5c | 99.5c | otros_cierre |  | Will Google (GOOGL) close above $260 on November 23? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4228 | abiertas: 450 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1212 | 98.73c | 99.17% | +0.45 pts | -0.06 a +0.96 | 10 |
| cripto_cierre | tocadas | 839 | 98.56c | 98.81% | +0.25 pts | -0.48 a +0.98 | 10 |
| deportes_previo | todas | 2349 | 98.31c | 98.98% | +0.67 pts | +0.27 a +1.07 | 25 |
| deportes_previo | tocadas | 1998 | 98.29c | 98.90% | +0.61 pts | +0.16 a +1.07 | 23 |
| otros_cierre | todas | 581 | 98.82c | 99.31% | +0.49 pts | -0.19 a +1.17 | 4 |
| otros_cierre | tocadas | 378 | 98.70c | 98.94% | +0.24 pts | -0.79 a +1.28 | 4 |
| post_fin_95_97 | todas | 86 | 95.87c | 93.02% | -2.85 pts | -8.27 a +2.57 | 6 |
| post_fin_95_97 | tocadas | 77 | 95.90c | 92.21% | -3.69 pts | -9.72 a +2.34 | 6 |
| TOTAL | todas | 4228 | 98.45c | 98.96% | +0.51 pts | +0.21 a +0.81 | 45 |
| TOTAL | tocadas | 3292 | 98.35c | 98.72% | +0.38 pts | -0.00 a +0.76 | 43 |

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

Aun no hay veredicto: van 104 operaciones cerradas en 12.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
