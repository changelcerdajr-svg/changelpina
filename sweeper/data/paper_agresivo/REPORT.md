# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 12.8 de 28 | corridas: 293
- Capital inicial: $1,000.00 | valor actual: $977.58 | P&L: $-22.42 (-2.24%)
- Efectivo libre: $4.21 | en ordenes abiertas: $399.30 (5) | en posiciones: $590.47 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 590 colocadas, 268 llenadas, 255 tocadas sin llenarse (sorteo 30%), 62 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 76 | 98.84c | 100.00% | 95.2-100.0% | +1.16 pts | $+61.04 | 0.18 |
| deportes_previo | 132 | 98.06c | 97.19% | 93.5-99.2% | -0.87 pts | $-92.91 | 0.25 |
| otros_cierre | 45 | 99.61c | 100.00% | 92.1-100.0% | +0.39 pts | $+12.25 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 261 | 98.52c | 98.49% | 96.7-99.6% | -0.02 pts | $-6.03 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 85.4c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $96.90 | 97.8c | 96.5c | deportes_previo |  | Spread: Persita Tangerang (-2.5) |
| $92.23 | 97.2c | 97.2c | deportes_previo |  | Spread: Borneo Samarinda (-3.5) |
| $97.47 | 98.9c | 98.9c | deportes_previo |  | Spread: Phnom Penh Crown FC (-2.5) |
| $89.45 | 99.8c | 99.8c | deportes_previo |  | Spread: Phnom Penh Crown FC (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 15476 | abiertas: 2096 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4248 | 98.80c | 98.89% | +0.09 pts | -0.22 a +0.41 | 47 |
| clima_cierre | tocadas | 3956 | 98.82c | 98.81% | -0.01 pts | -0.35 a +0.32 | 47 |
| cripto_cierre | todas | 1963 | 98.64c | 98.22% | -0.42 pts | -1.00 a +0.16 | 35 |
| cripto_cierre | tocadas | 1795 | 98.68c | 98.05% | -0.63 pts | -1.27 a -0.00 | 35 |
| deportes_previo | todas | 7308 | 98.05c | 97.43% | -0.62 pts | -0.98 a -0.26 | 192 |
| deportes_previo | tocadas | 7122 | 98.09c | 97.40% | -0.70 pts | -1.06 a -0.33 | 190 |
| otros_cierre | todas | 1692 | 99.00c | 97.64% | -1.36 pts | -2.08 a -0.64 | 40 |
| otros_cierre | tocadas | 1540 | 98.95c | 97.40% | -1.55 pts | -2.34 a -0.76 | 40 |
| post_fin_90_97 | todas | 265 | 94.04c | 93.96% | -0.07 pts | -2.91 a +2.76 | 16 |
| post_fin_90_97 | tocadas | 225 | 94.15c | 92.89% | -1.26 pts | -4.57 a +2.06 | 16 |
| TOTAL | todas | 15476 | 98.37c | 97.90% | -0.47 pts | -0.69 a -0.25 | 330 |
| TOTAL | tocadas | 14638 | 98.39c | 97.79% | -0.60 pts | -0.84 a -0.37 | 328 |

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

Aun no hay veredicto: van 261 operaciones cerradas en 12.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
