# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 8.5 de 28 | corridas: 182
- Capital inicial: $1,000.00 | valor actual: $866.55 | P&L: $-133.45 (-13.35%)
- Efectivo libre: $0.00 | en ordenes abiertas: $172.84 (4) | en posiciones: $703.59 (11)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 377 colocadas, 170 llenadas, 164 tocadas sin llenarse (sorteo 30%), 39 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 49 | 98.78c | 100.00% | 92.7-100.0% | +1.22 pts | $+40.02 | 0.14 |
| deportes_previo | 74 | 98.05c | 94.97% | 88.7-98.6% | -3.08 pts | $-182.21 | 0.29 |
| otros_cierre | 31 | 99.67c | 100.00% | 89.0-100.0% | +0.33 pts | $+7.04 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 159 | 98.53c | 97.50% | 94.6-99.4% | -1.03 pts | $-123.57 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 89.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $6.92 | 93.9c | 97.4c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 66-67°F on November 21? |
| $86.78 | 98.7c | 98.7c | deportes_previo |  | Spread: CA Mineiro (-2.5) |
| $86.66 | 96.7c | 96.7c | deportes_previo |  | Spread: Hawai'i (-17.5) |
| $94.72 | 99.6c | 99.3c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $17.05 | 99.6c | 99.8c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 21, 2026? |
| $94.88 | 99.8c | 99.5c | clima_cierre |  | Will the next hurricane form between November 17 and November 21, 2026? |
| $93.98 | 98.5c | 99.7c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $8.19 | 97.9c | 99.4c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 9264 | abiertas: 2438 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2567 | 98.83c | 99.07% | +0.23 pts | -0.14 a +0.60 | 24 |
| clima_cierre | tocadas | 2375 | 98.85c | 98.99% | +0.13 pts | -0.26 a +0.53 | 24 |
| cripto_cierre | todas | 1276 | 98.71c | 98.04% | -0.67 pts | -1.42 a +0.08 | 25 |
| cripto_cierre | tocadas | 1158 | 98.74c | 97.84% | -0.90 pts | -1.73 a -0.08 | 25 |
| deportes_previo | todas | 4144 | 98.03c | 97.36% | -0.68 pts | -1.16 a -0.19 | 112 |
| deportes_previo | tocadas | 4038 | 98.07c | 97.31% | -0.76 pts | -1.25 a -0.26 | 111 |
| otros_cierre | todas | 1189 | 99.00c | 97.22% | -1.78 pts | -2.70 a -0.85 | 33 |
| otros_cierre | tocadas | 1115 | 98.97c | 97.04% | -1.93 pts | -2.92 a -0.94 | 33 |
| post_fin_90_97 | todas | 88 | 94.33c | 96.59% | +2.26 pts | -1.54 a +6.07 | 3 |
| post_fin_90_97 | tocadas | 71 | 94.38c | 95.77% | +1.39 pts | -3.30 a +6.09 | 3 |
| TOTAL | todas | 9264 | 98.44c | 97.90% | -0.54 pts | -0.83 a -0.25 | 197 |
| TOTAL | tocadas | 8757 | 98.46c | 97.79% | -0.67 pts | -0.97 a -0.36 | 196 |

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

Aun no hay veredicto: van 159 operaciones cerradas en 8.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
