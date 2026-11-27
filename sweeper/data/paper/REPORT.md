# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 15.1 de 28 | corridas: 348
- Capital inicial: $1,000.00 | valor actual: $1,048.96 | P&L: $+48.96 (+4.90%)
- Efectivo libre: $421.01 | en ordenes abiertas: $523.99 (10) | en posiciones: $104.19 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 591 colocadas, 131 llenadas, 318 tocadas sin llenarse (sorteo 30%), 132 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 41 | 98.97c | 100.00% | 91.4-100.0% | +1.03 pts | $+21.56 | 0.28 |
| deportes_previo | 47 | 98.11c | 100.00% | 92.4-100.0% | +1.89 pts | $+45.83 | 0.33 |
| otros_cierre | 31 | 99.02c | 100.00% | 89.0-100.0% | +0.98 pts | $+15.88 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 129 | 98.43c | 99.18% | 95.7-99.9% | +0.75 pts | $+49.20 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.37 | 99.2c | 99.0c | deportes_previo |  | Spread: K. Sint-Truidense VV (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5515 | abiertas: 307 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1560 | 98.72c | 99.29% | +0.58 pts | +0.16 a +0.99 | 11 |
| cripto_cierre | tocadas | 1088 | 98.56c | 98.99% | +0.43 pts | -0.16 a +1.03 | 11 |
| deportes_previo | todas | 3104 | 98.31c | 98.70% | +0.39 pts | -0.01 a +0.78 | 42 |
| deportes_previo | tocadas | 2553 | 98.28c | 98.65% | +0.37 pts | -0.07 a +0.82 | 36 |
| otros_cierre | todas | 752 | 98.87c | 99.34% | +0.46 pts | -0.12 a +1.05 | 5 |
| otros_cierre | tocadas | 476 | 98.70c | 98.95% | +0.25 pts | -0.67 a +1.17 | 5 |
| post_fin_95_97 | todas | 99 | 95.90c | 93.94% | -1.96 pts | -6.69 a +2.77 | 6 |
| post_fin_95_97 | tocadas | 87 | 95.92c | 93.10% | -2.81 pts | -8.17 a +2.54 | 6 |
| TOTAL | todas | 5515 | 98.46c | 98.87% | +0.41 pts | +0.13 a +0.69 | 64 |
| TOTAL | tocadas | 4204 | 98.35c | 98.66% | +0.31 pts | -0.04 a +0.65 | 58 |

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

Aun no hay veredicto: van 129 operaciones cerradas en 15.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
