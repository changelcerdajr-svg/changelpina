# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 15.0 de 28 | corridas: 351
- Capital inicial: $1,000.00 | valor actual: $934.75 | P&L: $-65.25 (-6.52%)
- Efectivo libre: $0.00 | en ordenes abiertas: $292.26 (5) | en posiciones: $659.23 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 700 colocadas, 319 llenadas, 298 tocadas sin llenarse (sorteo 30%), 78 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 84 | 98.84c | 100.00% | 95.6-100.0% | +1.16 pts | $+66.77 | 0.17 |
| deportes_previo | 166 | 98.06c | 96.95% | 94.0-99.1% | -1.10 pts | $-145.49 | 0.24 |
| otros_cierre | 52 | 99.56c | 100.00% | 93.1-100.0% | +0.44 pts | $+15.78 | 0.31 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 311 | 98.48c | 98.28% | 96.7-99.5% | -0.20 pts | $-48.51 | 0.25 |

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
| $91.77 | 99.8c | 99.7c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $93.04 | 99.8c | 99.4c | deportes_previo |  | Prairie View A&M Panthers vs. Iowa Hawkeyes |
| $94.85 | 95.0c | 85.1c | deportes_previo |  | Bandirmaspor vs. Batman Petrolspor: O/U 5.5 |
| $94.90 | 99.5c | 94.9c | deportes_previo |  | Sivasspor vs. Bodrum FK: O/U 5.5 |
| $90.48 | 97.8c | 97.8c | deportes_previo |  | Spread: Notts County FC (-2.5) |
| $71.55 | 99.9c | 99.9c | cripto_cierre |  | Will the price of Ethereum be above $1,400 on November 28? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 18209 | abiertas: 3603 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 5019 | 98.80c | 99.02% | +0.22 pts | -0.05 a +0.49 | 49 |
| clima_cierre | tocadas | 4679 | 98.83c | 98.95% | +0.12 pts | -0.17 a +0.41 | 49 |
| cripto_cierre | todas | 2305 | 98.58c | 98.18% | -0.40 pts | -0.94 a +0.14 | 42 |
| cripto_cierre | tocadas | 2091 | 98.65c | 97.99% | -0.65 pts | -1.25 a -0.06 | 42 |
| deportes_previo | todas | 8557 | 98.05c | 97.46% | -0.59 pts | -0.92 a -0.26 | 222 |
| deportes_previo | tocadas | 8338 | 98.09c | 97.42% | -0.67 pts | -1.01 a -0.34 | 220 |
| otros_cierre | todas | 2031 | 98.92c | 97.78% | -1.13 pts | -1.77 a -0.50 | 45 |
| otros_cierre | tocadas | 1872 | 98.87c | 97.60% | -1.27 pts | -1.96 a -0.58 | 45 |
| post_fin_90_97 | todas | 297 | 94.05c | 92.93% | -1.13 pts | -4.01 a +1.76 | 21 |
| post_fin_90_97 | tocadas | 252 | 94.15c | 91.67% | -2.48 pts | -5.86 a +0.89 | 21 |
| TOTAL | todas | 18209 | 98.35c | 97.94% | -0.41 pts | -0.61 a -0.21 | 379 |
| TOTAL | tocadas | 17232 | 98.38c | 97.84% | -0.55 pts | -0.76 a -0.33 | 377 |

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

Aun no hay veredicto: van 311 operaciones cerradas en 15.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
