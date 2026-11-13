# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.3 de 28 | corridas: 32
- Capital inicial: $1,000.00 | valor actual: $1,008.01 | P&L: $+8.01 (+0.80%)
- Efectivo libre: $403.90 | en ordenes abiertas: $503.15 (10) | en posiciones: $100.45 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 58 colocadas, 14 llenadas, 23 tocadas sin llenarse (sorteo 30%), 11 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 5 | 98.52c | 100.00% | 56.6-100.0% | +1.48 pts | $+3.76 | 0.48 |
| otros_cierre | 3 | 99.33c | 100.00% | 43.8-100.0% | +0.67 pts | $+1.01 | 0.11 |
| post_fin_95_97 | 1 | 96.80c | 100.00% | 20.7-100.0% | +3.20 pts | $+1.66 | 0.04 |
| TOTAL | 12 | 98.77c | 100.00% | 75.7-100.0% | +1.23 pts | $+7.50 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.19 | 98.5c | 99.0c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 12, 2026? |
| $50.26 | 97.9c | 98.5c | deportes_previo |  | Will Mlada Boleslav vs. Vysocina Jihlava end in a draw? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 354 | abiertas: 360 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 141 | 98.86c | 97.16% | -1.70 pts | -4.43 a +1.03 | 4 |
| cripto_cierre | tocadas | 92 | 98.76c | 95.65% | -3.11 pts | -7.27 a +1.05 | 4 |
| deportes_previo | todas | 179 | 98.36c | 99.44% | +1.08 pts | -0.01 a +2.17 | 1 |
| deportes_previo | tocadas | 159 | 98.26c | 99.37% | +1.11 pts | -0.11 a +2.34 | 1 |
| otros_cierre | todas | 33 | 98.43c | 100.00% | +1.57 pts | +1.35 a +1.79 | 0 |
| otros_cierre | tocadas | 31 | 98.42c | 100.00% | +1.58 pts | +1.36 a +1.81 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 354 | 98.56c | 98.59% | +0.03 pts | -1.20 a +1.25 | 5 |
| TOTAL | tocadas | 283 | 98.43c | 98.23% | -0.19 pts | -1.73 a +1.34 | 5 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?
- 97.1c -> pago 0.0 | deportes_previo | tocada | Blues vs. Utah: O/U 2.5

## Veredicto

Aun no hay veredicto: van 12 operaciones cerradas en 1.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
