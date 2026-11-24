# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 10.7 de 28 | corridas: 240
- Capital inicial: $1,000.00 | valor actual: $927.84 | P&L: $-72.16 (-7.22%)
- Efectivo libre: $0.03 | en ordenes abiertas: $280.42 (4) | en posiciones: $665.22 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 479 colocadas, 220 llenadas, 204 tocadas sin llenarse (sorteo 30%), 51 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 62 | 98.81c | 100.00% | 94.2-100.0% | +1.19 pts | $+50.28 | 0.17 |
| deportes_previo | 105 | 97.98c | 96.50% | 91.9-99.0% | -1.49 pts | $-126.63 | 0.26 |
| otros_cierre | 36 | 99.66c | 100.00% | 90.4-100.0% | +0.34 pts | $+8.42 | 0.35 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 211 | 98.46c | 98.13% | 95.9-99.5% | -0.33 pts | $-54.33 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 84.8c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $61.22 | 99.2c | 99.4c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 23, 2026? |
| $92.57 | 99.7c | 99.1c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 23, 2026? |
| $91.44 | 99.8c | 99.5c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 17-23? |
| $91.44 | 99.7c | 99.0c | cripto_cierre |  | MicroStrategy announces >1000 BTC purchase November 17-23? |
| $92.63 | 99.2c | 99.0c | deportes_previo |  | Spread: Newcastle United Jets (-2.5) |
| $21.52 | 99.1c | 98.4c | deportes_previo |  | Newcastle United Jets vs. Kashiwa Reysol: Neither team to score first? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 12626 | abiertas: 2147 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3398 | 98.83c | 99.00% | +0.17 pts | -0.16 a +0.51 | 34 |
| clima_cierre | tocadas | 3145 | 98.85c | 98.92% | +0.07 pts | -0.29 a +0.43 | 34 |
| cripto_cierre | todas | 1621 | 98.68c | 98.21% | -0.46 pts | -1.10 a +0.17 | 29 |
| cripto_cierre | tocadas | 1477 | 98.72c | 98.04% | -0.69 pts | -1.39 a +0.01 | 29 |
| deportes_previo | todas | 6053 | 98.04c | 97.45% | -0.59 pts | -0.98 a -0.19 | 157 |
| deportes_previo | tocadas | 5912 | 98.07c | 97.42% | -0.65 pts | -1.05 a -0.25 | 155 |
| otros_cierre | todas | 1310 | 98.97c | 97.18% | -1.80 pts | -2.69 a -0.91 | 37 |
| otros_cierre | tocadas | 1222 | 98.94c | 96.97% | -1.96 pts | -2.92 a -1.01 | 37 |
| post_fin_90_97 | todas | 244 | 94.01c | 93.44% | -0.57 pts | -3.64 a +2.51 | 16 |
| post_fin_90_97 | tocadas | 207 | 94.13c | 92.27% | -1.86 pts | -5.46 a +1.73 | 16 |
| TOTAL | todas | 12626 | 98.35c | 97.86% | -0.49 pts | -0.74 a -0.24 | 273 |
| TOTAL | tocadas | 11963 | 98.38c | 97.76% | -0.62 pts | -0.88 a -0.36 | 271 |

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

Aun no hay veredicto: van 211 operaciones cerradas en 10.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
