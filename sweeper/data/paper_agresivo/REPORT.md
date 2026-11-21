# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.7 de 28 | corridas: 158
- Capital inicial: $1,000.00 | valor actual: $939.83 | P&L: $-60.17 (-6.02%)
- Efectivo libre: $0.00 | en ordenes abiertas: $548.29 (8) | en posiciones: $397.47 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 340 colocadas, 148 llenadas, 147 tocadas sin llenarse (sorteo 30%), 37 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 46 | 98.81c | 100.00% | 92.3-100.0% | +1.19 pts | $+36.63 | 0.15 |
| deportes_previo | 62 | 98.14c | 95.90% | 89.0-99.1% | -2.24 pts | $-109.31 | 0.31 |
| otros_cierre | 30 | 99.67c | 100.00% | 88.6-100.0% | +0.33 pts | $+6.86 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 143 | 98.62c | 98.12% | 95.0-99.6% | -0.50 pts | $-54.24 | 0.29 |

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
| $89.17 | 99.8c | 99.1c | otros_cierre |  | Manchester City punishment announced by November 20? |
| $93.89 | 96.2c | 96.2c | deportes_previo |  | Spread: Fagiano Okayama (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 7820 | abiertas: 2692 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2251 | 98.85c | 99.02% | +0.17 pts | -0.23 a +0.58 | 22 |
| clima_cierre | tocadas | 2077 | 98.87c | 98.94% | +0.07 pts | -0.37 a +0.51 | 22 |
| cripto_cierre | todas | 1152 | 98.71c | 98.00% | -0.71 pts | -1.51 a +0.09 | 23 |
| cripto_cierre | tocadas | 1054 | 98.76c | 97.82% | -0.94 pts | -1.81 a -0.07 | 23 |
| deportes_previo | todas | 3251 | 98.05c | 97.46% | -0.59 pts | -1.12 a -0.06 | 85 |
| deportes_previo | tocadas | 3178 | 98.08c | 97.40% | -0.68 pts | -1.22 a -0.13 | 85 |
| otros_cierre | todas | 1089 | 98.99c | 97.06% | -1.92 pts | -2.92 a -0.93 | 32 |
| otros_cierre | tocadas | 1017 | 98.94c | 96.85% | -2.09 pts | -3.15 a -1.02 | 32 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 7820 | 98.47c | 97.93% | -0.54 pts | -0.85 a -0.23 | 164 |
| TOTAL | tocadas | 7387 | 98.49c | 97.81% | -0.68 pts | -1.00 a -0.35 | 164 |

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

Aun no hay veredicto: van 143 operaciones cerradas en 7.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
