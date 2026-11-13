# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.8 de 28 | corridas: 43
- Capital inicial: $1,000.00 | valor actual: $1,011.82 | P&L: $+11.82 (+1.18%)
- Efectivo libre: $354.85 | en ordenes abiertas: $505.24 (10) | en posiciones: $151.24 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 75 colocadas, 21 llenadas, 30 tocadas sin llenarse (sorteo 30%), 14 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 4 | 99.10c | 100.00% | 51.0-100.0% | +0.90 pts | $+1.83 | 0.23 |
| deportes_previo | 8 | 98.68c | 100.00% | 67.6-100.0% | +1.32 pts | $+5.40 | 0.43 |
| otros_cierre | 5 | 99.04c | 100.00% | 56.6-100.0% | +0.96 pts | $+2.44 | 0.18 |
| post_fin_95_97 | 1 | 96.80c | 100.00% | 20.7-100.0% | +3.20 pts | $+1.66 | 0.04 |
| TOTAL | 18 | 98.77c | 100.00% | 82.4-100.0% | +1.23 pts | $+11.33 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.40 | 98.4c | 99.7c | cripto_cierre |  | Will the price of Bitcoin be between $72,000 and $74,000 on November 13? |
| $50.42 | 99.4c | 98.6c | otros_cierre |  | Will Microsoft Corporation (MSFT) hit (HIGH) $577.50 Week of November 9 2026? |
| $50.43 | 97.5c | 98.0c | otros_cierre |  | Will Amazon.com, Inc. (AMZN) hit (LOW) $252 Week of November 9 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 448 | abiertas: 538 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 205 | 98.81c | 98.05% | -0.76 pts | -2.65 a +1.12 | 4 |
| cripto_cierre | tocadas | 141 | 98.76c | 97.16% | -1.60 pts | -4.33 a +1.13 | 4 |
| deportes_previo | todas | 190 | 98.35c | 99.47% | +1.13 pts | +0.10 a +2.15 | 1 |
| deportes_previo | tocadas | 169 | 98.26c | 99.41% | +1.15 pts | -0.00 a +2.31 | 1 |
| otros_cierre | todas | 47 | 98.62c | 100.00% | +1.38 pts | +1.18 a +1.59 | 0 |
| otros_cierre | tocadas | 37 | 98.49c | 100.00% | +1.51 pts | +1.29 a +1.73 | 0 |
| post_fin_95_97 | todas | 6 | 95.82c | 66.67% | -29.15 pts | -70.43 a +12.13 | 2 |
| post_fin_95_97 | tocadas | 6 | 95.82c | 66.67% | -29.15 pts | -70.43 a +12.13 | 2 |
| TOTAL | todas | 448 | 98.56c | 98.44% | -0.12 pts | -1.25 a +1.02 | 7 |
| TOTAL | tocadas | 353 | 98.44c | 98.02% | -0.42 pts | -1.86 a +1.02 | 7 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?
- 97.1c -> pago 0.0 | deportes_previo | tocada | Blues vs. Utah: O/U 2.5
- 96.5c -> pago 0.0 | post_fin_95_97 | tocada | Spread: Memphis (-10.5)
- 95.0c -> pago 0.0 | post_fin_95_97 | tocada | Spread: Memphis (-7.5)

## Veredicto

Aun no hay veredicto: van 18 operaciones cerradas en 1.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
