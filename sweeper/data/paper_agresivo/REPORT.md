# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 8.1 de 28 | corridas: 170
- Capital inicial: $1,000.00 | valor actual: $959.98 | P&L: $-40.02 (-4.00%)
- Efectivo libre: $1.86 | en ordenes abiertas: $148.59 (2) | en posiciones: $815.32 (12)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 365 colocadas, 164 llenadas, 161 tocadas sin llenarse (sorteo 30%), 38 expiradas

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
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $6.92 | 93.9c | 98.3c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 66-67°F on November 21? |
| $93.94 | 99.5c | 99.5c | deportes_previo |  | NEC vs. PSV: Neither team to score first? |
| $95.35 | 98.4c | 98.5c | deportes_previo |  | Spread: OGC Nice (-2.5) |
| $95.89 | 97.4c | 97.4c | deportes_previo |  | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $94.72 | 99.6c | 99.2c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $17.05 | 99.6c | 99.7c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 21, 2026? |
| $94.88 | 99.8c | 99.5c | clima_cierre |  | Will the next hurricane form between November 17 and November 21, 2026? |
| $93.98 | 98.5c | 98.5c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $8.19 | 97.9c | 95.5c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 8354 | abiertas: 2601 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2371 | 98.85c | 99.03% | +0.18 pts | -0.21 a +0.58 | 23 |
| clima_cierre | tocadas | 2188 | 98.87c | 98.95% | +0.08 pts | -0.34 a +0.51 | 23 |
| cripto_cierre | todas | 1189 | 98.69c | 97.90% | -0.79 pts | -1.60 a +0.02 | 25 |
| cripto_cierre | tocadas | 1083 | 98.73c | 97.69% | -1.04 pts | -1.93 a -0.16 | 25 |
| deportes_previo | todas | 3548 | 98.05c | 97.48% | -0.57 pts | -1.08 a -0.06 | 92 |
| deportes_previo | tocadas | 3465 | 98.08c | 97.42% | -0.66 pts | -1.18 a -0.14 | 92 |
| otros_cierre | todas | 1164 | 98.99c | 97.16% | -1.83 pts | -2.78 a -0.88 | 33 |
| otros_cierre | tocadas | 1091 | 98.96c | 96.98% | -1.98 pts | -2.99 a -0.97 | 33 |
| post_fin_90_97 | todas | 82 | 94.33c | 96.34% | +2.01 pts | -2.06 a +6.09 | 3 |
| post_fin_90_97 | tocadas | 65 | 94.39c | 95.38% | +1.00 pts | -4.12 a +6.11 | 3 |
| TOTAL | todas | 8354 | 98.46c | 97.92% | -0.54 pts | -0.84 a -0.23 | 176 |
| TOTAL | tocadas | 7892 | 98.48c | 97.80% | -0.68 pts | -1.00 a -0.36 | 176 |

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

Aun no hay veredicto: van 152 operaciones cerradas en 8.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
