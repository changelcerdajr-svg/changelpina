# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 11.3 de 28 | corridas: 256
- Capital inicial: $1,000.00 | valor actual: $939.09 | P&L: $-60.91 (-6.09%)
- Efectivo libre: $0.00 | en ordenes abiertas: $276.01 (4) | en posiciones: $683.56 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 507 colocadas, 237 llenadas, 213 tocadas sin llenarse (sorteo 30%), 53 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 66 | 98.86c | 100.00% | 94.5-100.0% | +1.14 pts | $+51.46 | 0.18 |
| deportes_previo | 114 | 98.02c | 96.76% | 92.5-99.1% | -1.26 pts | $-116.06 | 0.26 |
| otros_cierre | 40 | 99.62c | 100.00% | 91.2-100.0% | +0.38 pts | $+10.58 | 0.34 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 228 | 98.50c | 98.27% | 96.2-99.6% | -0.23 pts | $-40.43 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.8c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $94.12 | 99.5c | 97.8c | deportes_previo |  | Bradford City AFC vs. Barnsley FC: Neither team to score first? |
| $94.19 | 97.9c | 97.9c | deportes_previo |  | Spread: Barnsley FC (-2.5) |
| $94.12 | 99.8c | 100.0c | otros_cierre |  | Will Apple (AAPL) close above $335 on November 24? |
| $67.95 | 99.8c | 98.0c | otros_cierre |  | Will Apple (AAPL) close above $340 on November 24? |
| $24.70 | 98.8c | 99.0c | cripto_cierre |  | NVIDIA (NVDA) Up or Down on November 24? |
| $94.08 | 97.8c | 97.8c | cripto_cierre |  | Apple (AAPL) Up or Down on November 24? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 13353 | abiertas: 2232 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3638 | 98.81c | 98.93% | +0.11 pts | -0.22 a +0.45 | 39 |
| clima_cierre | tocadas | 3373 | 98.84c | 98.84% | +0.00 pts | -0.35 a +0.36 | 39 |
| cripto_cierre | todas | 1768 | 98.66c | 98.08% | -0.59 pts | -1.22 a +0.05 | 34 |
| cripto_cierre | tocadas | 1617 | 98.71c | 97.90% | -0.81 pts | -1.50 a -0.12 | 34 |
| deportes_previo | todas | 6291 | 98.05c | 97.43% | -0.61 pts | -1.00 a -0.23 | 164 |
| deportes_previo | tocadas | 6148 | 98.08c | 97.41% | -0.67 pts | -1.07 a -0.28 | 162 |
| otros_cierre | todas | 1403 | 98.95c | 97.29% | -1.66 pts | -2.51 a -0.82 | 38 |
| otros_cierre | tocadas | 1295 | 98.91c | 97.07% | -1.84 pts | -2.76 a -0.93 | 38 |
| post_fin_90_97 | todas | 253 | 94.03c | 93.68% | -0.35 pts | -3.32 a +2.62 | 16 |
| post_fin_90_97 | tocadas | 215 | 94.14c | 92.56% | -1.58 pts | -5.05 a +1.89 | 16 |
| TOTAL | todas | 13353 | 98.36c | 97.84% | -0.52 pts | -0.76 a -0.27 | 291 |
| TOTAL | tocadas | 12648 | 98.38c | 97.73% | -0.65 pts | -0.90 a -0.39 | 289 |

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

Aun no hay veredicto: van 228 operaciones cerradas en 11.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
