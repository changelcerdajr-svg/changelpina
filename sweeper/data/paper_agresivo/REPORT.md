# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.0 de 28 | corridas: 300
- Capital inicial: $1,000.00 | valor actual: $989.64 | P&L: $-10.36 (-1.04%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $676.07 (8) | en posiciones: $326.10 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 604 colocadas, 271 llenadas, 260 tocadas sin llenarse (sorteo 30%), 65 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 77 | 98.82c | 100.00% | 95.2-100.0% | +1.18 pts | $+63.13 | 0.18 |
| deportes_previo | 136 | 98.07c | 97.29% | 93.7-99.2% | -0.78 pts | $-86.81 | 0.25 |
| otros_cierre | 45 | 99.61c | 100.00% | 92.1-100.0% | +0.39 pts | $+12.25 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 266 | 98.51c | 98.53% | 96.7-99.6% | +0.02 pts | $+2.17 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 88.5c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $16.29 | 99.9c | 98.2c | otros_cierre |  | Will the US national average gas price be less than $3.5700 on November 26? |
| $95.40 | 97.3c | 97.3c | deportes_previo |  | Spread: Mjällby AIF (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 15563 | abiertas: 2355 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4279 | 98.80c | 98.90% | +0.10 pts | -0.21 a +0.41 | 47 |
| clima_cierre | tocadas | 3985 | 98.82c | 98.82% | -0.00 pts | -0.34 a +0.33 | 47 |
| cripto_cierre | todas | 1972 | 98.63c | 98.23% | -0.41 pts | -0.98 a +0.17 | 35 |
| cripto_cierre | tocadas | 1799 | 98.68c | 98.05% | -0.63 pts | -1.26 a +0.00 | 35 |
| deportes_previo | todas | 7352 | 98.05c | 97.44% | -0.61 pts | -0.97 a -0.26 | 193 |
| deportes_previo | tocadas | 7163 | 98.09c | 97.40% | -0.69 pts | -1.06 a -0.33 | 191 |
| otros_cierre | todas | 1695 | 98.99c | 97.64% | -1.35 pts | -2.07 a -0.64 | 40 |
| otros_cierre | tocadas | 1543 | 98.94c | 97.41% | -1.54 pts | -2.33 a -0.75 | 40 |
| post_fin_90_97 | todas | 265 | 94.04c | 93.96% | -0.07 pts | -2.91 a +2.76 | 16 |
| post_fin_90_97 | tocadas | 225 | 94.15c | 92.89% | -1.26 pts | -4.57 a +2.06 | 16 |
| TOTAL | todas | 15563 | 98.36c | 97.90% | -0.46 pts | -0.68 a -0.24 | 331 |
| TOTAL | tocadas | 14715 | 98.39c | 97.79% | -0.60 pts | -0.83 a -0.36 | 329 |

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

Aun no hay veredicto: van 266 operaciones cerradas en 13.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
