# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.4 de 28 | corridas: 17
- Capital inicial: $1,000.00 | valor actual: $898.38 | P&L: $-101.62 (-10.16%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $732.54 (10) | en posiciones: $182.22 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 45 colocadas, 18 llenadas, 14 tocadas sin llenarse (sorteo 30%), 3 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 4 | 99.52c | 100.00% | 51.0-100.0% | +0.48 pts | $+1.90 | 0.08 |
| deportes_previo | 7 | 97.99c | 85.25% | 48.7-97.4% | -12.74 pts | $-87.90 | 1.08 |
| otros_cierre | 4 | 99.79c | 100.00% | 51.0-100.0% | +0.21 pts | $+0.46 | 0.93 |
| TOTAL | 16 | 98.83c | 92.81% | 71.7-98.9% | -6.02 pts | $-85.24 | 0.84 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 99.2c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.36 | 98.4c | 81.2c | deportes_previo |  | Spread: Danubio FC (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1483 | abiertas: 1945 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 348 | 99.08c | 99.43% | +0.34 pts | -0.44 a +1.13 | 2 |
| clima_cierre | tocadas | 318 | 99.03c | 99.37% | +0.34 pts | -0.52 a +1.20 | 2 |
| cripto_cierre | todas | 246 | 99.06c | 96.34% | -2.71 pts | -5.03 a -0.40 | 9 |
| cripto_cierre | tocadas | 221 | 99.09c | 95.93% | -3.16 pts | -5.73 a -0.59 | 9 |
| deportes_previo | todas | 606 | 97.96c | 95.54% | -2.41 pts | -4.05 a -0.77 | 27 |
| deportes_previo | tocadas | 591 | 98.01c | 95.43% | -2.58 pts | -4.26 a -0.90 | 27 |
| otros_cierre | todas | 275 | 99.44c | 99.64% | +0.20 pts | -0.51 a +0.92 | 1 |
| otros_cierre | tocadas | 265 | 99.43c | 99.62% | +0.19 pts | -0.55 a +0.94 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1483 | 98.66c | 97.37% | -1.29 pts | -2.10 a -0.48 | 39 |
| TOTAL | tocadas | 1403 | 98.66c | 97.22% | -1.44 pts | -2.29 a -0.59 | 39 |

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

Aun no hay veredicto: van 16 operaciones cerradas en 2.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
