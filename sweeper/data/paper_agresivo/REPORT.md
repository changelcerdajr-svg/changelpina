# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.5 de 28 | corridas: 21
- Capital inicial: $1,000.00 | valor actual: $917.21 | P&L: $-82.79 (-8.28%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $630.08 (8) | en posiciones: $288.44 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 59 colocadas, 24 llenadas, 19 tocadas sin llenarse (sorteo 30%), 8 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 7 | 99.28c | 100.00% | 64.6-100.0% | +0.72 pts | $+4.17 | 0.06 |
| deportes_previo | 8 | 98.04c | 87.02% | 52.9-97.8% | -11.02 pts | $-86.41 | 0.97 |
| otros_cierre | 4 | 99.79c | 100.00% | 51.0-100.0% | +0.21 pts | $+0.46 | 0.93 |
| TOTAL | 20 | 98.80c | 94.01% | 76.4-99.1% | -4.79 pts | $-81.48 | 0.69 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 99.2c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.58 | 98.6c | 97.8c | deportes_previo |  | Spread: Deportes Quindio (-3.5) |
| $14.23 | 97.7c | 96.9c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 99.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1543 | abiertas: 1992 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 396 | 99.09c | 99.24% | +0.15 pts | -0.70 a +0.99 | 3 |
| clima_cierre | tocadas | 364 | 99.05c | 99.18% | +0.13 pts | -0.79 a +1.05 | 3 |
| cripto_cierre | todas | 246 | 99.06c | 96.34% | -2.71 pts | -5.03 a -0.40 | 9 |
| cripto_cierre | tocadas | 221 | 99.09c | 95.93% | -3.16 pts | -5.73 a -0.59 | 9 |
| deportes_previo | todas | 618 | 97.96c | 95.63% | -2.33 pts | -3.93 a -0.72 | 27 |
| deportes_previo | tocadas | 603 | 98.01c | 95.52% | -2.49 pts | -4.14 a -0.84 | 27 |
| otros_cierre | todas | 275 | 99.44c | 99.64% | +0.20 pts | -0.51 a +0.92 | 1 |
| otros_cierre | tocadas | 265 | 99.43c | 99.62% | +0.19 pts | -0.55 a +0.94 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1543 | 98.67c | 97.41% | -1.26 pts | -2.05 a -0.48 | 40 |
| TOTAL | tocadas | 1461 | 98.67c | 97.26% | -1.41 pts | -2.24 a -0.58 | 40 |

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

Aun no hay veredicto: van 20 operaciones cerradas en 2.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
