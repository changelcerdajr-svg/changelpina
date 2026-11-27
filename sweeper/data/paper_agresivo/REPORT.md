# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.7 de 28 | corridas: 318
- Capital inicial: $1,000.00 | valor actual: $895.89 | P&L: $-104.11 (-10.41%)
- Efectivo libre: $0.00 | en ordenes abiertas: $394.59 (7) | en posiciones: $623.76 (10)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 637 colocadas, 290 llenadas, 270 tocadas sin llenarse (sorteo 30%), 70 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 80 | 98.82c | 100.00% | 95.4-100.0% | +1.18 pts | $+65.56 | 0.17 |
| deportes_previo | 146 | 98.09c | 97.47% | 94.1-99.3% | -0.61 pts | $-73.07 | 0.25 |
| otros_cierre | 46 | 99.61c | 100.00% | 92.3-100.0% | +0.39 pts | $+12.27 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 280 | 98.50c | 98.60% | 96.9-99.6% | +0.10 pts | $+18.35 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 81.5c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $19.30 | 95.9c | 99.4c | post_fin_90_97 |  | Will the highest temperature in Dallas be between 56-57°F on November 26? |
| $99.67 | 97.3c | 0.1c | deportes_previo |  | Spread: CF Cruz Azul (-3.5) |
| $12.22 | 96.0c | 95.5c | deportes_previo |  | Spread: Gonzaga Bulldogs (-20.5) |
| $99.87 | 96.0c | 91.5c | deportes_previo |  | Spread: Baylor Bears (-14.5) |
| $69.81 | 99.5c | 99.5c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 26, 2026? |
| $99.27 | 99.7c | 99.7c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 26, 2026? |
| $9.22 | 97.3c | 97.5c | deportes_previo |  | Spread: Melbourne City FC (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16480 | abiertas: 2577 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4567 | 98.80c | 98.93% | +0.13 pts | -0.17 a +0.43 | 49 |
| clima_cierre | tocadas | 4251 | 98.82c | 98.85% | +0.03 pts | -0.29 a +0.35 | 49 |
| cripto_cierre | todas | 2116 | 98.61c | 98.06% | -0.55 pts | -1.13 a +0.04 | 41 |
| cripto_cierre | tocadas | 1925 | 98.66c | 97.87% | -0.79 pts | -1.43 a -0.16 | 41 |
| deportes_previo | todas | 7792 | 98.05c | 97.38% | -0.67 pts | -1.02 a -0.32 | 209 |
| deportes_previo | tocadas | 7582 | 98.09c | 97.33% | -0.76 pts | -1.12 a -0.40 | 207 |
| otros_cierre | todas | 1727 | 98.99c | 97.57% | -1.43 pts | -2.15 a -0.70 | 42 |
| otros_cierre | tocadas | 1575 | 98.95c | 97.33% | -1.61 pts | -2.40 a -0.82 | 42 |
| post_fin_90_97 | todas | 278 | 94.00c | 93.88% | -0.11 pts | -2.90 a +2.68 | 17 |
| post_fin_90_97 | tocadas | 235 | 94.10c | 92.77% | -1.34 pts | -4.61 a +1.94 | 17 |
| TOTAL | todas | 16480 | 98.36c | 97.85% | -0.50 pts | -0.72 a -0.28 | 358 |
| TOTAL | tocadas | 15568 | 98.39c | 97.74% | -0.64 pts | -0.88 a -0.41 | 356 |

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

Aun no hay veredicto: van 280 operaciones cerradas en 13.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
