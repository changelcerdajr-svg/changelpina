# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.7 de 28 | corridas: 41
- Capital inicial: $1,000.00 | valor actual: $1,010.42 | P&L: $+10.42 (+1.04%)
- Efectivo libre: $404.15 | en ordenes abiertas: $252.29 (5) | en posiciones: $352.90 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 69 colocadas, 21 llenadas, 29 tocadas sin llenarse (sorteo 30%), 14 expiradas

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
| $50.43 | 98.5c | 98.9c | cripto_cierre |  | Will the price of Ethereum be above $1,800 on November 13? |
| $50.42 | 99.4c | 98.6c | otros_cierre |  | Will Microsoft Corporation (MSFT) hit (HIGH) $577.50 Week of November 9 2026? |
| $50.43 | 97.5c | 97.5c | otros_cierre |  | Will Amazon.com, Inc. (AMZN) hit (LOW) $252 Week of November 9 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 376 | abiertas: 563 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 150 | 98.81c | 97.33% | -1.48 pts | -4.05 a +1.09 | 4 |
| cripto_cierre | tocadas | 97 | 98.74c | 95.88% | -2.86 pts | -6.81 a +1.08 | 4 |
| deportes_previo | todas | 184 | 98.36c | 99.46% | +1.10 pts | +0.04 a +2.16 | 1 |
| deportes_previo | tocadas | 164 | 98.26c | 99.39% | +1.13 pts | -0.06 a +2.32 | 1 |
| otros_cierre | todas | 41 | 98.54c | 100.00% | +1.46 pts | +1.24 a +1.67 | 0 |
| otros_cierre | tocadas | 37 | 98.49c | 100.00% | +1.51 pts | +1.29 a +1.73 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 376 | 98.55c | 98.67% | +0.12 pts | -1.04 a +1.27 | 5 |
| TOTAL | tocadas | 299 | 98.43c | 98.33% | -0.10 pts | -1.55 a +1.35 | 5 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?
- 97.1c -> pago 0.0 | deportes_previo | tocada | Blues vs. Utah: O/U 2.5

## Veredicto

Aun no hay veredicto: van 14 operaciones cerradas en 1.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
