# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 12.0 de 28 | corridas: 274
- Capital inicial: $1,000.00 | valor actual: $956.29 | P&L: $-43.71 (-4.37%)
- Efectivo libre: $0.00 | en ordenes abiertas: $540.27 (7) | en posiciones: $433.39 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 548 colocadas, 249 llenadas, 235 tocadas sin llenarse (sorteo 30%), 57 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 70 | 98.86c | 100.00% | 94.8-100.0% | +1.14 pts | $+54.28 | 0.18 |
| deportes_previo | 122 | 98.03c | 96.96% | 93.0-99.2% | -1.07 pts | $-105.40 | 0.25 |
| otros_cierre | 43 | 99.63c | 100.00% | 91.8-100.0% | +0.37 pts | $+11.19 | 0.33 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 243 | 98.51c | 98.38% | 96.4-99.6% | -0.13 pts | $-26.34 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.7c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.72 | 98.2c | 99.1c | deportes_previo |  | Spread: Tokushima Vortis (-2.5) |
| $94.27 | 97.0c | 97.0c | deportes_previo |  | Spread: FK Kryvbas Kryvyi Rih (-1.5) |
| $35.99 | 99.4c | 98.7c | cripto_cierre |  | Will the price of Bitcoin be less than $54,000 on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 14353 | abiertas: 2078 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3900 | 98.80c | 98.85% | +0.05 pts | -0.28 a +0.38 | 45 |
| clima_cierre | tocadas | 3622 | 98.82c | 98.76% | -0.06 pts | -0.42 a +0.29 | 45 |
| cripto_cierre | todas | 1812 | 98.65c | 98.12% | -0.52 pts | -1.14 a +0.09 | 34 |
| cripto_cierre | tocadas | 1654 | 98.69c | 97.94% | -0.75 pts | -1.42 a -0.07 | 34 |
| deportes_previo | todas | 6757 | 98.05c | 97.36% | -0.69 pts | -1.07 a -0.31 | 181 |
| deportes_previo | tocadas | 6587 | 98.09c | 97.32% | -0.77 pts | -1.15 a -0.38 | 179 |
| otros_cierre | todas | 1631 | 98.98c | 97.55% | -1.44 pts | -2.18 a -0.69 | 40 |
| otros_cierre | tocadas | 1487 | 98.93c | 97.31% | -1.62 pts | -2.44 a -0.81 | 40 |
| post_fin_90_97 | todas | 253 | 94.03c | 93.68% | -0.35 pts | -3.32 a +2.62 | 16 |
| post_fin_90_97 | tocadas | 215 | 94.14c | 92.56% | -1.58 pts | -5.05 a +1.89 | 16 |
| TOTAL | todas | 14353 | 98.36c | 97.82% | -0.55 pts | -0.78 a -0.31 | 316 |
| TOTAL | tocadas | 13565 | 98.39c | 97.70% | -0.68 pts | -0.93 a -0.43 | 314 |

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

Aun no hay veredicto: van 243 operaciones cerradas en 12.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
