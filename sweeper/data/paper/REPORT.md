# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.3 de 28 | corridas: 30
- Capital inicial: $1,000.00 | valor actual: $1,005.33 | P&L: $+5.33 (+0.53%)
- Efectivo libre: $402.96 | en ordenes abiertas: $451.60 (9) | en posiciones: $150.57 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 51 colocadas, 13 llenadas, 21 tocadas sin llenarse (sorteo 30%), 8 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 4 | 98.50c | 100.00% | 51.0-100.0% | +1.50 pts | $+3.05 | 0.49 |
| otros_cierre | 3 | 99.33c | 100.00% | 43.8-100.0% | +0.67 pts | $+1.01 | 0.11 |
| TOTAL | 10 | 98.99c | 100.00% | 72.2-100.0% | +1.01 pts | $+5.12 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.12 | 98.6c | 98.3c | deportes_previo |  | Northern Iowa Panthers vs. Iowa Hawkeyes (W) |
| $50.19 | 98.5c | 99.0c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 12, 2026? |
| $50.26 | 97.9c | 98.2c | deportes_previo |  | Will Mlada Boleslav vs. Vysocina Jihlava end in a draw? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 286 | abiertas: 342 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 100 | 98.82c | 96.00% | -2.82 pts | -6.65 a +1.01 | 4 |
| cripto_cierre | tocadas | 67 | 98.72c | 94.03% | -4.69 pts | -10.36 a +0.98 | 4 |
| deportes_previo | todas | 163 | 98.40c | 100.00% | +1.60 pts | +1.45 a +1.75 | 0 |
| deportes_previo | tocadas | 143 | 98.29c | 100.00% | +1.71 pts | +1.56 a +1.86 | 0 |
| otros_cierre | todas | 22 | 98.52c | 100.00% | +1.48 pts | +1.23 a +1.73 | 0 |
| otros_cierre | tocadas | 21 | 98.48c | 100.00% | +1.52 pts | +1.28 a +1.77 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 286 | 98.54c | 98.60% | +0.06 pts | -1.30 a +1.42 | 4 |
| TOTAL | tocadas | 232 | 98.42c | 98.28% | -0.14 pts | -1.82 a +1.53 | 4 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 10 operaciones cerradas en 1.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
