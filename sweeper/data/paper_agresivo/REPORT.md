# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 14.2 de 28 | corridas: 331
- Capital inicial: $1,000.00 | valor actual: $916.50 | P&L: $-83.50 (-8.35%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $531.46 (7) | en posiciones: $404.24 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 662 colocadas, 302 llenadas, 278 tocadas sin llenarse (sorteo 30%), 75 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 84 | 98.84c | 100.00% | 95.6-100.0% | +1.16 pts | $+66.77 | 0.17 |
| deportes_previo | 155 | 98.03c | 96.75% | 93.6-99.0% | -1.28 pts | $-158.41 | 0.25 |
| otros_cierre | 48 | 99.61c | 100.00% | 92.6-100.0% | +0.39 pts | $+12.91 | 0.32 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 296 | 98.48c | 98.20% | 96.6-99.5% | -0.28 pts | $-64.30 | 0.25 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-99.67 | 97.3c | 0.0 | deportes_previo | Spread: CF Cruz Azul (-3.5) |
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.0c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $45.26 | 98.8c | 98.5c | deportes_previo |  | Spread: Zira FK (-2.5) |
| $91.63 | 97.9c | 97.2c | deportes_previo |  | Spread: PFC Slavia Sofia (-2.5) |
| $52.95 | 97.3c | 97.2c | deportes_previo |  | Spread: FC Lokomotiv 1929 Sofia (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16911 | abiertas: 2912 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4758 | 98.80c | 98.97% | +0.17 pts | -0.12 a +0.46 | 49 |
| clima_cierre | tocadas | 4431 | 98.82c | 98.89% | +0.07 pts | -0.24 a +0.38 | 49 |
| cripto_cierre | todas | 2232 | 98.59c | 98.16% | -0.43 pts | -0.98 a +0.12 | 41 |
| cripto_cierre | tocadas | 2030 | 98.65c | 97.98% | -0.67 pts | -1.28 a -0.07 | 41 |
| deportes_previo | todas | 7902 | 98.04c | 97.39% | -0.66 pts | -1.01 a -0.31 | 211 |
| deportes_previo | tocadas | 7689 | 98.09c | 97.34% | -0.75 pts | -1.10 a -0.39 | 209 |
| otros_cierre | todas | 1738 | 98.99c | 97.58% | -1.41 pts | -2.12 a -0.69 | 42 |
| otros_cierre | tocadas | 1584 | 98.94c | 97.35% | -1.60 pts | -2.38 a -0.81 | 42 |
| post_fin_90_97 | todas | 281 | 94.01c | 93.95% | -0.06 pts | -2.83 a +2.70 | 17 |
| post_fin_90_97 | tocadas | 237 | 94.12c | 92.83% | -1.29 pts | -4.54 a +1.96 | 17 |
| TOTAL | todas | 16911 | 98.36c | 97.90% | -0.46 pts | -0.68 a -0.25 | 360 |
| TOTAL | tocadas | 15971 | 98.39c | 97.79% | -0.60 pts | -0.83 a -0.38 | 358 |

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

Aun no hay veredicto: van 296 operaciones cerradas en 14.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
