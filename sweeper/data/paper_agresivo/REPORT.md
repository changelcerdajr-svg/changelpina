# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.3 de 28 | corridas: 41
- Capital inicial: $1,000.00 | valor actual: $832.42 | P&L: $-167.58 (-16.76%)
- Efectivo libre: $0.02 | en ordenes abiertas: $281.59 (6) | en posiciones: $553.55 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 92 colocadas, 40 llenadas, 33 tocadas sin llenarse (sorteo 30%), 13 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 12 | 99.07c | 100.00% | 75.7-100.0% | +0.93 pts | $+8.47 | 0.06 |
| deportes_previo | 12 | 97.93c | 83.09% | 55.2-95.3% | -14.83 pts | $-174.43 | 0.74 |
| otros_cierre | 6 | 99.66c | 100.00% | 61.0-100.0% | +0.34 pts | $+0.82 | 0.79 |
| TOTAL | 31 | 98.61c | 91.93% | 79.3-98.2% | -6.68 pts | $-164.83 | 0.52 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 96.8c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 99.1c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 99.8c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $22.72 | 96.1c | 80.8c | deportes_previo |  | Greece vs. Serbia: Neither team to score first? |
| $14.54 | 99.1c | 99.1c | deportes_previo |  | Spread: CA Grau (-2.5) |
| $22.70 | 99.8c | 97.5c | cripto_cierre |  | Amazon (AMZN) Up or Down on November 16? |
| $83.50 | 99.7c | 99.7c | cripto_cierre |  | Google (GOOGL) Up or Down on November 16? |
| $53.36 | 99.9c | 99.9c | otros_cierre |  | Will Apple (AAPL) close above $345 on November 16? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2508 | abiertas: 1970 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 574 | 99.11c | 99.48% | +0.37 pts | -0.21 a +0.96 | 3 |
| clima_cierre | tocadas | 526 | 99.06c | 99.43% | +0.37 pts | -0.27 a +1.00 | 3 |
| cripto_cierre | todas | 429 | 99.09c | 97.20% | -1.88 pts | -3.43 a -0.34 | 12 |
| cripto_cierre | tocadas | 391 | 99.11c | 96.93% | -2.18 pts | -3.86 a -0.49 | 12 |
| deportes_previo | todas | 1143 | 97.99c | 96.76% | -1.22 pts | -2.25 a -0.20 | 37 |
| deportes_previo | tocadas | 1124 | 98.02c | 96.71% | -1.31 pts | -2.35 a -0.27 | 37 |
| otros_cierre | todas | 330 | 99.35c | 99.70% | +0.35 pts | -0.25 a +0.95 | 1 |
| otros_cierre | tocadas | 317 | 99.34c | 99.68% | +0.34 pts | -0.28 a +0.96 | 1 |
| post_fin_90_97 | todas | 32 | 94.20c | 100.00% | +5.80 pts | +5.23 a +6.37 | 0 |
| post_fin_90_97 | tocadas | 26 | 94.33c | 100.00% | +5.67 pts | +5.06 a +6.28 | 0 |
| TOTAL | todas | 2508 | 98.56c | 97.89% | -0.67 pts | -1.23 a -0.12 | 53 |
| TOTAL | tocadas | 2384 | 98.57c | 97.78% | -0.79 pts | -1.38 a -0.20 | 53 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?
- 98.9c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 15?

## Veredicto

Aun no hay veredicto: van 31 operaciones cerradas en 3.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
