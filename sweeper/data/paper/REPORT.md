# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.8 de 28 | corridas: 42
- Capital inicial: $1,000.00 | valor actual: $1,010.31 | P&L: $+10.31 (+1.03%)
- Efectivo libre: $404.16 | en ordenes abiertas: $252.28 (5) | en posiciones: $352.90 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 70 colocadas, 21 llenadas, 30 tocadas sin llenarse (sorteo 30%), 14 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 6 | 98.42c | 100.00% | 61.0-100.0% | +1.58 pts | $+4.84 | 0.48 |
| otros_cierre | 4 | 99.12c | 100.00% | 51.0-100.0% | +0.88 pts | $+1.77 | 0.15 |
| post_fin_95_97 | 1 | 96.80c | 100.00% | 20.7-100.0% | +3.20 pts | $+1.66 | 0.04 |
| TOTAL | 14 | 98.69c | 100.00% | 78.5-100.0% | +1.31 pts | $+9.34 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.40 | 99.7c | 99.7c | deportes_previo |  | Spread: Ethiopia (-3.5) |
| $50.40 | 99.2c | 99.2c | deportes_previo |  | Spread: Burundi (-2.5) |
| $50.43 | 98.7c | 100.0c | otros_cierre |  | Will the US national average gas price be less than $3.8900 on November 13? |
| $50.40 | 98.4c | 99.7c | cripto_cierre |  | Will the price of Bitcoin be between $72,000 and $74,000 on November 13? |
| $50.43 | 98.5c | 98.7c | cripto_cierre |  | Will the price of Ethereum be above $1,800 on November 13? |
| $50.42 | 99.4c | 98.6c | otros_cierre |  | Will Microsoft Corporation (MSFT) hit (HIGH) $577.50 Week of November 9 2026? |
| $50.43 | 97.5c | 97.5c | otros_cierre |  | Will Amazon.com, Inc. (AMZN) hit (LOW) $252 Week of November 9 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 387 | abiertas: 570 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 153 | 98.83c | 97.39% | -1.44 pts | -3.96 a +1.07 | 4 |
| cripto_cierre | tocadas | 100 | 98.77c | 96.00% | -2.76 pts | -6.59 a +1.06 | 4 |
| deportes_previo | todas | 187 | 98.34c | 99.47% | +1.13 pts | +0.08 a +2.17 | 1 |
| deportes_previo | tocadas | 166 | 98.25c | 99.40% | +1.15 pts | -0.02 a +2.33 | 1 |
| otros_cierre | todas | 41 | 98.54c | 100.00% | +1.46 pts | +1.24 a +1.67 | 0 |
| otros_cierre | tocadas | 37 | 98.49c | 100.00% | +1.51 pts | +1.29 a +1.73 | 0 |
| post_fin_95_97 | todas | 6 | 95.82c | 66.67% | -29.15 pts | -70.43 a +12.13 | 2 |
| post_fin_95_97 | tocadas | 6 | 95.82c | 66.67% | -29.15 pts | -70.43 a +12.13 | 2 |
| TOTAL | todas | 387 | 98.52c | 98.19% | -0.32 pts | -1.64 a +0.99 | 7 |
| TOTAL | tocadas | 309 | 98.40c | 97.73% | -0.66 pts | -2.31 a +0.98 | 7 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?
- 97.1c -> pago 0.0 | deportes_previo | tocada | Blues vs. Utah: O/U 2.5
- 96.5c -> pago 0.0 | post_fin_95_97 | tocada | Spread: Memphis (-10.5)
- 95.0c -> pago 0.0 | post_fin_95_97 | tocada | Spread: Memphis (-7.5)

## Veredicto

Aun no hay veredicto: van 14 operaciones cerradas en 1.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
