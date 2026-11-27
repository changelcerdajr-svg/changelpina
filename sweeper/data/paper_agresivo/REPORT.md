# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.6 de 28 | corridas: 315
- Capital inicial: $1,000.00 | valor actual: $992.69 | P&L: $-7.31 (-0.73%)
- Efectivo libre: $0.00 | en ordenes abiertas: $488.65 (7) | en posiciones: $529.46 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 633 colocadas, 287 llenadas, 270 tocadas sin llenarse (sorteo 30%), 69 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 79 | 98.81c | 100.00% | 95.4-100.0% | +1.19 pts | $+65.33 | 0.17 |
| deportes_previo | 145 | 98.08c | 97.47% | 94.1-99.3% | -0.61 pts | $-73.08 | 0.25 |
| otros_cierre | 46 | 99.61c | 100.00% | 92.3-100.0% | +0.39 pts | $+12.27 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 278 | 98.50c | 98.59% | 96.9-99.6% | +0.10 pts | $+18.11 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 84.4c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $19.30 | 95.9c | 99.4c | post_fin_90_97 |  | Will the highest temperature in Dallas be between 56-57°F on November 26? |
| $99.67 | 97.3c | 87.8c | deportes_previo |  | Spread: CF Cruz Azul (-3.5) |
| $14.19 | 99.9c | 100.0c | deportes_previo |  | Games Total: O/U 2.5 |
| $12.22 | 96.0c | 94.5c | deportes_previo |  | Spread: Gonzaga Bulldogs (-20.5) |
| $99.87 | 96.0c | 96.0c | deportes_previo |  | Spread: Baylor Bears (-14.5) |
| $69.81 | 99.5c | 99.5c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 26, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16376 | abiertas: 2446 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4550 | 98.80c | 98.95% | +0.15 pts | -0.15 a +0.44 | 48 |
| clima_cierre | tocadas | 4236 | 98.82c | 98.87% | +0.05 pts | -0.27 a +0.36 | 48 |
| cripto_cierre | todas | 2093 | 98.61c | 98.09% | -0.52 pts | -1.11 a +0.06 | 40 |
| cripto_cierre | tocadas | 1906 | 98.66c | 97.90% | -0.76 pts | -1.40 a -0.13 | 40 |
| deportes_previo | todas | 7732 | 98.05c | 97.43% | -0.61 pts | -0.96 a -0.26 | 203 |
| deportes_previo | tocadas | 7522 | 98.09c | 97.39% | -0.70 pts | -1.06 a -0.35 | 201 |
| otros_cierre | todas | 1727 | 98.99c | 97.57% | -1.43 pts | -2.15 a -0.70 | 42 |
| otros_cierre | tocadas | 1575 | 98.95c | 97.33% | -1.61 pts | -2.40 a -0.82 | 42 |
| post_fin_90_97 | todas | 274 | 94.03c | 93.80% | -0.23 pts | -3.06 a +2.60 | 17 |
| post_fin_90_97 | tocadas | 232 | 94.14c | 92.67% | -1.47 pts | -4.78 a +1.85 | 17 |
| TOTAL | todas | 16376 | 98.36c | 97.89% | -0.47 pts | -0.69 a -0.25 | 350 |
| TOTAL | tocadas | 15471 | 98.39c | 97.78% | -0.61 pts | -0.84 a -0.38 | 348 |

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

Aun no hay veredicto: van 278 operaciones cerradas en 13.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
