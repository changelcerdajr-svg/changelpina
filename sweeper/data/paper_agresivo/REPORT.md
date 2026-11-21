# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.6 de 28 | corridas: 156
- Capital inicial: $1,000.00 | valor actual: $892.83 | P&L: $-107.17 (-10.72%)
- Efectivo libre: $0.00 | en ordenes abiertas: $525.54 (7) | en posiciones: $419.20 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 330 colocadas, 146 llenadas, 140 tocadas sin llenarse (sorteo 30%), 37 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 44 | 98.81c | 100.00% | 92.0-100.0% | +1.19 pts | $+35.79 | 0.15 |
| deportes_previo | 61 | 98.10c | 95.81% | 88.8-99.1% | -2.29 pts | $-109.49 | 0.32 |
| otros_cierre | 30 | 99.67c | 100.00% | 88.6-100.0% | +0.33 pts | $+6.86 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 140 | 98.60c | 98.09% | 94.9-99.6% | -0.52 pts | $-55.26 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.9c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.14 | 99.8c | 50.0c | deportes_previo |  | Spread: Clemson (-17.5) |
| $89.17 | 99.8c | 99.1c | otros_cierre |  | Manchester City punishment announced by November 20? |
| $23.49 | 99.7c | 99.7c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 20? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 7655 | abiertas: 2782 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2238 | 98.85c | 99.02% | +0.16 pts | -0.24 a +0.57 | 22 |
| clima_cierre | tocadas | 2064 | 98.87c | 98.93% | +0.06 pts | -0.38 a +0.50 | 22 |
| cripto_cierre | todas | 1128 | 98.70c | 98.23% | -0.47 pts | -1.23 a +0.29 | 20 |
| cripto_cierre | tocadas | 1031 | 98.74c | 98.06% | -0.68 pts | -1.51 a +0.15 | 20 |
| deportes_previo | todas | 3132 | 98.06c | 97.43% | -0.63 pts | -1.18 a -0.08 | 83 |
| deportes_previo | tocadas | 3061 | 98.09c | 97.37% | -0.72 pts | -1.28 a -0.16 | 83 |
| otros_cierre | todas | 1080 | 98.98c | 97.04% | -1.94 pts | -2.95 a -0.94 | 32 |
| otros_cierre | tocadas | 1008 | 98.94c | 96.83% | -2.11 pts | -3.19 a -1.04 | 32 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 7655 | 98.48c | 97.96% | -0.52 pts | -0.84 a -0.21 | 159 |
| TOTAL | tocadas | 7225 | 98.49c | 97.83% | -0.66 pts | -0.99 a -0.33 | 159 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) finish week of November 16 above $270?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Amazon (AMZN) close at $245-$250 on the final day of trading of the week of Nov 16 – 

## Veredicto

Aun no hay veredicto: van 140 operaciones cerradas en 7.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
