# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.0 de 28 | corridas: 59
- Capital inicial: $1,000.00 | valor actual: $843.45 | P&L: $-156.55 (-15.66%)
- Efectivo libre: $4.17 | en ordenes abiertas: $254.06 (3) | en posiciones: $595.34 (10)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 139 colocadas, 63 llenadas, 54 tocadas sin llenarse (sorteo 30%), 19 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 19 | 99.03c | 100.00% | 83.2-100.0% | +0.97 pts | $+12.97 | 0.06 |
| deportes_previo | 19 | 98.15c | 87.15% | 68.6-97.1% | -11.00 pts | $-170.25 | 0.54 |
| otros_cierre | 12 | 99.66c | 100.00% | 75.7-100.0% | +0.34 pts | $+2.39 | 0.55 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 53 | 98.66c | 94.95% | 87.2-99.0% | -3.71 pts | $-146.43 | 0.40 |

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
| $7.62 | 99.7c | 99.2c | deportes_previo |  | Will Singapore win on 2026-11-17? |
| $77.09 | 98.5c | 100.0c | deportes_previo |  | Will Brazil win on 2026-11-17? |
| $84.97 | 99.7c | 92.6c | deportes_previo |  | Singapore leading at halftime? |
| $83.05 | 96.9c | 96.9c | deportes_previo |  | Will Malawi win on 2026-11-17? |
| $84.57 | 99.8c | 97.5c | otros_cierre |  | Will the US national average gas price be less than $3.7900 on November 17? |
| $43.73 | 99.8c | 99.9c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 17? |
| $23.44 | 98.8c | 98.9c | cripto_cierre |  | Will the price of Bitcoin be between $68,000 and $70,000 on November 17? |
| $39.99 | 98.4c | 99.2c | cripto_cierre |  | Will the price of Ethereum be above $1,700 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3234 | abiertas: 1901 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 797 | 99.05c | 99.37% | +0.32 pts | -0.22 a +0.87 | 5 |
| clima_cierre | tocadas | 724 | 99.02c | 99.31% | +0.29 pts | -0.31 a +0.89 | 5 |
| cripto_cierre | todas | 496 | 98.99c | 97.58% | -1.41 pts | -2.75 a -0.08 | 12 |
| cripto_cierre | tocadas | 453 | 99.03c | 97.35% | -1.68 pts | -3.14 a -0.22 | 12 |
| deportes_previo | todas | 1518 | 98.07c | 96.84% | -1.23 pts | -2.11 a -0.36 | 48 |
| deportes_previo | tocadas | 1489 | 98.10c | 96.78% | -1.33 pts | -2.22 a -0.43 | 48 |
| otros_cierre | todas | 388 | 99.24c | 99.48% | +0.24 pts | -0.47 a +0.95 | 2 |
| otros_cierre | tocadas | 372 | 99.24c | 99.46% | +0.22 pts | -0.52 a +0.96 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 3234 | 98.55c | 97.93% | -0.62 pts | -1.11 a -0.14 | 67 |
| TOTAL | tocadas | 3067 | 98.56c | 97.82% | -0.74 pts | -1.26 a -0.23 | 67 |

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

Aun no hay veredicto: van 53 operaciones cerradas en 4.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
