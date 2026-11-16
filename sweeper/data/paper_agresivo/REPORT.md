# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.2 de 28 | corridas: 37
- Capital inicial: $1,000.00 | valor actual: $833.62 | P&L: $-166.38 (-16.64%)
- Efectivo libre: $0.00 | en ordenes abiertas: $462.64 (9) | en posiciones: $370.96 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 83 colocadas, 33 llenadas, 28 tocadas sin llenarse (sorteo 30%), 13 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 10 | 99.07c | 100.00% | 72.2-100.0% | +0.93 pts | $+7.24 | 0.07 |
| deportes_previo | 12 | 97.93c | 83.09% | 55.2-95.3% | -14.83 pts | $-174.43 | 0.74 |
| otros_cierre | 5 | 99.78c | 100.00% | 56.6-100.0% | +0.22 pts | $+0.49 | 0.79 |
| TOTAL | 28 | 98.59c | 91.39% | 77.4-98.0% | -7.20 pts | $-166.40 | 0.55 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 96.7c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 97.5c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $14.23 | 97.7c | 97.0c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 97.1c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 99.5c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2394 | abiertas: 1953 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 559 | 99.11c | 99.46% | +0.36 pts | -0.24 a +0.96 | 3 |
| clima_cierre | tocadas | 515 | 99.07c | 99.42% | +0.35 pts | -0.30 a +1.00 | 3 |
| cripto_cierre | todas | 423 | 99.10c | 97.16% | -1.94 pts | -3.50 a -0.37 | 12 |
| cripto_cierre | tocadas | 388 | 99.11c | 96.91% | -2.20 pts | -3.90 a -0.50 | 12 |
| deportes_previo | todas | 1076 | 97.93c | 96.56% | -1.37 pts | -2.46 a -0.29 | 37 |
| deportes_previo | tocadas | 1058 | 97.97c | 96.50% | -1.47 pts | -2.57 a -0.37 | 37 |
| otros_cierre | todas | 321 | 99.37c | 99.69% | +0.31 pts | -0.30 a +0.93 | 1 |
| otros_cierre | tocadas | 308 | 99.37c | 99.68% | +0.30 pts | -0.34 a +0.94 | 1 |
| post_fin_90_97 | todas | 15 | 95.00c | 100.00% | +5.00 pts | +4.48 a +5.52 | 0 |
| post_fin_90_97 | tocadas | 14 | 95.00c | 100.00% | +5.00 pts | +4.44 a +5.56 | 0 |
| TOTAL | todas | 2394 | 98.59c | 97.79% | -0.80 pts | -1.39 a -0.22 | 53 |
| TOTAL | tocadas | 2283 | 98.58c | 97.68% | -0.91 pts | -1.52 a -0.29 | 53 |

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

Aun no hay veredicto: van 28 operaciones cerradas en 3.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
