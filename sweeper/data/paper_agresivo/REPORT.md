# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 12.2 de 28 | corridas: 279
- Capital inicial: $1,000.00 | valor actual: $963.26 | P&L: $-36.74 (-3.67%)
- Efectivo libre: $1.19 | en ordenes abiertas: $383.73 (4) | en posiciones: $596.84 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 566 colocadas, 259 llenadas, 244 tocadas sin llenarse (sorteo 30%), 59 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 74 | 98.86c | 100.00% | 95.1-100.0% | +1.14 pts | $+57.57 | 0.18 |
| deportes_previo | 125 | 98.04c | 97.05% | 93.2-99.2% | -0.99 pts | $-100.76 | 0.25 |
| otros_cierre | 44 | 99.63c | 100.00% | 92.0-100.0% | +0.37 pts | $+11.37 | 0.33 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 251 | 98.52c | 98.43% | 96.5-99.6% | -0.09 pts | $-18.23 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 81.7c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $8.21 | 98.9c | 98.9c | deportes_previo |  | Navy Midshipmen vs. Iowa Hawkeyes (W) |
| $96.02 | 98.0c | 98.4c | deportes_previo |  | Spread: Aldershot Town FC (-1.5) |
| $85.70 | 99.8c | 99.8c | deportes_previo |  | Spread: Aldershot Town FC (-2.5) |
| $96.25 | 96.8c | 96.8c | cripto_cierre |  | Microsoft (MSFT) Up or Down on November 25? |
| $96.25 | 99.7c | 99.7c | cripto_cierre |  | Amazon (AMZN) Up or Down on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 14680 | abiertas: 2320 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4017 | 98.80c | 98.85% | +0.06 pts | -0.27 a +0.38 | 46 |
| clima_cierre | tocadas | 3733 | 98.82c | 98.77% | -0.05 pts | -0.40 a +0.30 | 46 |
| cripto_cierre | todas | 1913 | 98.65c | 98.17% | -0.48 pts | -1.07 a +0.12 | 35 |
| cripto_cierre | tocadas | 1750 | 98.69c | 98.00% | -0.69 pts | -1.34 a -0.04 | 35 |
| deportes_previo | todas | 6838 | 98.04c | 97.36% | -0.68 pts | -1.06 a -0.31 | 185 |
| deportes_previo | tocadas | 6666 | 98.08c | 97.32% | -0.76 pts | -1.14 a -0.38 | 183 |
| otros_cierre | todas | 1655 | 98.99c | 97.58% | -1.41 pts | -2.14 a -0.67 | 40 |
| otros_cierre | tocadas | 1507 | 98.94c | 97.35% | -1.59 pts | -2.40 a -0.79 | 40 |
| post_fin_90_97 | todas | 257 | 94.02c | 93.77% | -0.25 pts | -3.17 a +2.68 | 16 |
| post_fin_90_97 | tocadas | 219 | 94.13c | 92.69% | -1.44 pts | -4.84 a +1.97 | 16 |
| TOTAL | todas | 14680 | 98.37c | 97.84% | -0.53 pts | -0.76 a -0.30 | 322 |
| TOTAL | tocadas | 13875 | 98.39c | 97.73% | -0.66 pts | -0.91 a -0.42 | 320 |

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

Aun no hay veredicto: van 251 operaciones cerradas en 12.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
