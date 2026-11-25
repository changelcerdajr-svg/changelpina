# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 12.3 de 28 | corridas: 281
- Capital inicial: $1,000.00 | valor actual: $962.45 | P&L: $-37.55 (-3.76%)
- Efectivo libre: $0.00 | en ordenes abiertas: $393.23 (5) | en posiciones: $588.63 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 569 colocadas, 259 llenadas, 246 tocadas sin llenarse (sorteo 30%), 59 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 74 | 98.86c | 100.00% | 95.1-100.0% | +1.14 pts | $+57.57 | 0.18 |
| deportes_previo | 126 | 98.04c | 97.05% | 93.2-99.2% | -0.99 pts | $-100.67 | 0.25 |
| otros_cierre | 44 | 99.63c | 100.00% | 92.0-100.0% | +0.37 pts | $+11.37 | 0.33 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 252 | 98.52c | 98.43% | 96.6-99.6% | -0.09 pts | $-18.14 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 83.2c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $96.02 | 98.0c | 99.2c | deportes_previo |  | Spread: Aldershot Town FC (-1.5) |
| $85.70 | 99.8c | 99.8c | deportes_previo |  | Spread: Aldershot Town FC (-2.5) |
| $96.25 | 96.8c | 95.5c | cripto_cierre |  | Microsoft (MSFT) Up or Down on November 25? |
| $96.25 | 99.7c | 97.5c | cripto_cierre |  | Amazon (AMZN) Up or Down on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 14760 | abiertas: 2393 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4033 | 98.80c | 98.86% | +0.06 pts | -0.26 a +0.39 | 46 |
| clima_cierre | tocadas | 3749 | 98.82c | 98.77% | -0.05 pts | -0.40 a +0.30 | 46 |
| cripto_cierre | todas | 1920 | 98.64c | 98.18% | -0.47 pts | -1.06 a +0.13 | 35 |
| cripto_cierre | tocadas | 1756 | 98.69c | 98.01% | -0.68 pts | -1.33 a -0.03 | 35 |
| deportes_previo | todas | 6877 | 98.05c | 97.38% | -0.67 pts | -1.05 a -0.30 | 185 |
| deportes_previo | tocadas | 6702 | 98.09c | 97.34% | -0.75 pts | -1.13 a -0.37 | 183 |
| otros_cierre | todas | 1672 | 99.00c | 97.61% | -1.39 pts | -2.12 a -0.66 | 40 |
| otros_cierre | tocadas | 1524 | 98.95c | 97.38% | -1.57 pts | -2.37 a -0.77 | 40 |
| post_fin_90_97 | todas | 258 | 94.02c | 93.80% | -0.22 pts | -3.13 a +2.69 | 16 |
| post_fin_90_97 | tocadas | 219 | 94.13c | 92.69% | -1.44 pts | -4.84 a +1.97 | 16 |
| TOTAL | todas | 14760 | 98.37c | 97.85% | -0.52 pts | -0.75 a -0.29 | 322 |
| TOTAL | tocadas | 13950 | 98.39c | 97.74% | -0.65 pts | -0.90 a -0.41 | 320 |

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

Aun no hay veredicto: van 252 operaciones cerradas en 12.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
