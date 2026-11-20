# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.4 de 28 | corridas: 149
- Capital inicial: $1,000.00 | valor actual: $919.90 | P&L: $-80.10 (-8.01%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $436.21 (5) | en posiciones: $499.49 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 310 colocadas, 137 llenadas, 132 tocadas sin llenarse (sorteo 30%), 36 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 39 | 98.82c | 100.00% | 91.0-100.0% | +1.18 pts | $+31.97 | 0.16 |
| deportes_previo | 56 | 98.02c | 95.35% | 87.9-99.0% | -2.67 pts | $-114.72 | 0.33 |
| otros_cierre | 30 | 99.67c | 100.00% | 88.6-100.0% | +0.33 pts | $+6.86 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 130 | 98.59c | 97.93% | 94.6-99.6% | -0.65 pts | $-64.30 | 0.30 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.27 | 98.9c | 98.4c | deportes_previo |  | Alcorn State Braves vs. Tulane Green Wave (W) |
| $91.13 | 97.9c | 87.2c | deportes_previo |  | Spread: Real Murcia CF (-2.5) |
| $14.22 | 98.9c | 98.8c | cripto_cierre |  | Silver (XAGUSD) Up or Down on November 20? |
| $87.47 | 98.9c | 98.9c | cripto_cierre |  | Gold (XAUUSD) Up or Down on November 20? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 7243 | abiertas: 2845 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2129 | 98.87c | 99.11% | +0.24 pts | -0.16 a +0.64 | 19 |
| clima_cierre | tocadas | 1960 | 98.89c | 99.03% | +0.14 pts | -0.29 a +0.57 | 19 |
| cripto_cierre | todas | 1119 | 98.71c | 98.21% | -0.50 pts | -1.27 a +0.27 | 20 |
| cripto_cierre | tocadas | 1028 | 98.75c | 98.05% | -0.69 pts | -1.53 a +0.14 | 20 |
| deportes_previo | todas | 2905 | 98.08c | 97.37% | -0.71 pts | -1.28 a -0.13 | 79 |
| deportes_previo | tocadas | 2840 | 98.10c | 97.31% | -0.80 pts | -1.38 a -0.21 | 79 |
| otros_cierre | todas | 1013 | 99.00c | 96.84% | -2.16 pts | -3.23 a -1.10 | 32 |
| otros_cierre | tocadas | 948 | 98.97c | 96.62% | -2.34 pts | -3.48 a -1.20 | 32 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 7243 | 98.50c | 97.94% | -0.56 pts | -0.88 a -0.24 | 152 |
| TOTAL | tocadas | 6837 | 98.51c | 97.81% | -0.70 pts | -1.04 a -0.36 | 152 |

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

Aun no hay veredicto: van 130 operaciones cerradas en 7.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
