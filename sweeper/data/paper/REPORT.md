# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.4 de 28 | corridas: 34
- Capital inicial: $1,000.00 | valor actual: $1,008.59 | P&L: $+8.59 (+0.86%)
- Efectivo libre: $404.37 | en ordenes abiertas: $452.80 (9) | en posiciones: $151.09 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 62 colocadas, 16 llenadas, 26 tocadas sin llenarse (sorteo 30%), 11 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 5 | 98.52c | 100.00% | 56.6-100.0% | +1.48 pts | $+3.76 | 0.48 |
| otros_cierre | 4 | 99.12c | 100.00% | 51.0-100.0% | +0.88 pts | $+1.77 | 0.15 |
| post_fin_95_97 | 1 | 96.80c | 100.00% | 20.7-100.0% | +3.20 pts | $+1.66 | 0.04 |
| TOTAL | 13 | 98.75c | 100.00% | 77.2-100.0% | +1.25 pts | $+8.26 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.26 | 97.9c | 98.4c | deportes_previo |  | Will Mlada Boleslav vs. Vysocina Jihlava end in a draw? |
| $50.40 | 98.4c | 98.6c | cripto_cierre |  | Will the price of Bitcoin be between $72,000 and $74,000 on November 13? |
| $50.43 | 98.5c | 98.5c | cripto_cierre |  | Will the price of Ethereum be above $1,800 on November 13? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 368 | abiertas: 363 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 146 | 98.85c | 97.26% | -1.58 pts | -4.22 a +1.05 | 4 |
| cripto_cierre | tocadas | 96 | 98.75c | 95.83% | -2.92 pts | -6.90 a +1.07 | 4 |
| deportes_previo | todas | 181 | 98.36c | 99.45% | +1.09 pts | +0.01 a +2.17 | 1 |
| deportes_previo | tocadas | 161 | 98.26c | 99.38% | +1.12 pts | -0.09 a +2.33 | 1 |
| otros_cierre | todas | 40 | 98.52c | 100.00% | +1.48 pts | +1.25 a +1.70 | 0 |
| otros_cierre | tocadas | 36 | 98.46c | 100.00% | +1.54 pts | +1.32 a +1.76 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 368 | 98.56c | 98.64% | +0.08 pts | -1.10 a +1.26 | 5 |
| TOTAL | tocadas | 294 | 98.43c | 98.30% | -0.13 pts | -1.61 a +1.34 | 5 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?
- 97.1c -> pago 0.0 | deportes_previo | tocada | Blues vs. Utah: O/U 2.5

## Veredicto

Aun no hay veredicto: van 13 operaciones cerradas en 1.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
