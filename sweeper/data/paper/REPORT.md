# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 13.5 de 28 | corridas: 306
- Capital inicial: $1,000.00 | valor actual: $1,037.16 | P&L: $+37.16 (+3.72%)
- Efectivo libre: $415.23 | en ordenes abiertas: $466.53 (9) | en posiciones: $155.51 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 517 colocadas, 120 llenadas, 271 tocadas sin llenarse (sorteo 30%), 117 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 37 | 99.01c | 100.00% | 90.6-100.0% | +0.99 pts | $+18.54 | 0.29 |
| deportes_previo | 41 | 98.18c | 100.00% | 91.4-100.0% | +1.82 pts | $+38.30 | 0.35 |
| otros_cierre | 29 | 99.04c | 100.00% | 88.3-100.0% | +0.96 pts | $+14.49 | 0.39 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 117 | 98.46c | 99.09% | 95.3-99.8% | +0.63 pts | $+37.27 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.83 | 97.7c | 97.7c | deportes_previo |  | RB Ōmiya Ardija vs. Tokushima Vortis: O/U 6.5 |
| $51.86 | 98.7c | 98.7c | cripto_cierre |  | Will the price of Bitcoin be less than $54,000 on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4932 | abiertas: 328 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1394 | 98.73c | 99.28% | +0.56 pts | +0.11 a +1.00 | 10 |
| cripto_cierre | tocadas | 980 | 98.56c | 98.98% | +0.42 pts | -0.21 a +1.05 | 10 |
| deportes_previo | todas | 2736 | 98.30c | 98.72% | +0.42 pts | -0.00 a +0.83 | 36 |
| deportes_previo | tocadas | 2288 | 98.28c | 98.73% | +0.45 pts | +0.00 a +0.91 | 30 |
| otros_cierre | todas | 710 | 98.89c | 99.44% | +0.55 pts | -0.00 a +1.11 | 4 |
| otros_cierre | tocadas | 445 | 98.72c | 99.10% | +0.38 pts | -0.50 a +1.26 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 4932 | 98.46c | 98.88% | +0.42 pts | +0.13 a +0.71 | 56 |
| TOTAL | tocadas | 3796 | 98.35c | 98.71% | +0.36 pts | +0.00 a +0.71 | 50 |

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

Aun no hay veredicto: van 117 operaciones cerradas en 13.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
