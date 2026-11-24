# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 12.3 de 28 | corridas: 276
- Capital inicial: $1,000.00 | valor actual: $1,030.05 | P&L: $+30.05 (+3.00%)
- Efectivo libre: $362.50 | en ordenes abiertas: $461.03 (9) | en posiciones: $206.18 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 465 colocadas, 112 llenadas, 240 tocadas sin llenarse (sorteo 30%), 104 expiradas

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
| $51.48 | 98.5c | 99.6c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 23, 2026? |
| $51.48 | 97.4c | 97.2c | deportes_previo |  | Newcastle United Jets vs. Kashiwa Reysol: O/U 0.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4418 | abiertas: 391 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1234 | 98.72c | 99.19% | +0.47 pts | -0.03 a +0.97 | 10 |
| cripto_cierre | tocadas | 853 | 98.55c | 98.83% | +0.28 pts | -0.45 a +1.00 | 10 |
| deportes_previo | todas | 2484 | 98.30c | 98.87% | +0.57 pts | +0.16 a +0.98 | 29 |
| deportes_previo | tocadas | 2112 | 98.28c | 98.86% | +0.58 pts | +0.14 a +1.03 | 25 |
| otros_cierre | todas | 611 | 98.83c | 99.35% | +0.51 pts | -0.13 a +1.15 | 4 |
| otros_cierre | tocadas | 398 | 98.71c | 98.99% | +0.28 pts | -0.70 a +1.27 | 4 |
| post_fin_95_97 | todas | 89 | 95.88c | 93.26% | -2.62 pts | -7.86 a +2.62 | 6 |
| post_fin_95_97 | tocadas | 80 | 95.90c | 92.50% | -3.40 pts | -9.21 a +2.41 | 6 |
| TOTAL | todas | 4418 | 98.44c | 98.91% | +0.47 pts | +0.17 a +0.77 | 49 |
| TOTAL | tocadas | 3443 | 98.34c | 98.72% | +0.38 pts | +0.01 a +0.75 | 45 |

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

Aun no hay veredicto: van 108 operaciones cerradas en 12.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
