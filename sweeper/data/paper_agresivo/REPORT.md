# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.2 de 28 | corridas: 305
- Capital inicial: $1,000.00 | valor actual: $970.42 | P&L: $-29.58 (-2.96%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $378.34 (4) | en posiciones: $623.89 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 610 colocadas, 277 llenadas, 263 tocadas sin llenarse (sorteo 30%), 66 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 78 | 98.83c | 100.00% | 95.3-100.0% | +1.17 pts | $+63.18 | 0.17 |
| deportes_previo | 136 | 98.07c | 97.29% | 93.7-99.2% | -0.78 pts | $-86.81 | 0.25 |
| otros_cierre | 46 | 99.61c | 100.00% | 92.3-100.0% | +0.39 pts | $+12.27 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 268 | 98.51c | 98.53% | 96.8-99.6% | +0.02 pts | $+2.23 | 0.26 |

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
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $19.30 | 95.9c | 95.9c | post_fin_90_97 |  | Will the highest temperature in Dallas be between 56-57°F on November 26? |
| $95.40 | 97.3c | 97.0c | deportes_previo |  | Spread: Mjällby AIF (-2.5) |
| $98.96 | 97.8c | 88.2c | deportes_previo |  | Spread: Qairat FK (-3.5) |
| $98.96 | 98.9c | 100.0c | deportes_previo |  | Oregon Ducks vs. Maryland Eastern Shore Hawks (W) |
| $72.38 | 96.6c | 89.5c | deportes_previo |  | RU Saint-Gilloise vs. KKS Lech Poznań: Neither team to score first? |
| $24.48 | 96.1c | 96.1c | deportes_previo |  | Will Kuopion PS win on 2026-11-26? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 15853 | abiertas: 2468 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4395 | 98.80c | 98.91% | +0.11 pts | -0.20 a +0.41 | 48 |
| clima_cierre | tocadas | 4090 | 98.82c | 98.83% | +0.00 pts | -0.32 a +0.33 | 48 |
| cripto_cierre | todas | 2068 | 98.62c | 98.07% | -0.56 pts | -1.14 a +0.03 | 40 |
| cripto_cierre | tocadas | 1892 | 98.67c | 97.89% | -0.79 pts | -1.43 a -0.14 | 40 |
| deportes_previo | todas | 7403 | 98.05c | 97.44% | -0.61 pts | -0.97 a -0.26 | 194 |
| deportes_previo | tocadas | 7212 | 98.09c | 97.40% | -0.69 pts | -1.06 a -0.33 | 192 |
| otros_cierre | todas | 1719 | 99.00c | 97.56% | -1.44 pts | -2.16 a -0.71 | 42 |
| otros_cierre | tocadas | 1567 | 98.95c | 97.32% | -1.63 pts | -2.42 a -0.83 | 42 |
| post_fin_90_97 | todas | 268 | 94.05c | 94.03% | -0.02 pts | -2.83 a +2.79 | 16 |
| post_fin_90_97 | tocadas | 227 | 94.15c | 92.95% | -1.20 pts | -4.49 a +2.09 | 16 |
| TOTAL | todas | 15853 | 98.37c | 97.88% | -0.49 pts | -0.71 a -0.26 | 340 |
| TOTAL | tocadas | 14988 | 98.40c | 97.77% | -0.62 pts | -0.85 a -0.39 | 338 |

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

Aun no hay veredicto: van 268 operaciones cerradas en 13.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
