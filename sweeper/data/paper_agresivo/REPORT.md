# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 11.1 de 28 | corridas: 251
- Capital inicial: $1,000.00 | valor actual: $929.28 | P&L: $-70.72 (-7.07%)
- Efectivo libre: $0.00 | en ordenes abiertas: $165.03 (3) | en posiciones: $787.03 (11)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 493 colocadas, 231 llenadas, 208 tocadas sin llenarse (sorteo 30%), 51 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 64 | 98.85c | 100.00% | 94.3-100.0% | +1.15 pts | $+50.74 | 0.18 |
| deportes_previo | 109 | 98.00c | 96.62% | 92.2-99.1% | -1.38 pts | $-121.73 | 0.26 |
| otros_cierre | 39 | 99.65c | 100.00% | 91.0-100.0% | +0.35 pts | $+9.45 | 0.34 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 220 | 98.49c | 98.21% | 96.1-99.5% | -0.28 pts | $-47.94 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.4c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $93.01 | 98.8c | 90.5c | deportes_previo |  | Spread: Cong An Ha Noi FC (-2.5) |
| $72.26 | 98.3c | 99.2c | deportes_previo |  | Cong An Ha Noi FC vs. Vissel Kobe: O/U 6.5 |
| $93.00 | 98.3c | 98.3c | deportes_previo |  | Spread: SC Delhi (-2.5) |
| $20.72 | 96.1c | 100.0c | deportes_previo |  | North East United FC vs. SC Delhi: O/U 0.5 |
| $92.78 | 98.8c | 100.0c | otros_cierre |  | Will the US national average gas price be less than $3.6200 on November 24? |
| $92.96 | 99.1c | 99.5c | deportes_previo |  | Spread: Abo Qir Semad SC (-2.5) |
| $93.01 | 99.3c | 99.6c | cripto_cierre |  | Will the price of Bitcoin be between $54,000 and $56,000 on November 24? |
| $14.87 | 99.6c | 99.8c | cripto_cierre |  | Will the price of Ethereum be above $1,500 on November 24? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 13028 | abiertas: 2160 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3537 | 98.82c | 98.90% | +0.08 pts | -0.26 a +0.42 | 39 |
| clima_cierre | tocadas | 3278 | 98.84c | 98.81% | -0.03 pts | -0.40 a +0.33 | 39 |
| cripto_cierre | todas | 1679 | 98.67c | 98.21% | -0.46 pts | -1.08 a +0.17 | 30 |
| cripto_cierre | tocadas | 1531 | 98.72c | 98.04% | -0.68 pts | -1.36 a +0.01 | 30 |
| deportes_previo | todas | 6196 | 98.04c | 97.46% | -0.58 pts | -0.97 a -0.19 | 160 |
| deportes_previo | tocadas | 6055 | 98.07c | 97.43% | -0.64 pts | -1.04 a -0.25 | 158 |
| otros_cierre | todas | 1370 | 98.97c | 97.23% | -1.74 pts | -2.61 a -0.88 | 38 |
| otros_cierre | tocadas | 1264 | 98.92c | 96.99% | -1.93 pts | -2.87 a -1.00 | 38 |
| post_fin_90_97 | todas | 246 | 94.02c | 93.50% | -0.52 pts | -3.57 a +2.53 | 16 |
| post_fin_90_97 | tocadas | 208 | 94.13c | 92.31% | -1.83 pts | -5.40 a +1.75 | 16 |
| TOTAL | todas | 13028 | 98.36c | 97.85% | -0.51 pts | -0.76 a -0.26 | 283 |
| TOTAL | tocadas | 12336 | 98.38c | 97.74% | -0.64 pts | -0.90 a -0.38 | 281 |

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

Aun no hay veredicto: van 220 operaciones cerradas en 11.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
