# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 0.9 de 28 | corridas: 21
- Capital inicial: $1,000.00 | valor actual: $1,002.44 | P&L: $+2.44 (+0.24%)
- Efectivo libre: $401.28 | en ordenes abiertas: $400.49 (8) | en posiciones: $199.80 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 41 colocadas, 9 llenadas, 17 tocadas sin llenarse (sorteo 30%), 7 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 1 | 99.40c | 100.00% | 20.7-100.0% | +0.60 pts | $+0.30 | 0.42 |
| otros_cierre | 1 | 99.60c | 100.00% | 20.7-100.0% | +0.40 pts | $+0.20 | 0.17 |
| TOTAL | 5 | 99.38c | 100.00% | 56.6-100.0% | +0.62 pts | $+1.56 | 0.23 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.00 | 97.7c | 99.6c | deportes_previo |  | Will Somalia win on 2026-11-12? |
| $50.11 | 99.2c | 99.2c | otros_cierre |  | Will Microsoft (MSFT) close above $520 on November 12? |
| $49.73 | 97.7c | 97.5c | deportes_previo |  | Spread: CSD Mixco (-2.5) |
| $49.96 | 99.2c | 99.2c | deportes_previo |  | Spread: CSD Mixco (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 106 | abiertas: 369 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 82 | 98.94c | 97.56% | -1.38 pts | -4.70 a +1.93 | 2 |
| cripto_cierre | tocadas | 52 | 98.89c | 96.15% | -2.74 pts | -7.94 a +2.47 | 2 |
| deportes_previo | todas | 21 | 98.77c | 100.00% | +1.23 pts | +0.92 a +1.55 | 0 |
| deportes_previo | tocadas | 18 | 98.78c | 100.00% | +1.22 pts | +0.86 a +1.58 | 0 |
| otros_cierre | todas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| otros_cierre | tocadas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| TOTAL | todas | 106 | 98.91c | 98.11% | -0.80 pts | -3.36 a +1.77 | 2 |
| TOTAL | tocadas | 73 | 98.87c | 97.26% | -1.61 pts | -5.33 a +2.11 | 2 |

Peores casos del registro sombra:

- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 5 operaciones cerradas en 0.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
