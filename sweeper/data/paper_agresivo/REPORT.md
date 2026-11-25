# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 11.7 de 28 | corridas: 266
- Capital inicial: $1,000.00 | valor actual: $946.73 | P&L: $-53.27 (-5.33%)
- Efectivo libre: $0.00 | en ordenes abiertas: $549.33 (8) | en posiciones: $416.08 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 533 colocadas, 244 llenadas, 226 tocadas sin llenarse (sorteo 30%), 55 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 70 | 98.86c | 100.00% | 94.8-100.0% | +1.14 pts | $+54.28 | 0.18 |
| deportes_previo | 118 | 98.07c | 96.89% | 92.8-99.1% | -1.18 pts | $-113.37 | 0.26 |
| otros_cierre | 42 | 99.63c | 100.00% | 91.6-100.0% | +0.37 pts | $+10.90 | 0.33 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 238 | 98.53c | 98.35% | 96.4-99.6% | -0.18 pts | $-34.60 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.0c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $95.27 | 99.7c | 99.5c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 24, 2026? |
| $17.68 | 95.0c | 95.0c | deportes_previo |  | Spread: Giravanz Kitakyushu (-2.5) |
| $88.72 | 98.2c | 98.2c | deportes_previo |  | Spread: Tokushima Vortis (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 14098 | abiertas: 2048 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3811 | 98.81c | 98.87% | +0.07 pts | -0.27 a +0.40 | 43 |
| clima_cierre | tocadas | 3534 | 98.83c | 98.78% | -0.05 pts | -0.41 a +0.31 | 43 |
| cripto_cierre | todas | 1778 | 98.66c | 98.09% | -0.57 pts | -1.20 a +0.06 | 34 |
| cripto_cierre | tocadas | 1624 | 98.70c | 97.91% | -0.79 pts | -1.48 a -0.10 | 34 |
| deportes_previo | todas | 6646 | 98.05c | 97.37% | -0.68 pts | -1.06 a -0.30 | 177 |
| deportes_previo | tocadas | 6486 | 98.09c | 97.34% | -0.75 pts | -1.14 a -0.36 | 175 |
| otros_cierre | todas | 1610 | 99.00c | 97.58% | -1.42 pts | -2.16 a -0.67 | 39 |
| otros_cierre | tocadas | 1466 | 98.95c | 97.34% | -1.61 pts | -2.43 a -0.79 | 39 |
| post_fin_90_97 | todas | 253 | 94.03c | 93.68% | -0.35 pts | -3.32 a +2.62 | 16 |
| post_fin_90_97 | tocadas | 215 | 94.14c | 92.56% | -1.58 pts | -5.05 a +1.89 | 16 |
| TOTAL | todas | 14098 | 98.37c | 97.83% | -0.54 pts | -0.78 a -0.30 | 309 |
| TOTAL | tocadas | 13325 | 98.39c | 97.71% | -0.68 pts | -0.93 a -0.42 | 307 |

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

Aun no hay veredicto: van 238 operaciones cerradas en 11.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
