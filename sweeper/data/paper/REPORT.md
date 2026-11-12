# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 1.0 de 28 | corridas: 24
- Capital inicial: $1,000.00 | valor actual: $1,003.73 | P&L: $+3.73 (+0.37%)
- Efectivo libre: $402.60 | en ordenes abiertas: $451.14 (9) | en posiciones: $149.81 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 47 colocadas, 11 llenadas, 20 tocadas sin llenarse (sorteo 30%), 7 expiradas

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
| $50.12 | 98.6c | 98.7c | deportes_previo |  | Northern Iowa Panthers vs. Iowa Hawkeyes (W) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 179 | abiertas: 338 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 85 | 98.90c | 97.65% | -1.25 pts | -4.45 a +1.95 | 2 |
| cripto_cierre | tocadas | 54 | 98.85c | 96.30% | -2.55 pts | -7.57 a +2.46 | 2 |
| deportes_previo | todas | 85 | 98.56c | 100.00% | +1.44 pts | +1.24 a +1.64 | 0 |
| deportes_previo | tocadas | 70 | 98.43c | 100.00% | +1.57 pts | +1.35 a +1.78 | 0 |
| otros_cierre | todas | 9 | 98.66c | 100.00% | +1.34 pts | +1.07 a +1.61 | 0 |
| otros_cierre | tocadas | 9 | 98.66c | 100.00% | +1.34 pts | +1.07 a +1.61 | 0 |
| TOTAL | todas | 179 | 98.73c | 98.88% | +0.16 pts | -1.37 a +1.69 | 2 |
| TOTAL | tocadas | 133 | 98.62c | 98.50% | -0.12 pts | -2.18 a +1.94 | 2 |

Peores casos del registro sombra:

- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.2c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 8 operaciones cerradas en 1.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
