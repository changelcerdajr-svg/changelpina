# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.3 de 28 | corridas: 16
- Capital inicial: $1,000.00 | valor actual: $897.64 | P&L: $-102.36 (-10.24%)
- Efectivo libre: $2.75 | en ordenes abiertas: $636.52 (8) | en posiciones: $273.45 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 43 colocadas, 18 llenadas, 14 tocadas sin llenarse (sorteo 30%), 3 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 4 | 99.52c | 100.00% | 51.0-100.0% | +0.48 pts | $+1.90 | 0.08 |
| deportes_previo | 6 | 98.02c | 82.93% | 43.6-97.0% | -15.09 pts | $-89.95 | 1.22 |
| otros_cierre | 4 | 99.79c | 100.00% | 51.0-100.0% | +0.21 pts | $+0.46 | 0.93 |
| TOTAL | 15 | 98.90c | 92.30% | 70.2-98.8% | -6.60 pts | $-87.29 | 0.88 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 99.2c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.23 | 97.8c | 99.2c | deportes_previo |  | Spread: CE Sabadell FC (-2.5) |
| $91.36 | 98.4c | 81.2c | deportes_previo |  | Spread: Danubio FC (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1453 | abiertas: 1944 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 333 | 99.06c | 99.40% | +0.34 pts | -0.48 a +1.16 | 2 |
| clima_cierre | tocadas | 303 | 99.01c | 99.34% | +0.33 pts | -0.57 a +1.23 | 2 |
| cripto_cierre | todas | 246 | 99.06c | 96.34% | -2.71 pts | -5.03 a -0.40 | 9 |
| cripto_cierre | tocadas | 221 | 99.09c | 95.93% | -3.16 pts | -5.73 a -0.59 | 9 |
| deportes_previo | todas | 591 | 97.97c | 95.43% | -2.54 pts | -4.22 a -0.86 | 27 |
| deportes_previo | tocadas | 576 | 98.03c | 95.31% | -2.71 pts | -4.44 a -0.99 | 27 |
| otros_cierre | todas | 275 | 99.44c | 99.64% | +0.20 pts | -0.51 a +0.92 | 1 |
| otros_cierre | tocadas | 265 | 99.43c | 99.62% | +0.19 pts | -0.55 a +0.94 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1453 | 98.66c | 97.32% | -1.35 pts | -2.17 a -0.52 | 39 |
| TOTAL | tocadas | 1373 | 98.67c | 97.16% | -1.51 pts | -2.38 a -0.64 | 39 |

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

Aun no hay veredicto: van 15 operaciones cerradas en 2.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
