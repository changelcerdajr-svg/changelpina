# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.2 de 28 | corridas: 64
- Capital inicial: $1,000.00 | valor actual: $855.26 | P&L: $-144.74 (-14.47%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $617.32 (8) | en posiciones: $241.55 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 151 colocadas, 65 llenadas, 59 tocadas sin llenarse (sorteo 30%), 19 expiradas

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

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3537 | abiertas: 1854 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 902 | 99.03c | 99.22% | +0.19 pts | -0.38 a +0.76 | 7 |
| clima_cierre | tocadas | 826 | 99.01c | 99.15% | +0.14 pts | -0.48 a +0.77 | 7 |
| cripto_cierre | todas | 581 | 98.97c | 97.93% | -1.03 pts | -2.18 a +0.11 | 12 |
| cripto_cierre | tocadas | 534 | 99.00c | 97.75% | -1.25 pts | -2.49 a -0.00 | 12 |
| deportes_previo | todas | 1574 | 98.06c | 96.95% | -1.11 pts | -1.96 a -0.27 | 48 |
| deportes_previo | tocadas | 1542 | 98.10c | 96.89% | -1.21 pts | -2.08 a -0.35 | 48 |
| otros_cierre | todas | 442 | 99.28c | 99.32% | +0.04 pts | -0.73 a +0.80 | 3 |
| otros_cierre | tocadas | 397 | 99.25c | 99.24% | -0.00 pts | -0.85 a +0.85 | 3 |
| post_fin_90_97 | todas | 38 | 94.13c | 97.37% | +3.24 pts | -1.94 a +8.41 | 1 |
| post_fin_90_97 | tocadas | 31 | 94.23c | 96.77% | +2.54 pts | -3.79 a +8.87 | 1 |
| TOTAL | todas | 3537 | 98.57c | 97.99% | -0.58 pts | -1.04 a -0.12 | 71 |
| TOTAL | tocadas | 3330 | 98.57c | 97.87% | -0.70 pts | -1.19 a -0.22 | 71 |

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

Aun no hay veredicto: van 61 operaciones cerradas en 4.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
