# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.5 de 28 | corridas: 45
- Capital inicial: $1,000.00 | valor actual: $845.39 | P&L: $-154.61 (-15.46%)
- Efectivo libre: $0.00 | en ordenes abiertas: $602.78 (11) | en posiciones: $245.60 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 109 colocadas, 45 llenadas, 39 tocadas sin llenarse (sorteo 30%), 14 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 16 | 98.98c | 100.00% | 80.6-100.0% | +1.02 pts | $+12.15 | 0.06 |
| deportes_previo | 14 | 97.91c | 83.63% | 60.1-96.0% | -14.27 pts | $-173.37 | 0.66 |
| otros_cierre | 8 | 99.70c | 100.00% | 67.6-100.0% | +0.30 pts | $+1.15 | 0.76 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 41 | 98.48c | 93.61% | 83.9-98.7% | -4.86 pts | $-151.62 | 0.48 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $83.77 | 98.3c | 98.3c | deportes_previo |  | Spread: Aruba (-1.5) |
| $15.50 | 99.8c | 99.8c | deportes_previo |  | Spread: Aruba (-2.5) |
| $54.57 | 98.8c | 98.8c | deportes_previo |  | Derius Davis: Anytime Touchdown |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2703 | abiertas: 1919 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 666 | 99.09c | 99.55% | +0.46 pts | -0.04 a +0.97 | 3 |
| clima_cierre | tocadas | 609 | 99.05c | 99.51% | +0.46 pts | -0.09 a +1.01 | 3 |
| cripto_cierre | todas | 444 | 99.04c | 97.30% | -1.75 pts | -3.24 a -0.25 | 12 |
| cripto_cierre | tocadas | 404 | 99.08c | 97.03% | -2.05 pts | -3.68 a -0.41 | 12 |
| deportes_previo | todas | 1209 | 98.00c | 96.77% | -1.23 pts | -2.22 a -0.24 | 39 |
| deportes_previo | tocadas | 1188 | 98.04c | 96.72% | -1.32 pts | -2.33 a -0.31 | 39 |
| otros_cierre | todas | 349 | 99.28c | 99.43% | +0.15 pts | -0.64 a +0.94 | 2 |
| otros_cierre | tocadas | 334 | 99.28c | 99.40% | +0.12 pts | -0.70 a +0.95 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 2703 | 98.56c | 97.93% | -0.63 pts | -1.16 a -0.09 | 56 |
| TOTAL | tocadas | 2564 | 98.56c | 97.82% | -0.75 pts | -1.31 a -0.18 | 56 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?

## Veredicto

Aun no hay veredicto: van 41 operaciones cerradas en 3.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
