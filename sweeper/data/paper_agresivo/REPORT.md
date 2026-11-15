# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.2 de 28 | corridas: 11
- Capital inicial: $1,000.00 | valor actual: $912.30 | P&L: $-87.70 (-8.77%)
- Efectivo libre: $2.88 | en ordenes abiertas: $727.75 (9) | en posiciones: $182.09 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 42 colocadas, 17 llenadas, 13 tocadas sin llenarse (sorteo 30%), 3 expiradas

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
| $91.23 | 97.8c | 97.8c | deportes_previo |  | Spread: CE Sabadell FC (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1362 | abiertas: 1762 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 321 | 99.05c | 99.38% | +0.33 pts | -0.52 a +1.18 | 2 |
| clima_cierre | tocadas | 292 | 98.99c | 99.32% | +0.32 pts | -0.61 a +1.26 | 2 |
| cripto_cierre | todas | 174 | 98.91c | 96.55% | -2.36 pts | -5.03 a +0.32 | 6 |
| cripto_cierre | tocadas | 155 | 98.96c | 96.13% | -2.83 pts | -5.83 a +0.16 | 6 |
| deportes_previo | todas | 584 | 97.98c | 95.38% | -2.61 pts | -4.30 a -0.91 | 27 |
| deportes_previo | tocadas | 571 | 98.03c | 95.27% | -2.76 pts | -4.49 a -1.02 | 27 |
| otros_cierre | todas | 275 | 99.44c | 99.64% | +0.20 pts | -0.51 a +0.92 | 1 |
| otros_cierre | tocadas | 265 | 99.43c | 99.62% | +0.19 pts | -0.55 a +0.94 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1362 | 98.63c | 97.36% | -1.27 pts | -2.11 a -0.43 | 36 |
| TOTAL | tocadas | 1291 | 98.63c | 97.21% | -1.42 pts | -2.31 a -0.53 | 36 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?
- 98.7c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 98.7c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Chongqing be 22°C on November 14?

## Veredicto

Aun no hay veredicto: van 15 operaciones cerradas en 2.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
