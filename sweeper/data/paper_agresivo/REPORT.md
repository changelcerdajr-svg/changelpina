# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 12.2 de 28 | corridas: 277
- Capital inicial: $1,000.00 | valor actual: $960.22 | P&L: $-39.78 (-3.98%)
- Efectivo libre: $0.00 | en ordenes abiertas: $468.42 (5) | en posiciones: $510.06 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 560 colocadas, 255 llenadas, 241 tocadas sin llenarse (sorteo 30%), 59 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 70 | 98.86c | 100.00% | 94.8-100.0% | +1.14 pts | $+54.28 | 0.18 |
| deportes_previo | 125 | 98.04c | 97.05% | 93.2-99.2% | -0.99 pts | $-100.76 | 0.25 |
| otros_cierre | 44 | 99.63c | 100.00% | 92.0-100.0% | +0.37 pts | $+11.37 | 0.33 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 247 | 98.51c | 98.41% | 96.5-99.6% | -0.11 pts | $-21.52 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.7c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $8.21 | 98.9c | 98.9c | deportes_previo |  | Navy Midshipmen vs. Iowa Hawkeyes (W) |
| $35.99 | 99.4c | 98.5c | cripto_cierre |  | Will the price of Bitcoin be less than $54,000 on November 25? |
| $95.63 | 99.9c | 99.9c | cripto_cierre |  | Will the price of Ethereum be above $1,300 on November 25? |
| $95.63 | 97.1c | 97.1c | cripto_cierre |  | Will the price of Bitcoin be between $54,000 and $56,000 on November 25? |
| $60.20 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Ethereum be above $1,400 on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 14559 | abiertas: 2200 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4009 | 98.80c | 98.85% | +0.06 pts | -0.27 a +0.38 | 46 |
| clima_cierre | tocadas | 3726 | 98.82c | 98.77% | -0.05 pts | -0.41 a +0.30 | 46 |
| cripto_cierre | todas | 1831 | 98.65c | 98.14% | -0.51 pts | -1.12 a +0.11 | 34 |
| cripto_cierre | tocadas | 1669 | 98.69c | 97.96% | -0.73 pts | -1.40 a -0.06 | 34 |
| deportes_previo | todas | 6819 | 98.04c | 97.35% | -0.69 pts | -1.07 a -0.31 | 185 |
| deportes_previo | tocadas | 6647 | 98.08c | 97.31% | -0.77 pts | -1.15 a -0.38 | 183 |
| otros_cierre | todas | 1643 | 98.99c | 97.57% | -1.42 pts | -2.16 a -0.68 | 40 |
| otros_cierre | tocadas | 1495 | 98.94c | 97.32% | -1.61 pts | -2.42 a -0.80 | 40 |
| post_fin_90_97 | todas | 257 | 94.02c | 93.77% | -0.25 pts | -3.17 a +2.68 | 16 |
| post_fin_90_97 | tocadas | 219 | 94.13c | 92.69% | -1.44 pts | -4.84 a +1.97 | 16 |
| TOTAL | todas | 14559 | 98.36c | 97.83% | -0.54 pts | -0.77 a -0.30 | 321 |
| TOTAL | tocadas | 13756 | 98.39c | 97.71% | -0.67 pts | -0.92 a -0.43 | 319 |

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

Aun no hay veredicto: van 247 operaciones cerradas en 12.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
