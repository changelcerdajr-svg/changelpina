# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.6 de 28 | corridas: 211
- Capital inicial: $1,000.00 | valor actual: $897.44 | P&L: $-102.56 (-10.26%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $350.85 (6) | en posiciones: $556.82 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 428 colocadas, 192 llenadas, 184 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 55 | 98.82c | 100.00% | 93.5-100.0% | +1.18 pts | $+43.25 | 0.17 |
| deportes_previo | 89 | 98.02c | 95.86% | 90.6-98.8% | -2.15 pts | $-155.29 | 0.27 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 184 | 98.51c | 97.85% | 95.3-99.4% | -0.66 pts | $-92.33 | 0.28 |

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
| $35.36 | 99.8c | 97.2c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $26.13 | 95.0c | 100.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $89.53 | 99.4c | 99.4c | deportes_previo |  | Spread: Aurora FC (-2.5) |
| $89.56 | 99.7c | 99.5c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 22, 2026? |
| $54.02 | 99.0c | 99.0c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 22, 2026? |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 10947 | abiertas: 2526 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2996 | 98.83c | 99.03% | +0.20 pts | -0.15 a +0.55 | 29 |
| clima_cierre | tocadas | 2779 | 98.85c | 98.96% | +0.10 pts | -0.27 a +0.48 | 29 |
| cripto_cierre | todas | 1408 | 98.70c | 98.08% | -0.62 pts | -1.33 a +0.09 | 27 |
| cripto_cierre | tocadas | 1277 | 98.75c | 97.89% | -0.87 pts | -1.65 a -0.09 | 27 |
| deportes_previo | todas | 5136 | 98.01c | 97.42% | -0.59 pts | -1.02 a -0.16 | 135 |
| deportes_previo | tocadas | 5006 | 98.05c | 97.39% | -0.66 pts | -1.09 a -0.22 | 133 |
| otros_cierre | todas | 1220 | 99.00c | 97.21% | -1.78 pts | -2.70 a -0.87 | 34 |
| otros_cierre | tocadas | 1138 | 98.96c | 97.01% | -1.95 pts | -2.93 a -0.97 | 34 |
| post_fin_90_97 | todas | 187 | 94.12c | 93.05% | -1.07 pts | -4.67 a +2.52 | 13 |
| post_fin_90_97 | tocadas | 159 | 94.19c | 91.82% | -2.36 pts | -6.56 a +1.83 | 13 |
| TOTAL | todas | 10947 | 98.37c | 97.85% | -0.52 pts | -0.79 a -0.25 | 238 |
| TOTAL | tocadas | 10359 | 98.39c | 97.75% | -0.65 pts | -0.93 a -0.36 | 236 |

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

Aun no hay veredicto: van 184 operaciones cerradas en 9.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
