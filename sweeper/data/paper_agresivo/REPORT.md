# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.6 de 28 | corridas: 23
- Capital inicial: $1,000.00 | valor actual: $918.18 | P&L: $-81.82 (-8.18%)
- Efectivo libre: $0.00 | en ordenes abiertas: $534.01 (7) | en posiciones: $385.53 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 62 colocadas, 27 llenadas, 20 tocadas sin llenarse (sorteo 30%), 8 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 8 | 99.23c | 100.00% | 67.6-100.0% | +0.77 pts | $+5.19 | 0.06 |
| deportes_previo | 8 | 98.04c | 87.02% | 52.9-97.8% | -11.02 pts | $-86.41 | 0.97 |
| otros_cierre | 4 | 99.79c | 100.00% | 51.0-100.0% | +0.21 pts | $+0.46 | 0.93 |
| TOTAL | 21 | 98.81c | 94.33% | 77.3-99.2% | -4.48 pts | $-80.46 | 0.66 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 99.2c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.58 | 98.6c | 97.8c | deportes_previo |  | Spread: Deportes Quindio (-3.5) |
| $14.23 | 97.7c | 97.0c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 98.2c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $7.32 | 99.6c | 99.6c | otros_cierre |  | Will GPT Astra 6.1+ be released between November 9 and November 15, 2026? |
| $89.77 | 97.8c | 99.4c | cripto_cierre |  | Will Bitcoin dip to $62,000 November 9-15? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1557 | abiertas: 2026 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 410 | 99.11c | 99.27% | +0.16 pts | -0.65 a +0.97 | 3 |
| clima_cierre | tocadas | 377 | 99.06c | 99.20% | +0.14 pts | -0.74 a +1.03 | 3 |
| cripto_cierre | todas | 246 | 99.06c | 96.34% | -2.71 pts | -5.03 a -0.40 | 9 |
| cripto_cierre | tocadas | 221 | 99.09c | 95.93% | -3.16 pts | -5.73 a -0.59 | 9 |
| deportes_previo | todas | 618 | 97.96c | 95.63% | -2.33 pts | -3.93 a -0.72 | 27 |
| deportes_previo | tocadas | 603 | 98.01c | 95.52% | -2.49 pts | -4.14 a -0.84 | 27 |
| otros_cierre | todas | 275 | 99.44c | 99.64% | +0.20 pts | -0.51 a +0.92 | 1 |
| otros_cierre | tocadas | 265 | 99.43c | 99.62% | +0.19 pts | -0.55 a +0.94 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1557 | 98.68c | 97.43% | -1.25 pts | -2.03 a -0.47 | 40 |
| TOTAL | tocadas | 1474 | 98.68c | 97.29% | -1.39 pts | -2.21 a -0.57 | 40 |

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

Aun no hay veredicto: van 21 operaciones cerradas en 2.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
