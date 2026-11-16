# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.1 de 28 | corridas: 36
- Capital inicial: $1,000.00 | valor actual: $816.15 | P&L: $-183.85 (-18.39%)
- Efectivo libre: $0.00 | en ordenes abiertas: $276.81 (6) | en posiciones: $646.11 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 79 colocadas, 33 llenadas, 28 tocadas sin llenarse (sorteo 30%), 12 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 10 | 99.07c | 100.00% | 72.2-100.0% | +0.93 pts | $+7.24 | 0.07 |
| deportes_previo | 9 | 98.10c | 88.41% | 56.5-98.0% | -9.69 pts | $-85.11 | 0.90 |
| otros_cierre | 5 | 99.78c | 100.00% | 56.6-100.0% | +0.22 pts | $+0.49 | 0.79 |
| TOTAL | 25 | 98.76c | 94.90% | 80.5-99.3% | -3.85 pts | $-77.09 | 0.58 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 97.8c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 95.5c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $14.23 | 97.7c | 97.0c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 99.5c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $91.92 | 95.0c | 0.1c | deportes_previo |  | Sudan vs. Senegal: O/U 5.5 |
| $92.03 | 98.4c | 85.1c | deportes_previo |  | Sudan vs. Senegal: O/U 6.5 |
| $91.20 | 98.8c | 97.8c | deportes_previo |  | Spread: Moldova (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2162 | abiertas: 2054 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 499 | 99.14c | 99.40% | +0.26 pts | -0.41 a +0.93 | 3 |
| clima_cierre | tocadas | 461 | 99.11c | 99.35% | +0.24 pts | -0.49 a +0.97 | 3 |
| cripto_cierre | todas | 340 | 99.07c | 96.47% | -2.60 pts | -4.53 a -0.66 | 12 |
| cripto_cierre | tocadas | 305 | 99.08c | 96.07% | -3.01 pts | -5.17 a -0.86 | 12 |
| deportes_previo | todas | 1007 | 97.96c | 96.43% | -1.54 pts | -2.68 a -0.39 | 36 |
| deportes_previo | tocadas | 990 | 98.00c | 96.36% | -1.64 pts | -2.80 a -0.48 | 36 |
| otros_cierre | todas | 303 | 99.41c | 99.67% | +0.26 pts | -0.39 a +0.91 | 1 |
| otros_cierre | tocadas | 291 | 99.40c | 99.66% | +0.26 pts | -0.42 a +0.93 | 1 |
| post_fin_90_97 | todas | 13 | 94.88c | 100.00% | +5.12 pts | +4.60 a +5.63 | 0 |
| post_fin_90_97 | tocadas | 12 | 94.88c | 100.00% | +5.13 pts | +4.56 a +5.69 | 0 |
| TOTAL | todas | 2162 | 98.59c | 97.59% | -1.00 pts | -1.64 a -0.36 | 52 |
| TOTAL | tocadas | 2059 | 98.59c | 97.47% | -1.11 pts | -1.79 a -0.44 | 52 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?
- 98.9c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 15?
- 98.7c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)

## Veredicto

Aun no hay veredicto: van 25 operaciones cerradas en 3.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
