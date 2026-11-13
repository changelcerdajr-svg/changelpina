# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.1 de 28 | corridas: 27
- Capital inicial: $1,000.00 | valor actual: $1,003.19 | P&L: $+3.19 (+0.32%)
- Efectivo libre: $402.60 | en ordenes abiertas: $400.95 (8) | en posiciones: $200.00 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 47 colocadas, 12 llenadas, 20 tocadas sin llenarse (sorteo 30%), 7 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 2 | 98.55c | 100.00% | 34.2-100.0% | +1.45 pts | $+1.48 | 0.58 |
| otros_cierre | 3 | 99.33c | 100.00% | 43.8-100.0% | +0.67 pts | $+1.01 | 0.11 |
| TOTAL | 8 | 99.12c | 100.00% | 67.6-100.0% | +0.88 pts | $+3.55 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $49.73 | 97.7c | 98.0c | deportes_previo |  | Spread: CSD Mixco (-2.5) |
| $49.96 | 99.2c | 99.2c | deportes_previo |  | Spread: CSD Mixco (-3.5) |
| $50.12 | 98.6c | 98.3c | deportes_previo |  | Northern Iowa Panthers vs. Iowa Hawkeyes (W) |
| $50.19 | 98.5c | 97.8c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 12, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 222 | abiertas: 336 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 89 | 98.83c | 97.75% | -1.07 pts | -4.13 a +1.99 | 2 |
| cripto_cierre | tocadas | 58 | 98.74c | 96.55% | -2.19 pts | -6.87 a +2.49 | 2 |
| deportes_previo | todas | 119 | 98.53c | 100.00% | +1.47 pts | +1.30 a +1.64 | 0 |
| deportes_previo | tocadas | 99 | 98.40c | 100.00% | +1.60 pts | +1.42 a +1.79 | 0 |
| otros_cierre | todas | 13 | 98.45c | 100.00% | +1.55 pts | +1.25 a +1.86 | 0 |
| otros_cierre | tocadas | 13 | 98.45c | 100.00% | +1.55 pts | +1.25 a +1.86 | 0 |
| post_fin_95_97 | todas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| post_fin_95_97 | tocadas | 1 | 95.00c | 100.00% | +5.00 pts | +5.00 a +5.00 | 0 |
| TOTAL | todas | 222 | 98.63c | 99.10% | +0.47 pts | -0.77 a +1.71 | 2 |
| TOTAL | tocadas | 171 | 98.50c | 98.83% | +0.33 pts | -1.27 a +1.94 | 2 |

Peores casos del registro sombra:

- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 8 operaciones cerradas en 1.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
