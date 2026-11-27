# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.8 de 28 | corridas: 320
- Capital inicial: $1,000.00 | valor actual: $896.50 | P&L: $-103.50 (-10.35%)
- Efectivo libre: $0.00 | en ordenes abiertas: $570.24 (9) | en posiciones: $349.91 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 641 colocadas, 291 llenadas, 271 tocadas sin llenarse (sorteo 30%), 70 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 80 | 98.82c | 100.00% | 95.4-100.0% | +1.18 pts | $+65.56 | 0.17 |
| deportes_previo | 147 | 98.08c | 96.62% | 93.2-98.9% | -1.46 pts | $-172.74 | 0.25 |
| otros_cierre | 48 | 99.61c | 100.00% | 92.6-100.0% | +0.39 pts | $+12.91 | 0.32 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 284 | 98.51c | 98.14% | 96.4-99.5% | -0.36 pts | $-79.85 | 0.26 |

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
| $91.77 | 99.8c | 81.3c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $12.22 | 96.0c | 95.5c | deportes_previo |  | Spread: Gonzaga Bulldogs (-20.5) |
| $99.87 | 96.0c | 91.5c | deportes_previo |  | Spread: Baylor Bears (-14.5) |
| $9.22 | 97.3c | 97.4c | deportes_previo |  | Spread: Melbourne City FC (-3.5) |
| $14.20 | 96.6c | 96.6c | deportes_previo |  | Macarthur FC vs. Melbourne City FC: O/U 6.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16573 | abiertas: 2567 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4625 | 98.80c | 98.94% | +0.14 pts | -0.15 a +0.44 | 49 |
| clima_cierre | tocadas | 4308 | 98.82c | 98.86% | +0.04 pts | -0.27 a +0.36 | 49 |
| cripto_cierre | todas | 2130 | 98.61c | 98.08% | -0.54 pts | -1.11 a +0.04 | 41 |
| cripto_cierre | tocadas | 1937 | 98.67c | 97.88% | -0.78 pts | -1.42 a -0.15 | 41 |
| deportes_previo | todas | 7805 | 98.04c | 97.37% | -0.68 pts | -1.03 a -0.33 | 210 |
| deportes_previo | tocadas | 7594 | 98.09c | 97.32% | -0.77 pts | -1.13 a -0.41 | 208 |
| otros_cierre | todas | 1735 | 98.99c | 97.58% | -1.41 pts | -2.13 a -0.70 | 42 |
| otros_cierre | tocadas | 1581 | 98.95c | 97.34% | -1.60 pts | -2.39 a -0.82 | 42 |
| post_fin_90_97 | todas | 278 | 94.00c | 93.88% | -0.11 pts | -2.90 a +2.68 | 17 |
| post_fin_90_97 | tocadas | 235 | 94.10c | 92.77% | -1.34 pts | -4.61 a +1.94 | 17 |
| TOTAL | todas | 16573 | 98.36c | 97.86% | -0.50 pts | -0.72 a -0.28 | 359 |
| TOTAL | tocadas | 15655 | 98.39c | 97.75% | -0.64 pts | -0.87 a -0.41 | 357 |

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

Aun no hay veredicto: van 284 operaciones cerradas en 13.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
