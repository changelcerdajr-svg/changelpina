# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 12.7 de 28 | corridas: 288
- Capital inicial: $1,000.00 | valor actual: $1,033.90 | P&L: $+33.90 (+3.39%)
- Efectivo libre: $413.67 | en ordenes abiertas: $361.73 (7) | en posiciones: $258.61 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 487 colocadas, 116 llenadas, 254 tocadas sin llenarse (sorteo 30%), 110 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 34 | 98.97c | 100.00% | 89.8-100.0% | +1.03 pts | $+17.60 | 0.29 |
| deportes_previo | 39 | 98.19c | 100.00% | 91.0-100.0% | +1.81 pts | $+36.19 | 0.35 |
| otros_cierre | 28 | 99.02c | 100.00% | 87.9-100.0% | +0.98 pts | $+14.29 | 0.40 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 111 | 98.43c | 99.04% | 95.1-99.8% | +0.61 pts | $+34.01 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.69 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Bitcoin be less than $54,000 on November 24? |
| $51.69 | 99.0c | 99.6c | cripto_cierre |  | Will the price of Bitcoin be between $54,000 and $56,000 on November 24? |
| $51.70 | 98.3c | 98.5c | deportes_previo |  | Stevenage FC vs. Sheffield Wednesday FC: O/U 6.5 |
| $51.71 | 97.7c | 97.0c | deportes_previo |  | Spread: Northampton Town FC (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4506 | abiertas: 495 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1281 | 98.72c | 99.22% | +0.50 pts | +0.02 a +0.98 | 10 |
| cripto_cierre | tocadas | 897 | 98.55c | 98.89% | +0.33 pts | -0.36 a +1.02 | 10 |
| deportes_previo | todas | 2500 | 98.30c | 98.88% | +0.58 pts | +0.17 a +0.99 | 29 |
| deportes_previo | tocadas | 2124 | 98.28c | 98.87% | +0.59 pts | +0.15 a +1.03 | 25 |
| otros_cierre | todas | 634 | 98.84c | 99.37% | +0.53 pts | -0.09 a +1.15 | 4 |
| otros_cierre | tocadas | 412 | 98.70c | 99.03% | +0.32 pts | -0.63 a +1.28 | 4 |
| post_fin_95_97 | todas | 91 | 95.89c | 93.41% | -2.48 pts | -7.61 a +2.65 | 6 |
| post_fin_95_97 | tocadas | 82 | 95.91c | 92.68% | -3.23 pts | -8.90 a +2.45 | 6 |
| TOTAL | todas | 4506 | 98.45c | 98.93% | +0.49 pts | +0.19 a +0.79 | 49 |
| TOTAL | tocadas | 3515 | 98.34c | 98.75% | +0.40 pts | +0.04 a +0.77 | 45 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.2c -> pago 0.0 | deportes_previo | tocada | FC UTA Arad vs. Universitatea Craiova CS: O/U 7.5
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.9c -> pago 0.0 | deportes_previo | tocada | Dundee FC vs. Heart of Midlothian FC: O/U 7.5
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $56,000 on November 20?

## Veredicto

Aun no hay veredicto: van 111 operaciones cerradas en 12.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
