# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.6 de 28 | corridas: 48
- Capital inicial: $1,000.00 | valor actual: $816.45 | P&L: $-183.55 (-18.35%)
- Efectivo libre: $0.00 | en ordenes abiertas: $282.50 (6) | en posiciones: $565.96 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 117 colocadas, 51 llenadas, 44 tocadas sin llenarse (sorteo 30%), 16 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 16 | 98.98c | 100.00% | 80.6-100.0% | +1.02 pts | $+12.15 | 0.06 |
| deportes_previo | 14 | 97.91c | 83.63% | 60.1-96.0% | -14.27 pts | $-173.37 | 0.66 |
| otros_cierre | 9 | 99.74c | 100.00% | 70.1-100.0% | +0.26 pts | $+1.23 | 0.68 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 42 | 98.51c | 93.79% | 84.2-98.7% | -4.73 pts | $-151.54 | 0.47 |

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
| $54.57 | 98.8c | 50.0c | deportes_previo |  | Derius Davis: Anytime Touchdown |
| $84.54 | 99.9c | 100.0c | deportes_previo |  | Counter-Strike: BANGARANGA vs banda chuya (BO1) - ESEA Advanced Europe Regular S |
| $81.76 | 99.8c | 99.8c | cripto_cierre |  | Bitcoin above 66,600 on November 16, 10PM ET? |
| $10.98 | 99.8c | 99.8c | cripto_cierre |  | Bitcoin above 66,400 on November 16, 10PM ET? |
| $83.97 | 98.9c | 97.2c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 16, 2026? |
| $59.11 | 99.9c | 98.7c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2744 | abiertas: 1923 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 685 | 99.08c | 99.56% | +0.48 pts | -0.01 a +0.97 | 3 |
| clima_cierre | tocadas | 623 | 99.04c | 99.52% | +0.48 pts | -0.06 a +1.02 | 3 |
| cripto_cierre | todas | 452 | 99.01c | 97.35% | -1.66 pts | -3.13 a -0.20 | 12 |
| cripto_cierre | tocadas | 412 | 99.04c | 97.09% | -1.95 pts | -3.56 a -0.35 | 12 |
| deportes_previo | todas | 1219 | 98.00c | 96.72% | -1.28 pts | -2.28 a -0.28 | 40 |
| deportes_previo | tocadas | 1198 | 98.03c | 96.66% | -1.37 pts | -2.39 a -0.36 | 40 |
| otros_cierre | todas | 353 | 99.27c | 99.43% | +0.17 pts | -0.61 a +0.95 | 2 |
| otros_cierre | tocadas | 337 | 99.27c | 99.41% | +0.14 pts | -0.68 a +0.96 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 2744 | 98.55c | 97.92% | -0.63 pts | -1.16 a -0.10 | 57 |
| TOTAL | tocadas | 2599 | 98.55c | 97.81% | -0.75 pts | -1.30 a -0.19 | 57 |

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

Aun no hay veredicto: van 42 operaciones cerradas en 3.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
