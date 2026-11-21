# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 8.2 de 28 | corridas: 171
- Capital inicial: $1,000.00 | valor actual: $958.64 | P&L: $-41.36 (-4.14%)
- Efectivo libre: $0.00 | en ordenes abiertas: $54.56 (1) | en posiciones: $911.20 (13)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 366 colocadas, 165 llenadas, 161 tocadas sin llenarse (sorteo 30%), 39 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 49 | 98.78c | 100.00% | 92.7-100.0% | +1.22 pts | $+40.02 | 0.14 |
| deportes_previo | 67 | 98.00c | 96.27% | 89.8-99.2% | -1.73 pts | $-92.88 | 0.31 |
| otros_cierre | 31 | 99.67c | 100.00% | 89.0-100.0% | +0.33 pts | $+7.04 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 152 | 98.53c | 98.25% | 95.3-99.6% | -0.29 pts | $-34.23 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.9c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $6.92 | 93.9c | 97.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 66-67°F on November 21? |
| $93.94 | 99.5c | 99.5c | deportes_previo |  | NEC vs. PSV: Neither team to score first? |
| $95.35 | 98.4c | 98.5c | deportes_previo |  | Spread: OGC Nice (-2.5) |
| $95.89 | 97.4c | 96.2c | deportes_previo |  | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $95.89 | 96.7c | 96.7c | deportes_previo |  | Spread: FC Schalke 04 (-2.5) |
| $94.72 | 99.6c | 99.2c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $17.05 | 99.6c | 99.7c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 21, 2026? |
| $94.88 | 99.8c | 99.5c | clima_cierre |  | Will the next hurricane form between November 17 and November 21, 2026? |
| $93.98 | 98.5c | 98.4c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $8.19 | 97.9c | 94.2c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 8539 | abiertas: 2521 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2450 | 98.84c | 99.02% | +0.18 pts | -0.20 a +0.57 | 24 |
| clima_cierre | tocadas | 2264 | 98.86c | 98.94% | +0.08 pts | -0.34 a +0.50 | 24 |
| cripto_cierre | todas | 1195 | 98.69c | 97.91% | -0.78 pts | -1.58 a +0.03 | 25 |
| cripto_cierre | tocadas | 1089 | 98.73c | 97.70% | -1.03 pts | -1.90 a -0.15 | 25 |
| deportes_previo | todas | 3640 | 98.04c | 97.54% | -0.50 pts | -1.00 a -0.00 | 92 |
| deportes_previo | tocadas | 3554 | 98.07c | 97.48% | -0.59 pts | -1.10 a -0.08 | 92 |
| otros_cierre | todas | 1171 | 99.00c | 97.18% | -1.82 pts | -2.76 a -0.87 | 33 |
| otros_cierre | tocadas | 1098 | 98.96c | 96.99% | -1.97 pts | -2.97 a -0.96 | 33 |
| post_fin_90_97 | todas | 83 | 94.36c | 96.39% | +2.03 pts | -2.00 a +6.05 | 3 |
| post_fin_90_97 | tocadas | 66 | 94.43c | 95.45% | +1.03 pts | -4.01 a +6.07 | 3 |
| TOTAL | todas | 8539 | 98.46c | 97.96% | -0.50 pts | -0.80 a -0.20 | 177 |
| TOTAL | tocadas | 8071 | 98.47c | 97.84% | -0.64 pts | -0.95 a -0.32 | 177 |

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

Aun no hay veredicto: van 152 operaciones cerradas en 8.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
