# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.0 de 28 | corridas: 33
- Capital inicial: $1,000.00 | valor actual: $917.52 | P&L: $-82.48 (-8.25%)
- Efectivo libre: $1.24 | en ordenes abiertas: $366.77 (7) | en posiciones: $554.91 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 77 colocadas, 32 llenadas, 26 tocadas sin llenarse (sorteo 30%), 12 expiradas

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
| $90.86 | 99.7c | 98.0c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 96.0c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $14.23 | 97.7c | 97.0c | otros_cierre |  | Will the USS George Washington depart CENTCOM by November 15, 2026? |
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 99.0c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $91.92 | 95.0c | 91.5c | deportes_previo |  | Sudan vs. Senegal: O/U 5.5 |
| $92.03 | 98.4c | 97.5c | deportes_previo |  | Sudan vs. Senegal: O/U 6.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2052 | abiertas: 1990 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 484 | 99.14c | 99.38% | +0.24 pts | -0.45 a +0.93 | 3 |
| clima_cierre | tocadas | 447 | 99.11c | 99.33% | +0.22 pts | -0.53 a +0.97 | 3 |
| cripto_cierre | todas | 330 | 99.07c | 96.36% | -2.71 pts | -4.70 a -0.71 | 12 |
| cripto_cierre | tocadas | 295 | 99.08c | 95.93% | -3.15 pts | -5.38 a -0.93 | 12 |
| deportes_previo | todas | 928 | 97.94c | 96.44% | -1.50 pts | -2.69 a -0.31 | 33 |
| deportes_previo | tocadas | 911 | 97.99c | 96.38% | -1.61 pts | -2.82 a -0.40 | 33 |
| otros_cierre | todas | 301 | 99.41c | 99.67% | +0.26 pts | -0.39 a +0.91 | 1 |
| otros_cierre | tocadas | 289 | 99.40c | 99.65% | +0.26 pts | -0.43 a +0.94 | 1 |
| post_fin_90_97 | todas | 9 | 94.70c | 100.00% | +5.30 pts | +4.72 a +5.88 | 0 |
| post_fin_90_97 | tocadas | 9 | 94.70c | 100.00% | +5.30 pts | +4.72 a +5.88 | 0 |
| TOTAL | todas | 2052 | 98.61c | 97.61% | -1.00 pts | -1.65 a -0.34 | 49 |
| TOTAL | tocadas | 1951 | 98.60c | 97.49% | -1.11 pts | -1.80 a -0.43 | 49 |

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

Aun no hay veredicto: van 25 operaciones cerradas en 3.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
