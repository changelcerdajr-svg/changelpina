# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 8.6 de 28 | corridas: 184
- Capital inicial: $1,000.00 | valor actual: $867.42 | P&L: $-132.58 (-13.26%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $167.08 (3) | en posiciones: $710.49 (12)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 379 colocadas, 172 llenadas, 165 tocadas sin llenarse (sorteo 30%), 39 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 49 | 98.78c | 100.00% | 92.7-100.0% | +1.22 pts | $+40.02 | 0.14 |
| deportes_previo | 75 | 98.06c | 95.04% | 88.9-98.6% | -3.01 pts | $-181.07 | 0.29 |
| otros_cierre | 31 | 99.67c | 100.00% | 89.0-100.0% | +0.33 pts | $+7.04 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 160 | 98.53c | 97.52% | 94.6-99.4% | -1.01 pts | $-122.43 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 90.1c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $6.92 | 93.9c | 97.4c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 66-67°F on November 21? |
| $86.66 | 96.7c | 96.0c | deportes_previo |  | Spread: Hawai'i (-17.5) |
| $94.72 | 99.6c | 99.3c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $17.05 | 99.6c | 99.8c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 21, 2026? |
| $94.88 | 99.8c | 99.5c | clima_cierre |  | Will the next hurricane form between November 17 and November 21, 2026? |
| $93.98 | 98.5c | 99.7c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $8.19 | 97.9c | 99.8c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |
| $86.75 | 98.5c | 98.5c | deportes_previo |  | Spread: Tokushima Vortis (-3.5) |
| $6.94 | 98.6c | 98.6c | deportes_previo |  | Spread: Shōnan Bellmāre (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 9328 | abiertas: 2595 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2583 | 98.84c | 99.07% | +0.24 pts | -0.13 a +0.60 | 24 |
| clima_cierre | tocadas | 2390 | 98.85c | 99.00% | +0.14 pts | -0.26 a +0.54 | 24 |
| cripto_cierre | todas | 1279 | 98.71c | 98.05% | -0.67 pts | -1.42 a +0.09 | 25 |
| cripto_cierre | tocadas | 1160 | 98.75c | 97.84% | -0.90 pts | -1.73 a -0.08 | 25 |
| deportes_previo | todas | 4179 | 98.03c | 97.38% | -0.65 pts | -1.13 a -0.17 | 112 |
| deportes_previo | tocadas | 4073 | 98.07c | 97.34% | -0.73 pts | -1.22 a -0.24 | 111 |
| otros_cierre | todas | 1199 | 99.00c | 97.25% | -1.76 pts | -2.68 a -0.84 | 33 |
| otros_cierre | tocadas | 1121 | 98.97c | 97.06% | -1.91 pts | -2.90 a -0.93 | 33 |
| post_fin_90_97 | todas | 88 | 94.33c | 96.59% | +2.26 pts | -1.54 a +6.07 | 3 |
| post_fin_90_97 | tocadas | 71 | 94.38c | 95.77% | +1.39 pts | -3.30 a +6.09 | 3 |
| TOTAL | todas | 9328 | 98.44c | 97.91% | -0.52 pts | -0.81 a -0.23 | 197 |
| TOTAL | tocadas | 8815 | 98.45c | 97.80% | -0.65 pts | -0.95 a -0.35 | 196 |

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

Aun no hay veredicto: van 160 operaciones cerradas en 8.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
