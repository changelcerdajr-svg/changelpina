# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.7 de 28 | corridas: 51
- Capital inicial: $1,000.00 | valor actual: $845.72 | P&L: $-154.28 (-15.43%)
- Efectivo libre: $0.00 | en ordenes abiertas: $381.75 (5) | en posiciones: $469.85 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 127 colocadas, 57 llenadas, 47 tocadas sin llenarse (sorteo 30%), 18 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 19 | 99.03c | 100.00% | 83.2-100.0% | +0.97 pts | $+12.97 | 0.06 |
| deportes_previo | 18 | 98.11c | 86.41% | 67.2-96.9% | -11.69 pts | $-171.14 | 0.55 |
| otros_cierre | 10 | 99.76c | 100.00% | 72.2-100.0% | +0.24 pts | $+1.31 | 0.62 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 50 | 98.62c | 94.61% | 86.5-98.9% | -4.01 pts | $-148.40 | 0.41 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $83.97 | 98.9c | 99.6c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 16, 2026? |
| $69.70 | 99.8c | 99.8c | otros_cierre |  | Will Brianna Cameron be eliminated in live shows week 2 of The Voice: Season 30? |
| $59.11 | 99.9c | 98.7c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $80.59 | 98.9c | 95.5c | deportes_previo |  | Tahiti vs. Cook Islands: O/U 0.5 |
| $7.62 | 99.7c | 99.7c | deportes_previo |  | Will Singapore win on 2026-11-17? |
| $77.09 | 98.5c | 98.5c | deportes_previo |  | Will Brazil win on 2026-11-17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2997 | abiertas: 1851 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 716 | 99.07c | 99.58% | +0.51 pts | +0.04 a +0.98 | 3 |
| clima_cierre | tocadas | 650 | 99.04c | 99.54% | +0.50 pts | -0.02 a +1.02 | 3 |
| cripto_cierre | todas | 474 | 99.00c | 97.47% | -1.54 pts | -2.94 a -0.14 | 12 |
| cripto_cierre | tocadas | 434 | 99.03c | 97.24% | -1.80 pts | -3.32 a -0.27 | 12 |
| deportes_previo | todas | 1410 | 98.07c | 96.81% | -1.26 pts | -2.18 a -0.35 | 45 |
| deportes_previo | tocadas | 1384 | 98.10c | 96.75% | -1.35 pts | -2.28 a -0.42 | 45 |
| otros_cierre | todas | 362 | 99.26c | 99.45% | +0.19 pts | -0.58 a +0.95 | 2 |
| otros_cierre | tocadas | 346 | 99.26c | 99.42% | +0.16 pts | -0.64 a +0.96 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 2997 | 98.56c | 97.93% | -0.63 pts | -1.13 a -0.12 | 62 |
| TOTAL | tocadas | 2843 | 98.56c | 97.82% | -0.74 pts | -1.27 a -0.21 | 62 |

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

Aun no hay veredicto: van 50 operaciones cerradas en 3.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
