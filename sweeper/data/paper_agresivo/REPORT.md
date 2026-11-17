# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.4 de 28 | corridas: 44
- Capital inicial: $1,000.00 | valor actual: $841.88 | P&L: $-158.12 (-15.81%)
- Efectivo libre: $0.00 | en ordenes abiertas: $479.05 (9) | en posiciones: $365.82 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 103 colocadas, 44 llenadas, 36 tocadas sin llenarse (sorteo 30%), 14 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 14 | 99.14c | 100.00% | 78.5-100.0% | +0.86 pts | $+8.77 | 0.07 |
| deportes_previo | 13 | 97.89c | 83.43% | 57.8-95.7% | -14.46 pts | $-173.50 | 0.70 |
| otros_cierre | 8 | 99.70c | 100.00% | 67.6-100.0% | +0.30 pts | $+1.15 | 0.76 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 38 | 98.50c | 93.22% | 82.7-98.5% | -5.29 pts | $-155.13 | 0.51 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $14.54 | 99.1c | 99.1c | deportes_previo |  | Spread: CA Grau (-2.5) |
| $83.86 | 98.9c | 98.9c | cripto_cierre |  | BNB Up or Down - November 16, 6:00PM-6:05PM ET |
| $76.38 | 96.9c | 96.9c | cripto_cierre |  | Dogecoin Up or Down - November 16, 6:00PM-6:05PM ET |
| $83.77 | 98.3c | 98.3c | deportes_previo |  | Spread: Aruba (-1.5) |
| $15.50 | 99.8c | 99.8c | deportes_previo |  | Spread: Aruba (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2681 | abiertas: 1913 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 652 | 99.09c | 99.54% | +0.45 pts | -0.06 a +0.97 | 3 |
| clima_cierre | tocadas | 595 | 99.05c | 99.50% | +0.45 pts | -0.12 a +1.01 | 3 |
| cripto_cierre | todas | 440 | 99.05c | 97.27% | -1.78 pts | -3.28 a -0.27 | 12 |
| cripto_cierre | tocadas | 400 | 99.09c | 97.00% | -2.09 pts | -3.74 a -0.43 | 12 |
| deportes_previo | todas | 1205 | 98.00c | 96.76% | -1.24 pts | -2.24 a -0.24 | 39 |
| deportes_previo | tocadas | 1184 | 98.04c | 96.71% | -1.33 pts | -2.35 a -0.32 | 39 |
| otros_cierre | todas | 349 | 99.28c | 99.43% | +0.15 pts | -0.64 a +0.94 | 2 |
| otros_cierre | tocadas | 334 | 99.28c | 99.40% | +0.12 pts | -0.70 a +0.95 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 2681 | 98.55c | 97.91% | -0.64 pts | -1.18 a -0.10 | 56 |
| TOTAL | tocadas | 2542 | 98.56c | 97.80% | -0.76 pts | -1.33 a -0.20 | 56 |

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

Aun no hay veredicto: van 38 operaciones cerradas en 3.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
