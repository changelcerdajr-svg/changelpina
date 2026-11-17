# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.8 de 28 | corridas: 53
- Capital inicial: $1,000.00 | valor actual: $850.00 | P&L: $-150.00 (-15.00%)
- Efectivo libre: $0.00 | en ordenes abiertas: $323.21 (6) | en posiciones: $529.46 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 133 colocadas, 60 llenadas, 49 tocadas sin llenarse (sorteo 30%), 18 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 19 | 99.03c | 100.00% | 83.2-100.0% | +0.97 pts | $+12.97 | 0.06 |
| deportes_previo | 18 | 98.11c | 86.41% | 67.2-96.9% | -11.69 pts | $-171.14 | 0.55 |
| otros_cierre | 12 | 99.66c | 100.00% | 75.7-100.0% | +0.34 pts | $+2.39 | 0.55 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 52 | 98.65c | 94.84% | 87.0-98.9% | -3.82 pts | $-147.33 | 0.40 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.7c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $80.59 | 98.9c | 100.0c | deportes_previo |  | Tahiti vs. Cook Islands: O/U 0.5 |
| $7.62 | 99.7c | 99.7c | deportes_previo |  | Will Singapore win on 2026-11-17? |
| $77.09 | 98.5c | 99.0c | deportes_previo |  | Will Brazil win on 2026-11-17? |
| $84.97 | 99.7c | 99.7c | deportes_previo |  | Singapore leading at halftime? |
| $84.57 | 99.8c | 99.6c | otros_cierre |  | Will the US national average gas price be less than $3.7900 on November 17? |
| $43.73 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3121 | abiertas: 1771 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 770 | 99.06c | 99.35% | +0.29 pts | -0.27 a +0.86 | 5 |
| clima_cierre | tocadas | 698 | 99.03c | 99.28% | +0.26 pts | -0.37 a +0.88 | 5 |
| cripto_cierre | todas | 488 | 99.01c | 97.54% | -1.47 pts | -2.83 a -0.11 | 12 |
| cripto_cierre | tocadas | 448 | 99.04c | 97.32% | -1.72 pts | -3.20 a -0.24 | 12 |
| deportes_previo | todas | 1447 | 98.09c | 96.75% | -1.34 pts | -2.25 a -0.43 | 47 |
| deportes_previo | tocadas | 1421 | 98.12c | 96.69% | -1.42 pts | -2.35 a -0.50 | 47 |
| otros_cierre | todas | 381 | 99.25c | 99.48% | +0.22 pts | -0.50 a +0.95 | 2 |
| otros_cierre | tocadas | 365 | 99.25c | 99.45% | +0.20 pts | -0.55 a +0.96 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 3121 | 98.57c | 97.89% | -0.68 pts | -1.19 a -0.18 | 66 |
| TOTAL | tocadas | 2961 | 98.57c | 97.77% | -0.80 pts | -1.33 a -0.28 | 66 |

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
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)

## Veredicto

Aun no hay veredicto: van 52 operaciones cerradas en 3.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
