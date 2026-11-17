# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.3 de 28 | corridas: 67
- Capital inicial: $1,000.00 | valor actual: $856.39 | P&L: $-143.61 (-14.36%)
- Efectivo libre: $0.94 | en ordenes abiertas: $425.19 (5) | en posiciones: $434.21 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 156 colocadas, 69 llenadas, 63 tocadas sin llenarse (sorteo 30%), 19 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 22 | 99.03c | 100.00% | 85.1-100.0% | +0.97 pts | $+13.99 | 0.10 |
| deportes_previo | 24 | 98.19c | 89.53% | 74.2-97.7% | -8.66 pts | $-164.67 | 0.49 |
| otros_cierre | 13 | 99.68c | 100.00% | 77.2-100.0% | +0.32 pts | $+2.56 | 0.54 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 62 | 98.67c | 95.57% | 89.0-99.1% | -3.10 pts | $-139.66 | 0.39 |

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
| $5.56 | 99.3c | 99.3c | otros_cierre |  | Will MrBeast's next video get between 68 and 69 million views on day 3? |
| $85.53 | 97.2c | 97.2c | deportes_previo |  | Denmark vs. Norway: Neither team to score first? |
| $21.19 | 96.0c | 96.0c | cripto_cierre |  | Dogecoin Up or Down - November 17, 3:00PM-3:05PM ET |
| $85.53 | 98.8c | 98.7c | otros_cierre |  | Will Apple (AAPL) close above $355 on November 17? |
| $85.53 | 99.8c | 99.5c | otros_cierre |  | Will Microsoft (MSFT) close above $540 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3647 | abiertas: 1901 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 916 | 99.02c | 99.24% | +0.21 pts | -0.35 a +0.78 | 7 |
| clima_cierre | tocadas | 838 | 99.00c | 99.16% | +0.17 pts | -0.45 a +0.78 | 7 |
| cripto_cierre | todas | 601 | 98.96c | 98.00% | -0.96 pts | -2.07 a +0.15 | 12 |
| cripto_cierre | tocadas | 554 | 98.99c | 97.83% | -1.16 pts | -2.36 a +0.04 | 12 |
| deportes_previo | todas | 1638 | 98.07c | 97.01% | -1.06 pts | -1.88 a -0.23 | 49 |
| deportes_previo | tocadas | 1603 | 98.10c | 96.94% | -1.16 pts | -2.00 a -0.32 | 49 |
| otros_cierre | todas | 452 | 99.28c | 99.34% | +0.05 pts | -0.69 a +0.80 | 3 |
| otros_cierre | tocadas | 407 | 99.25c | 99.26% | +0.02 pts | -0.81 a +0.85 | 3 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 3647 | 98.56c | 98.03% | -0.54 pts | -0.98 a -0.09 | 72 |
| TOTAL | tocadas | 3435 | 98.56c | 97.90% | -0.66 pts | -1.14 a -0.18 | 72 |

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

Aun no hay veredicto: van 62 operaciones cerradas en 4.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
