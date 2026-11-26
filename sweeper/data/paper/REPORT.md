# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 14.7 de 28 | corridas: 337
- Capital inicial: $1,000.00 | valor actual: $1,047.47 | P&L: $+47.47 (+4.75%)
- Efectivo libre: $419.65 | en ordenes abiertas: $523.74 (10) | en posiciones: $104.19 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 580 colocadas, 130 llenadas, 312 tocadas sin llenarse (sorteo 30%), 128 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 41 | 98.97c | 100.00% | 91.4-100.0% | +1.03 pts | $+21.56 | 0.28 |
| deportes_previo | 46 | 98.14c | 100.00% | 92.3-100.0% | +1.86 pts | $+44.21 | 0.33 |
| otros_cierre | 31 | 99.02c | 100.00% | 89.0-100.0% | +0.98 pts | $+15.88 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 128 | 98.44c | 99.17% | 95.7-99.9% | +0.73 pts | $+47.58 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.37 | 99.2c | 99.2c | deportes_previo |  | Spread: K. Sint-Truidense VV (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5298 | abiertas: 370 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1505 | 98.72c | 99.27% | +0.55 pts | +0.12 a +0.98 | 11 |
| cripto_cierre | tocadas | 1056 | 98.55c | 98.96% | +0.40 pts | -0.21 a +1.02 | 11 |
| deportes_previo | todas | 2953 | 98.31c | 98.80% | +0.49 pts | +0.10 a +0.88 | 37 |
| deportes_previo | tocadas | 2439 | 98.28c | 98.79% | +0.51 pts | +0.09 a +0.94 | 31 |
| otros_cierre | todas | 746 | 98.87c | 99.33% | +0.45 pts | -0.13 a +1.04 | 5 |
| otros_cierre | tocadas | 472 | 98.71c | 98.94% | +0.24 pts | -0.69 a +1.16 | 5 |
| post_fin_95_97 | todas | 94 | 95.90c | 93.62% | -2.28 pts | -7.25 a +2.69 | 6 |
| post_fin_95_97 | tocadas | 85 | 95.92c | 92.94% | -2.98 pts | -8.46 a +2.50 | 6 |
| TOTAL | todas | 5298 | 98.46c | 98.91% | +0.45 pts | +0.18 a +0.73 | 59 |
| TOTAL | tocadas | 4052 | 98.35c | 98.73% | +0.38 pts | +0.04 a +0.72 | 53 |

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

Aun no hay veredicto: van 128 operaciones cerradas en 14.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
