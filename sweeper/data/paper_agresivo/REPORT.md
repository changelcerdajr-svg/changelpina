# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.7 de 28 | corridas: 27
- Capital inicial: $1,000.00 | valor actual: $917.16 | P&L: $-82.84 (-8.28%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $533.96 (7) | en posiciones: $387.63 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 71 colocadas, 29 llenadas, 24 tocadas sin llenarse (sorteo 30%), 11 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 10 | 99.07c | 100.00% | 72.2-100.0% | +0.93 pts | $+7.24 | 0.07 |
| deportes_previo | 8 | 98.04c | 87.02% | 52.9-97.8% | -11.02 pts | $-86.41 | 0.97 |
| otros_cierre | 4 | 99.79c | 100.00% | 51.0-100.0% | +0.21 pts | $+0.46 | 0.93 |
| TOTAL | 23 | 98.76c | 94.63% | 79.0-99.2% | -4.13 pts | $-78.42 | 0.61 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 99.2c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 95.5c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $91.58 | 98.6c | 97.8c | deportes_previo |  | Spread: Deportes Quindio (-3.5) |
| $14.23 | 97.7c | 96.9c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 97.0c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $7.32 | 99.6c | 98.2c | otros_cierre |  | Will GPT Astra 6.1+ be released between November 9 and November 15, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1663 | abiertas: 2121 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 441 | 99.12c | 99.32% | +0.19 pts | -0.56 a +0.95 | 3 |
| clima_cierre | tocadas | 408 | 99.08c | 99.26% | +0.18 pts | -0.64 a +1.00 | 3 |
| cripto_cierre | todas | 295 | 99.10c | 95.93% | -3.17 pts | -5.39 a -0.94 | 12 |
| cripto_cierre | tocadas | 265 | 99.12c | 95.47% | -3.65 pts | -6.12 a -1.18 | 12 |
| deportes_previo | todas | 631 | 97.97c | 95.72% | -2.25 pts | -3.83 a -0.67 | 27 |
| deportes_previo | tocadas | 616 | 98.03c | 95.62% | -2.41 pts | -4.02 a -0.80 | 27 |
| otros_cierre | todas | 288 | 99.40c | 99.65% | +0.25 pts | -0.44 a +0.93 | 1 |
| otros_cierre | tocadas | 276 | 99.40c | 99.64% | +0.24 pts | -0.47 a +0.96 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1663 | 98.71c | 97.41% | -1.30 pts | -2.05 a -0.54 | 43 |
| TOTAL | tocadas | 1573 | 98.71c | 97.27% | -1.44 pts | -2.24 a -0.64 | 43 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?
- 98.9c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 15?
- 98.7c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 98.7c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?

## Veredicto

Aun no hay veredicto: van 23 operaciones cerradas en 2.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
