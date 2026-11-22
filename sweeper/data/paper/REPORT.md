# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 11.0 de 28 | corridas: 242
- Capital inicial: $1,000.00 | valor actual: $1,023.64 | P&L: $+23.64 (+2.36%)
- Efectivo libre: $412.44 | en ordenes abiertas: $455.05 (11) | en posiciones: $156.06 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 411 colocadas, 98 llenadas, 213 tocadas sin llenarse (sorteo 30%), 89 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 26 | 98.90c | 100.00% | 87.1-100.0% | +1.10 pts | $+15.05 | 0.28 |
| deportes_previo | 35 | 98.23c | 100.00% | 90.1-100.0% | +1.77 pts | $+32.51 | 0.34 |
| otros_cierre | 24 | 99.02c | 100.00% | 86.2-100.0% | +0.98 pts | $+12.21 | 0.44 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 94 | 98.40c | 98.89% | 94.2-99.8% | +0.49 pts | $+23.55 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $7.32 | 98.6c | 98.7c | deportes_previo |  | Spread: CF Cruz Azul (-3.5) |
| $53.71 | 99.0c | 99.4c | cripto_cierre |  | Will Bitcoin reach $66,000 November 16-22? |
| $43.20 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3848 | abiertas: 393 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1064 | 98.73c | 99.06% | +0.33 pts | -0.25 a +0.91 | 10 |
| cripto_cierre | tocadas | 728 | 98.56c | 98.63% | +0.07 pts | -0.77 a +0.92 | 10 |
| deportes_previo | todas | 2175 | 98.31c | 98.94% | +0.64 pts | +0.21 a +1.06 | 24 |
| deportes_previo | tocadas | 1856 | 98.28c | 98.87% | +0.59 pts | +0.12 a +1.07 | 22 |
| otros_cierre | todas | 537 | 98.81c | 99.26% | +0.45 pts | -0.28 a +1.18 | 4 |
| otros_cierre | tocadas | 361 | 98.70c | 98.89% | +0.20 pts | -0.89 a +1.28 | 4 |
| post_fin_95_97 | todas | 72 | 95.91c | 91.67% | -4.25 pts | -10.68 a +2.18 | 6 |
| post_fin_95_97 | tocadas | 64 | 95.93c | 90.62% | -5.30 pts | -12.50 a +1.89 | 6 |
| TOTAL | todas | 3848 | 98.45c | 98.88% | +0.43 pts | +0.10 a +0.76 | 44 |
| TOTAL | tocadas | 3009 | 98.34c | 98.64% | +0.29 pts | -0.12 a +0.70 | 42 |

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

Aun no hay veredicto: van 94 operaciones cerradas en 11.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
