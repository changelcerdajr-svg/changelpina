# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 2.9 de 28 | corridas: 30
- Capital inicial: $1,000.00 | valor actual: $920.25 | P&L: $-79.75 (-7.97%)
- Efectivo libre: $0.86 | en ordenes abiertas: $459.17 (7) | en posiciones: $462.88 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 73 colocadas, 31 llenadas, 24 tocadas sin llenarse (sorteo 30%), 11 expiradas

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
| $90.86 | 99.7c | 99.2c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 95.5c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $14.23 | 97.7c | 97.0c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 98.4c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 94.6c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $91.92 | 95.0c | 95.0c | deportes_previo |  | Sudan vs. Senegal: O/U 5.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1707 | abiertas: 2176 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 477 | 99.14c | 99.37% | +0.24 pts | -0.47 a +0.94 | 3 |
| clima_cierre | tocadas | 441 | 99.11c | 99.32% | +0.21 pts | -0.54 a +0.97 | 3 |
| cripto_cierre | todas | 295 | 99.10c | 95.93% | -3.17 pts | -5.39 a -0.94 | 12 |
| cripto_cierre | tocadas | 265 | 99.12c | 95.47% | -3.65 pts | -6.12 a -1.18 | 12 |
| deportes_previo | todas | 634 | 97.98c | 95.74% | -2.24 pts | -3.81 a -0.67 | 27 |
| deportes_previo | tocadas | 619 | 98.03c | 95.64% | -2.40 pts | -4.00 a -0.79 | 27 |
| otros_cierre | todas | 293 | 99.41c | 99.66% | +0.25 pts | -0.42 a +0.93 | 1 |
| otros_cierre | tocadas | 281 | 99.40c | 99.64% | +0.25 pts | -0.45 a +0.95 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1707 | 98.73c | 97.48% | -1.24 pts | -1.98 a -0.51 | 43 |
| TOTAL | tocadas | 1614 | 98.73c | 97.34% | -1.39 pts | -2.17 a -0.61 | 43 |

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

Aun no hay veredicto: van 25 operaciones cerradas en 2.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
