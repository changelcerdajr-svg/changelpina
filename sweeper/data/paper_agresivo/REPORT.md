# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 10.9 de 28 | corridas: 246
- Capital inicial: $1,000.00 | valor actual: $930.00 | P&L: $-70.00 (-7.00%)
- Efectivo libre: $4.86 | en ordenes abiertas: $301.73 (5) | en posiciones: $645.21 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 491 colocadas, 228 llenadas, 207 tocadas sin llenarse (sorteo 30%), 51 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 64 | 98.85c | 100.00% | 94.3-100.0% | +1.15 pts | $+50.74 | 0.18 |
| deportes_previo | 109 | 98.00c | 96.62% | 92.2-99.1% | -1.38 pts | $-121.73 | 0.26 |
| otros_cierre | 38 | 99.65c | 100.00% | 90.8-100.0% | +0.35 pts | $+9.19 | 0.35 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 219 | 98.48c | 98.20% | 96.1-99.5% | -0.28 pts | $-48.20 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.5c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $93.01 | 98.8c | 98.4c | deportes_previo |  | Spread: Cong An Ha Noi FC (-2.5) |
| $72.26 | 98.3c | 98.4c | deportes_previo |  | Cong An Ha Noi FC vs. Vissel Kobe: O/U 6.5 |
| $64.87 | 99.6c | 97.5c | otros_cierre |  | Will DICK'S Sporting Goods Q3 Dick's business comparable sales growth be below 1 |
| $92.78 | 98.8c | 97.2c | otros_cierre |  | Will the US national average gas price be less than $3.6200 on November 24? |
| $93.01 | 99.3c | 98.8c | cripto_cierre |  | Will the price of Bitcoin be between $54,000 and $56,000 on November 24? |
| $14.87 | 99.6c | 99.7c | cripto_cierre |  | Will the price of Ethereum be above $1,500 on November 24? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 12880 | abiertas: 2144 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3508 | 98.82c | 98.92% | +0.09 pts | -0.25 a +0.43 | 38 |
| clima_cierre | tocadas | 3249 | 98.85c | 98.83% | -0.02 pts | -0.38 a +0.35 | 38 |
| cripto_cierre | todas | 1651 | 98.68c | 98.24% | -0.43 pts | -1.06 a +0.20 | 29 |
| cripto_cierre | tocadas | 1507 | 98.72c | 98.08% | -0.65 pts | -1.33 a +0.04 | 29 |
| deportes_previo | todas | 6150 | 98.04c | 97.44% | -0.60 pts | -0.99 a -0.21 | 160 |
| deportes_previo | tocadas | 6009 | 98.07c | 97.41% | -0.66 pts | -1.06 a -0.26 | 158 |
| otros_cierre | todas | 1327 | 98.96c | 97.14% | -1.83 pts | -2.72 a -0.94 | 38 |
| otros_cierre | tocadas | 1238 | 98.93c | 96.93% | -2.00 pts | -2.95 a -1.04 | 38 |
| post_fin_90_97 | todas | 244 | 94.01c | 93.44% | -0.57 pts | -3.64 a +2.51 | 16 |
| post_fin_90_97 | tocadas | 207 | 94.13c | 92.27% | -1.86 pts | -5.46 a +1.73 | 16 |
| TOTAL | todas | 12880 | 98.35c | 97.84% | -0.52 pts | -0.76 a -0.27 | 281 |
| TOTAL | tocadas | 12210 | 98.38c | 97.74% | -0.64 pts | -0.91 a -0.38 | 279 |

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

Aun no hay veredicto: van 219 operaciones cerradas en 10.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
