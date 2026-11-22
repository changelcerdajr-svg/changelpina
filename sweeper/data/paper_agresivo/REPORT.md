# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 8.7 de 28 | corridas: 186
- Capital inicial: $1,000.00 | valor actual: $824.15 | P&L: $-175.85 (-17.58%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $270.86 (5) | en posiciones: $608.32 (10)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 381 colocadas, 172 llenadas, 165 tocadas sin llenarse (sorteo 30%), 39 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 51 | 98.77c | 100.00% | 93.0-100.0% | +1.23 pts | $+41.62 | 0.18 |
| deportes_previo | 75 | 98.06c | 95.04% | 88.9-98.6% | -3.01 pts | $-181.07 | 0.29 |
| otros_cierre | 31 | 99.67c | 100.00% | 89.0-100.0% | +0.33 pts | $+7.04 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 162 | 98.53c | 97.54% | 94.7-99.4% | -0.99 pts | $-120.82 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 89.9c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $6.92 | 93.9c | 97.4c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 66-67°F on November 21? |
| $86.66 | 96.7c | 96.0c | deportes_previo |  | Spread: Hawai'i (-17.5) |
| $94.72 | 99.6c | 99.3c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $17.05 | 99.6c | 99.8c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 21, 2026? |
| $94.88 | 99.8c | 99.5c | clima_cierre |  | Will the next hurricane form between November 17 and November 21, 2026? |
| $86.75 | 98.5c | 49.9c | deportes_previo |  | Spread: Tokushima Vortis (-3.5) |
| $6.94 | 98.6c | 91.5c | deportes_previo |  | Spread: Shōnan Bellmāre (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 9473 | abiertas: 2845 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2592 | 98.83c | 99.04% | +0.20 pts | -0.17 a +0.58 | 25 |
| clima_cierre | tocadas | 2399 | 98.85c | 98.96% | +0.10 pts | -0.30 a +0.51 | 25 |
| cripto_cierre | todas | 1282 | 98.71c | 98.05% | -0.66 pts | -1.41 a +0.09 | 25 |
| cripto_cierre | tocadas | 1163 | 98.75c | 97.85% | -0.90 pts | -1.72 a -0.07 | 25 |
| deportes_previo | todas | 4305 | 98.02c | 97.41% | -0.61 pts | -1.08 a -0.14 | 114 |
| deportes_previo | tocadas | 4199 | 98.06c | 97.37% | -0.69 pts | -1.17 a -0.21 | 113 |
| otros_cierre | todas | 1199 | 99.00c | 97.25% | -1.76 pts | -2.68 a -0.84 | 33 |
| otros_cierre | tocadas | 1121 | 98.97c | 97.06% | -1.91 pts | -2.90 a -0.93 | 33 |
| post_fin_90_97 | todas | 95 | 94.32c | 96.84% | +2.52 pts | -1.01 a +6.05 | 3 |
| post_fin_90_97 | tocadas | 77 | 94.37c | 96.10% | +1.73 pts | -2.60 a +6.06 | 3 |
| TOTAL | todas | 9473 | 98.42c | 97.92% | -0.51 pts | -0.79 a -0.22 | 200 |
| TOTAL | tocadas | 8959 | 98.44c | 97.81% | -0.64 pts | -0.94 a -0.34 | 199 |

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

Aun no hay veredicto: van 162 operaciones cerradas en 8.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
