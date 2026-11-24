# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 10.8 de 28 | corridas: 243
- Capital inicial: $1,000.00 | valor actual: $930.13 | P&L: $-69.87 (-6.99%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $433.04 (7) | en posiciones: $513.96 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 488 colocadas, 223 llenadas, 207 tocadas sin llenarse (sorteo 30%), 51 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 64 | 98.85c | 100.00% | 94.3-100.0% | +1.15 pts | $+50.74 | 0.18 |
| deportes_previo | 106 | 98.00c | 96.53% | 92.0-99.0% | -1.47 pts | $-126.53 | 0.26 |
| otros_cierre | 38 | 99.65c | 100.00% | 90.8-100.0% | +0.35 pts | $+9.19 | 0.35 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 216 | 98.49c | 98.18% | 96.0-99.5% | -0.32 pts | $-53.00 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 83.6c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.63 | 99.2c | 99.2c | deportes_previo |  | Spread: Newcastle United Jets (-2.5) |
| $21.52 | 99.1c | 98.2c | deportes_previo |  | Newcastle United Jets vs. Kashiwa Reysol: Neither team to score first? |
| $92.63 | 96.0c | 96.5c | deportes_previo |  | Spread: Newcastle United Jets (-1.5) |
| $92.78 | 98.8c | 98.8c | otros_cierre |  | Will the US national average gas price be less than $3.6200 on November 24? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 12811 | abiertas: 2105 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3478 | 98.82c | 98.94% | +0.11 pts | -0.23 a +0.45 | 37 |
| clima_cierre | tocadas | 3223 | 98.85c | 98.85% | +0.01 pts | -0.36 a +0.37 | 37 |
| cripto_cierre | todas | 1646 | 98.68c | 98.24% | -0.44 pts | -1.07 a +0.19 | 29 |
| cripto_cierre | tocadas | 1502 | 98.73c | 98.07% | -0.66 pts | -1.35 a +0.03 | 29 |
| deportes_previo | todas | 6117 | 98.04c | 97.46% | -0.58 pts | -0.97 a -0.19 | 158 |
| deportes_previo | tocadas | 5976 | 98.07c | 97.43% | -0.64 pts | -1.04 a -0.24 | 156 |
| otros_cierre | todas | 1326 | 98.97c | 97.13% | -1.83 pts | -2.72 a -0.94 | 38 |
| otros_cierre | tocadas | 1237 | 98.93c | 96.93% | -2.00 pts | -2.96 a -1.05 | 38 |
| post_fin_90_97 | todas | 244 | 94.01c | 93.44% | -0.57 pts | -3.64 a +2.51 | 16 |
| post_fin_90_97 | tocadas | 207 | 94.13c | 92.27% | -1.86 pts | -5.46 a +1.73 | 16 |
| TOTAL | todas | 12811 | 98.35c | 97.85% | -0.50 pts | -0.75 a -0.26 | 278 |
| TOTAL | tocadas | 12145 | 98.38c | 97.75% | -0.63 pts | -0.89 a -0.37 | 276 |

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

Aun no hay veredicto: van 216 operaciones cerradas en 10.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
