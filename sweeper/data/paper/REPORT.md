# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.2 de 28 | corridas: 29
- Capital inicial: $1,000.00 | valor actual: $1,005.28 | P&L: $+5.28 (+0.53%)
- Efectivo libre: $403.34 | en ordenes abiertas: $451.21 (9) | en posiciones: $150.57 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 49 colocadas, 13 llenadas, 20 tocadas sin llenarse (sorteo 30%), 7 expiradas

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
| $50.19 | 98.5c | 99.1c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 12, 2026? |
| $50.26 | 97.9c | 97.9c | deportes_previo |  | Will Mlada Boleslav vs. Vysocina Jihlava end in a draw? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 247 | abiertas: 323 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 93 | 98.80c | 97.85% | -0.95 pts | -3.88 a +1.98 | 2 |
| cripto_cierre | tocadas | 62 | 98.71c | 96.77% | -1.93 pts | -6.32 a +2.45 | 2 |
| deportes_previo | todas | 139 | 98.42c | 100.00% | +1.58 pts | +1.42 a +1.74 | 0 |
| deportes_previo | tocadas | 119 | 98.29c | 100.00% | +1.71 pts | +1.53 a +1.88 | 0 |
| otros_cierre | todas | 14 | 98.39c | 100.00% | +1.61 pts | +1.30 a +1.91 | 0 |
| otros_cierre | tocadas | 14 | 98.39c | 100.00% | +1.61 pts | +1.30 a +1.91 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 247 | 98.55c | 99.19% | +0.64 pts | -0.47 a +1.76 | 2 |
| TOTAL | tocadas | 196 | 98.42c | 98.98% | +0.56 pts | -0.84 a +1.97 | 2 |

Peores casos del registro sombra:

- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 10 operaciones cerradas en 1.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
