# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.3 de 28 | corridas: 31
- Capital inicial: $1,000.00 | valor actual: $1,005.51 | P&L: $+5.51 (+0.55%)
- Efectivo libre: $402.95 | en ordenes abiertas: $401.34 (8) | en posiciones: $200.84 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 52 colocadas, 14 llenadas, 22 tocadas sin llenarse (sorteo 30%), 8 expiradas

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
| $50.27 | 96.8c | 96.8c | post_fin_95_97 |  | Spread: Commanders (-6.5) |
| $50.12 | 98.6c | 98.3c | deportes_previo |  | Northern Iowa Panthers vs. Iowa Hawkeyes (W) |
| $50.19 | 98.5c | 99.0c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 12, 2026? |
| $50.26 | 97.9c | 98.5c | deportes_previo |  | Will Mlada Boleslav vs. Vysocina Jihlava end in a draw? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 344 | abiertas: 341 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 137 | 98.86c | 97.08% | -1.78 pts | -4.58 a +1.03 | 4 |
| cripto_cierre | tocadas | 92 | 98.76c | 95.65% | -3.11 pts | -7.27 a +1.05 | 4 |
| deportes_previo | todas | 174 | 98.37c | 100.00% | +1.63 pts | +1.49 a +1.77 | 0 |
| deportes_previo | tocadas | 154 | 98.26c | 100.00% | +1.74 pts | +1.60 a +1.88 | 0 |
| otros_cierre | todas | 32 | 98.42c | 100.00% | +1.58 pts | +1.35 a +1.81 | 0 |
| otros_cierre | tocadas | 30 | 98.40c | 100.00% | +1.60 pts | +1.37 a +1.83 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 344 | 98.56c | 98.84% | +0.28 pts | -0.85 a +1.41 | 4 |
| TOTAL | tocadas | 277 | 98.43c | 98.56% | +0.13 pts | -1.28 a +1.53 | 4 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $70,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 10 operaciones cerradas en 1.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
