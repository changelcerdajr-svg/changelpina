# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 14.3 de 28 | corridas: 334
- Capital inicial: $1,000.00 | valor actual: $924.35 | P&L: $-75.65 (-7.57%)
- Efectivo libre: $0.00 | en ordenes abiertas: $548.64 (8) | en posiciones: $391.17 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 670 colocadas, 305 llenadas, 281 tocadas sin llenarse (sorteo 30%), 76 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 84 | 98.84c | 100.00% | 95.6-100.0% | +1.16 pts | $+66.77 | 0.17 |
| deportes_previo | 158 | 98.03c | 96.80% | 93.7-99.0% | -1.23 pts | $-154.42 | 0.25 |
| otros_cierre | 49 | 99.62c | 100.00% | 92.7-100.0% | +0.38 pts | $+13.04 | 0.31 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 300 | 98.48c | 98.22% | 96.6-99.5% | -0.26 pts | $-60.19 | 0.25 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-99.67 | 97.3c | 0.0 | deportes_previo | Spread: CF Cruz Azul (-3.5) |
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 87.8c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $91.65 | 97.9c | 96.9c | deportes_previo |  | Spread: Borussia Mönchengladbach (-2.5) |
| $85.12 | 99.8c | 97.9c | deportes_previo |  | Spread: Borussia Mönchengladbach (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 17261 | abiertas: 2728 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4783 | 98.80c | 98.98% | +0.17 pts | -0.11 a +0.46 | 49 |
| clima_cierre | tocadas | 4455 | 98.83c | 98.90% | +0.07 pts | -0.23 a +0.38 | 49 |
| cripto_cierre | todas | 2237 | 98.59c | 98.17% | -0.42 pts | -0.97 a +0.13 | 41 |
| cripto_cierre | tocadas | 2034 | 98.65c | 97.98% | -0.66 pts | -1.27 a -0.06 | 41 |
| deportes_previo | todas | 7994 | 98.05c | 97.42% | -0.63 pts | -0.98 a -0.29 | 211 |
| deportes_previo | tocadas | 7781 | 98.09c | 97.37% | -0.72 pts | -1.07 a -0.37 | 209 |
| otros_cierre | todas | 1957 | 98.92c | 97.70% | -1.22 pts | -1.88 a -0.56 | 45 |
| otros_cierre | tocadas | 1803 | 98.88c | 97.50% | -1.37 pts | -2.09 a -0.66 | 45 |
| post_fin_90_97 | todas | 290 | 94.03c | 93.79% | -0.24 pts | -2.99 a +2.51 | 18 |
| post_fin_90_97 | tocadas | 245 | 94.13c | 92.65% | -1.48 pts | -4.71 a +1.75 | 18 |
| TOTAL | todas | 17261 | 98.36c | 97.92% | -0.44 pts | -0.65 a -0.23 | 364 |
| TOTAL | tocadas | 16318 | 98.39c | 97.81% | -0.58 pts | -0.80 a -0.36 | 362 |

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

Aun no hay veredicto: van 300 operaciones cerradas en 14.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
