# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.3 de 28 | corridas: 66
- Capital inicial: $1,000.00 | valor actual: $854.91 | P&L: $-145.09 (-14.51%)
- Efectivo libre: $0.00 | en ordenes abiertas: $360.74 (5) | en posiciones: $498.13 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 155 colocadas, 68 llenadas, 63 tocadas sin llenarse (sorteo 30%), 19 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 22 | 99.03c | 100.00% | 85.1-100.0% | +0.97 pts | $+13.99 | 0.10 |
| deportes_previo | 23 | 98.19c | 89.02% | 73.2-97.6% | -9.17 pts | $-166.14 | 0.50 |
| otros_cierre | 13 | 99.68c | 100.00% | 77.2-100.0% | +0.32 pts | $+2.56 | 0.54 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 61 | 98.68c | 95.48% | 88.8-99.1% | -3.20 pts | $-141.13 | 0.39 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $85.10 | 98.3c | 98.3c | deportes_previo |  | Spread: Kuwait (-2.5) |
| $5.56 | 99.3c | 99.3c | otros_cierre |  | Will MrBeast's next video get between 68 and 69 million views on day 3? |
| $85.53 | 97.2c | 97.2c | deportes_previo |  | Denmark vs. Norway: Neither team to score first? |
| $85.53 | 98.8c | 98.7c | otros_cierre |  | Will Apple (AAPL) close above $355 on November 17? |
| $85.53 | 99.8c | 99.5c | otros_cierre |  | Will Microsoft (MSFT) close above $540 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3623 | abiertas: 1862 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 914 | 99.03c | 99.23% | +0.21 pts | -0.35 a +0.77 | 7 |
| clima_cierre | tocadas | 838 | 99.00c | 99.16% | +0.17 pts | -0.45 a +0.78 | 7 |
| cripto_cierre | todas | 600 | 98.97c | 98.00% | -0.97 pts | -2.08 a +0.14 | 12 |
| cripto_cierre | tocadas | 553 | 99.00c | 97.83% | -1.17 pts | -2.37 a +0.03 | 12 |
| deportes_previo | todas | 1617 | 98.06c | 97.03% | -1.03 pts | -1.86 a -0.21 | 48 |
| deportes_previo | tocadas | 1584 | 98.10c | 96.97% | -1.13 pts | -1.97 a -0.29 | 48 |
| otros_cierre | todas | 452 | 99.28c | 99.34% | +0.05 pts | -0.69 a +0.80 | 3 |
| otros_cierre | tocadas | 407 | 99.25c | 99.26% | +0.02 pts | -0.81 a +0.85 | 3 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 3623 | 98.57c | 98.04% | -0.53 pts | -0.97 a -0.08 | 71 |
| TOTAL | tocadas | 3415 | 98.57c | 97.92% | -0.65 pts | -1.12 a -0.17 | 71 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 99.4c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Austin be between 62-63°F on November 16?
- 99.2c -> pago 0.0 | otros_cierre | tocada | Will Home Depot (HD) Q3 comparable sales growth be from 2% to under 2.25%?

## Veredicto

Aun no hay veredicto: van 61 operaciones cerradas en 4.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
