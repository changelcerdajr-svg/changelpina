# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.0 de 28 | corridas: 23
- Capital inicial: $1,000.00 | valor actual: $1,002.94 | P&L: $+2.94 (+0.29%)
- Efectivo libre: $404.36 | en ordenes abiertas: $348.35 (7) | en posiciones: $250.03 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 44 colocadas, 11 llenadas, 19 tocadas sin llenarse (sorteo 30%), 7 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.30c | 100.00% | 43.8-100.0% | +0.70 pts | $+1.06 | 0.18 |
| deportes_previo | 2 | 98.55c | 100.00% | 34.2-100.0% | +1.45 pts | $+1.48 | 0.58 |
| otros_cierre | 1 | 99.60c | 100.00% | 20.7-100.0% | +0.40 pts | $+0.20 | 0.17 |
| TOTAL | 6 | 99.10c | 100.00% | 61.0-100.0% | +0.90 pts | $+2.74 | 0.31 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.11 | 99.2c | 100.0c | otros_cierre |  | Will Microsoft (MSFT) close above $520 on November 12? |
| $50.11 | 99.2c | 99.2c | otros_cierre |  | Will Apple (AAPL) close above $340 on November 12? |
| $49.73 | 97.7c | 97.3c | deportes_previo |  | Spread: CSD Mixco (-2.5) |
| $49.96 | 99.2c | 99.2c | deportes_previo |  | Spread: CSD Mixco (-3.5) |
| $50.12 | 98.6c | 98.7c | deportes_previo |  | Northern Iowa Panthers vs. Iowa Hawkeyes (W) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 129 | abiertas: 371 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 83 | 98.92c | 97.59% | -1.33 pts | -4.61 a +1.94 | 2 |
| cripto_cierre | tocadas | 53 | 98.86c | 96.23% | -2.64 pts | -7.75 a +2.47 | 2 |
| deportes_previo | todas | 43 | 98.52c | 100.00% | +1.48 pts | +1.21 a +1.75 | 0 |
| deportes_previo | tocadas | 40 | 98.51c | 100.00% | +1.49 pts | +1.20 a +1.78 | 0 |
| otros_cierre | todas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| otros_cierre | tocadas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| TOTAL | todas | 129 | 98.79c | 98.45% | -0.34 pts | -2.46 a +1.78 | 2 |
| TOTAL | tocadas | 96 | 98.72c | 97.92% | -0.80 pts | -3.64 a +2.04 | 2 |

Peores casos del registro sombra:

- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 6 operaciones cerradas en 1.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
