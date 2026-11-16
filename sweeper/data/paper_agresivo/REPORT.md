# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.4 de 28 | corridas: 42
- Capital inicial: $1,000.00 | valor actual: $837.71 | P&L: $-162.29 (-16.23%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $465.16 (9) | en posiciones: $371.28 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 96 colocadas, 40 llenadas, 34 tocadas sin llenarse (sorteo 30%), 13 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 14 | 99.14c | 100.00% | 78.5-100.0% | +0.86 pts | $+8.77 | 0.07 |
| deportes_previo | 13 | 97.89c | 83.43% | 57.8-95.7% | -14.46 pts | $-173.50 | 0.70 |
| otros_cierre | 7 | 99.70c | 100.00% | 64.6-100.0% | +0.30 pts | $+0.87 | 0.68 |
| TOTAL | 35 | 98.66c | 92.51% | 81.4-98.4% | -6.15 pts | $-163.56 | 0.47 |

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
| $82.24 | 95.0c | 99.6c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $14.54 | 99.1c | 99.1c | deportes_previo |  | Spread: CA Grau (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2571 | abiertas: 1961 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 598 | 99.10c | 99.50% | +0.40 pts | -0.16 a +0.96 | 3 |
| clima_cierre | tocadas | 548 | 99.06c | 99.45% | +0.39 pts | -0.22 a +1.01 | 3 |
| cripto_cierre | todas | 430 | 99.08c | 97.21% | -1.87 pts | -3.41 a -0.33 | 12 |
| cripto_cierre | tocadas | 391 | 99.11c | 96.93% | -2.18 pts | -3.86 a -0.49 | 12 |
| deportes_previo | todas | 1176 | 98.00c | 96.85% | -1.15 pts | -2.14 a -0.15 | 37 |
| deportes_previo | tocadas | 1157 | 98.04c | 96.80% | -1.24 pts | -2.25 a -0.23 | 37 |
| otros_cierre | todas | 334 | 99.33c | 99.70% | +0.37 pts | -0.22 a +0.96 | 1 |
| otros_cierre | tocadas | 321 | 99.32c | 99.69% | +0.36 pts | -0.25 a +0.98 | 1 |
| post_fin_90_97 | todas | 33 | 94.24c | 100.00% | +5.76 pts | +5.20 a +6.31 | 0 |
| post_fin_90_97 | tocadas | 27 | 94.38c | 100.00% | +5.62 pts | +5.03 a +6.21 | 0 |
| TOTAL | todas | 2571 | 98.56c | 97.94% | -0.62 pts | -1.17 a -0.08 | 53 |
| TOTAL | tocadas | 2444 | 98.57c | 97.83% | -0.73 pts | -1.31 a -0.16 | 53 |

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

Aun no hay veredicto: van 35 operaciones cerradas en 3.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
