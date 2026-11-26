# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.3 de 28 | corridas: 306
- Capital inicial: $1,000.00 | valor actual: $983.81 | P&L: $-16.19 (-1.62%)
- Efectivo libre: $0.00 | en ordenes abiertas: $577.58 (7) | en posiciones: $429.53 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 613 colocadas, 277 llenadas, 263 tocadas sin llenarse (sorteo 30%), 66 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 78 | 98.83c | 100.00% | 95.3-100.0% | +1.17 pts | $+63.18 | 0.17 |
| deportes_previo | 138 | 98.06c | 97.34% | 93.8-99.3% | -0.73 pts | $-81.94 | 0.25 |
| otros_cierre | 46 | 99.61c | 100.00% | 92.3-100.0% | +0.39 pts | $+12.27 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 270 | 98.50c | 98.55% | 96.8-99.6% | +0.05 pts | $+7.11 | 0.26 |

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
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $19.30 | 95.9c | 91.2c | post_fin_90_97 |  | Will the highest temperature in Dallas be between 56-57°F on November 26? |
| $98.96 | 98.9c | 100.0c | deportes_previo |  | Oregon Ducks vs. Maryland Eastern Shore Hawks (W) |
| $72.38 | 96.6c | 89.5c | deportes_previo |  | RU Saint-Gilloise vs. KKS Lech Poznań: Neither team to score first? |
| $24.48 | 96.1c | 97.0c | deportes_previo |  | Will Kuopion PS win on 2026-11-26? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 15905 | abiertas: 2479 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4404 | 98.80c | 98.91% | +0.11 pts | -0.19 a +0.42 | 48 |
| clima_cierre | tocadas | 4099 | 98.82c | 98.83% | +0.01 pts | -0.32 a +0.34 | 48 |
| cripto_cierre | todas | 2077 | 98.62c | 98.07% | -0.55 pts | -1.13 a +0.04 | 40 |
| cripto_cierre | tocadas | 1897 | 98.67c | 97.89% | -0.78 pts | -1.42 a -0.14 | 40 |
| deportes_previo | todas | 7432 | 98.05c | 97.44% | -0.62 pts | -0.97 a -0.26 | 195 |
| deportes_previo | tocadas | 7241 | 98.09c | 97.40% | -0.70 pts | -1.06 a -0.34 | 193 |
| otros_cierre | todas | 1724 | 99.00c | 97.56% | -1.43 pts | -2.15 a -0.71 | 42 |
| otros_cierre | tocadas | 1572 | 98.95c | 97.33% | -1.62 pts | -2.41 a -0.83 | 42 |
| post_fin_90_97 | todas | 268 | 94.05c | 94.03% | -0.02 pts | -2.83 a +2.79 | 16 |
| post_fin_90_97 | tocadas | 227 | 94.15c | 92.95% | -1.20 pts | -4.49 a +2.09 | 16 |
| TOTAL | todas | 15905 | 98.37c | 97.88% | -0.48 pts | -0.71 a -0.26 | 341 |
| TOTAL | tocadas | 15036 | 98.39c | 97.78% | -0.62 pts | -0.85 a -0.39 | 339 |

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

Aun no hay veredicto: van 270 operaciones cerradas en 13.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
