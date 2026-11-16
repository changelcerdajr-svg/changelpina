# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.4 de 28 | corridas: 43
- Capital inicial: $1,000.00 | valor actual: $838.57 | P&L: $-161.43 (-16.14%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $461.59 (9) | en posiciones: $378.68 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 99 colocadas, 42 llenadas, 35 tocadas sin llenarse (sorteo 30%), 13 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 14 | 99.14c | 100.00% | 78.5-100.0% | +0.86 pts | $+8.77 | 0.07 |
| deportes_previo | 13 | 97.89c | 83.43% | 57.8-95.7% | -14.46 pts | $-173.50 | 0.70 |
| otros_cierre | 7 | 99.70c | 100.00% | 64.6-100.0% | +0.30 pts | $+0.87 | 0.68 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 36 | 98.57c | 92.77% | 81.9-98.5% | -5.80 pts | $-159.73 | 0.48 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 96.8c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 99.6c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $14.54 | 99.1c | 99.1c | deportes_previo |  | Spread: CA Grau (-2.5) |
| $83.77 | 98.3c | 98.3c | deportes_previo |  | Spread: Aruba (-1.5) |
| $15.50 | 99.8c | 99.8c | deportes_previo |  | Spread: Aruba (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2599 | abiertas: 1965 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 612 | 99.10c | 99.51% | +0.41 pts | -0.14 a +0.96 | 3 |
| clima_cierre | tocadas | 561 | 99.06c | 99.47% | +0.41 pts | -0.19 a +1.01 | 3 |
| cripto_cierre | todas | 430 | 99.08c | 97.21% | -1.87 pts | -3.41 a -0.33 | 12 |
| cripto_cierre | tocadas | 391 | 99.11c | 96.93% | -2.18 pts | -3.86 a -0.49 | 12 |
| deportes_previo | todas | 1180 | 98.00c | 96.86% | -1.13 pts | -2.13 a -0.14 | 37 |
| deportes_previo | tocadas | 1161 | 98.03c | 96.81% | -1.22 pts | -2.23 a -0.21 | 37 |
| otros_cierre | todas | 343 | 99.29c | 99.71% | +0.42 pts | -0.16 a +1.00 | 1 |
| otros_cierre | tocadas | 330 | 99.28c | 99.70% | +0.41 pts | -0.19 a +1.01 | 1 |
| post_fin_90_97 | todas | 34 | 94.26c | 100.00% | +5.74 pts | +5.19 a +6.28 | 0 |
| post_fin_90_97 | tocadas | 28 | 94.40c | 100.00% | +5.60 pts | +5.03 a +6.17 | 0 |
| TOTAL | todas | 2599 | 98.56c | 97.96% | -0.60 pts | -1.14 a -0.06 | 53 |
| TOTAL | tocadas | 2471 | 98.56c | 97.86% | -0.71 pts | -1.27 a -0.14 | 53 |

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

Aun no hay veredicto: van 36 operaciones cerradas en 3.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
