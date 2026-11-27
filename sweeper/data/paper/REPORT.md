# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 15.2 de 28 | corridas: 351
- Capital inicial: $1,000.00 | valor actual: $1,045.99 | P&L: $+45.99 (+4.60%)
- Efectivo libre: $422.08 | en ordenes abiertas: $418.50 (8) | en posiciones: $209.04 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 601 colocadas, 134 llenadas, 325 tocadas sin llenarse (sorteo 30%), 134 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 41 | 98.97c | 100.00% | 91.4-100.0% | +1.03 pts | $+21.56 | 0.28 |
| deportes_previo | 48 | 98.13c | 100.00% | 92.6-100.0% | +1.87 pts | $+46.25 | 0.33 |
| otros_cierre | 31 | 99.02c | 100.00% | 89.0-100.0% | +0.98 pts | $+15.88 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 130 | 98.44c | 99.19% | 95.8-99.9% | +0.75 pts | $+49.62 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.35 | 97.4c | 90.7c | deportes_previo |  | Spread: TCU (-13.5) |
| $52.40 | 97.0c | 97.0c | deportes_previo |  | Spread: CF Cruz Azul (-3.5) |
| $52.48 | 99.0c | 99.2c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 26, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5546 | abiertas: 324 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1567 | 98.72c | 99.30% | +0.58 pts | +0.16 a +0.99 | 11 |
| cripto_cierre | tocadas | 1089 | 98.55c | 98.99% | +0.44 pts | -0.16 a +1.03 | 11 |
| deportes_previo | todas | 3128 | 98.31c | 98.71% | +0.40 pts | +0.00 a +0.79 | 42 |
| deportes_previo | tocadas | 2570 | 98.28c | 98.66% | +0.38 pts | -0.06 a +0.82 | 36 |
| otros_cierre | todas | 752 | 98.87c | 99.34% | +0.46 pts | -0.12 a +1.05 | 5 |
| otros_cierre | tocadas | 476 | 98.70c | 98.95% | +0.25 pts | -0.67 a +1.17 | 5 |
| post_fin_95_97 | todas | 99 | 95.90c | 93.94% | -1.96 pts | -6.69 a +2.77 | 6 |
| post_fin_95_97 | tocadas | 87 | 95.92c | 93.10% | -2.81 pts | -8.17 a +2.54 | 6 |
| TOTAL | todas | 5546 | 98.46c | 98.87% | +0.41 pts | +0.14 a +0.69 | 64 |
| TOTAL | tocadas | 4222 | 98.35c | 98.66% | +0.31 pts | -0.03 a +0.66 | 58 |

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

Aun no hay veredicto: van 130 operaciones cerradas en 15.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
