# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.1 de 28 | corridas: 61
- Capital inicial: $1,000.00 | valor actual: $851.03 | P&L: $-148.97 (-14.90%)
- Efectivo libre: $0.00 | en ordenes abiertas: $423.79 (5) | en posiciones: $431.23 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 144 colocadas, 64 llenadas, 56 tocadas sin llenarse (sorteo 30%), 19 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 19 | 99.03c | 100.00% | 83.2-100.0% | +0.97 pts | $+12.97 | 0.06 |
| deportes_previo | 22 | 98.25c | 88.47% | 72.2-97.5% | -9.79 pts | $-168.80 | 0.51 |
| otros_cierre | 12 | 99.66c | 100.00% | 75.7-100.0% | +0.34 pts | $+2.39 | 0.55 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 56 | 98.68c | 95.16% | 87.9-99.0% | -3.52 pts | $-144.98 | 0.40 |

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
| $83.05 | 96.9c | 95.6c | deportes_previo |  | Will Malawi win on 2026-11-17? |
| $84.57 | 99.8c | 100.0c | otros_cierre |  | Will the US national average gas price be less than $3.7900 on November 17? |
| $43.73 | 99.8c | 100.0c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 17? |
| $23.44 | 98.8c | 99.8c | cripto_cierre |  | Will the price of Bitcoin be between $68,000 and $70,000 on November 17? |
| $39.99 | 98.4c | 99.2c | cripto_cierre |  | Will the price of Ethereum be above $1,700 on November 17? |
| $5.56 | 99.3c | 99.3c | otros_cierre |  | Will MrBeast's next video get between 68 and 69 million views on day 3? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3289 | abiertas: 1928 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 797 | 99.05c | 99.37% | +0.32 pts | -0.22 a +0.87 | 5 |
| clima_cierre | tocadas | 724 | 99.02c | 99.31% | +0.29 pts | -0.31 a +0.89 | 5 |
| cripto_cierre | todas | 504 | 98.95c | 97.62% | -1.33 pts | -2.65 a -0.02 | 12 |
| cripto_cierre | tocadas | 460 | 98.99c | 97.39% | -1.60 pts | -3.04 a -0.16 | 12 |
| deportes_previo | todas | 1549 | 98.07c | 96.90% | -1.17 pts | -2.03 a -0.31 | 48 |
| deportes_previo | tocadas | 1518 | 98.10c | 96.84% | -1.27 pts | -2.14 a -0.39 | 48 |
| otros_cierre | todas | 402 | 99.25c | 99.25% | -0.00 pts | -0.84 a +0.84 | 3 |
| otros_cierre | tocadas | 386 | 99.25c | 99.22% | -0.03 pts | -0.91 a +0.84 | 3 |
| post_fin_90_97 | todas | 37 | 94.16c | 97.30% | +3.14 pts | -2.18 a +8.45 | 1 |
| post_fin_90_97 | tocadas | 30 | 94.27c | 96.67% | +2.39 pts | -4.15 a +8.93 | 1 |
| TOTAL | todas | 3289 | 98.54c | 97.90% | -0.64 pts | -1.13 a -0.15 | 69 |
| TOTAL | tocadas | 3118 | 98.55c | 97.79% | -0.77 pts | -1.28 a -0.25 | 69 |

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

Aun no hay veredicto: van 56 operaciones cerradas en 4.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
