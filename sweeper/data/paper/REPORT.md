# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 13.7 de 28 | corridas: 312
- Capital inicial: $1,000.00 | valor actual: $1,037.57 | P&L: $+37.57 (+3.76%)
- Efectivo libre: $417.53 | en ordenes abiertas: $414.49 (8) | en posiciones: $207.37 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 533 colocadas, 123 llenadas, 283 tocadas sin llenarse (sorteo 30%), 119 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 38 | 98.96c | 100.00% | 90.8-100.0% | +1.04 pts | $+20.03 | 0.28 |
| deportes_previo | 42 | 98.20c | 100.00% | 91.6-100.0% | +1.80 pts | $+38.93 | 0.34 |
| otros_cierre | 29 | 99.04c | 100.00% | 88.3-100.0% | +0.96 pts | $+14.49 | 0.39 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 119 | 98.45c | 99.11% | 95.4-99.9% | +0.65 pts | $+39.39 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.83 | 97.7c | 98.1c | deportes_previo |  | RB Ōmiya Ardija vs. Tokushima Vortis: O/U 6.5 |
| $51.86 | 99.8c | 96.6c | otros_cierre |  | Will Core PCE MoM be 0.1% in October? |
| $51.86 | 98.7c | 98.2c | cripto_cierre |  | Will the price of Bitcoin be less than $54,000 on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4971 | abiertas: 395 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1400 | 98.72c | 99.29% | +0.56 pts | +0.12 a +1.00 | 10 |
| cripto_cierre | tocadas | 986 | 98.56c | 98.99% | +0.43 pts | -0.20 a +1.05 | 10 |
| deportes_previo | todas | 2762 | 98.30c | 98.71% | +0.41 pts | -0.00 a +0.83 | 37 |
| deportes_previo | tocadas | 2302 | 98.28c | 98.72% | +0.44 pts | -0.01 a +0.89 | 31 |
| otros_cierre | todas | 717 | 98.88c | 99.44% | +0.56 pts | +0.01 a +1.11 | 4 |
| otros_cierre | tocadas | 450 | 98.72c | 99.11% | +0.40 pts | -0.48 a +1.27 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 4971 | 98.46c | 98.88% | +0.42 pts | +0.13 a +0.71 | 57 |
| TOTAL | tocadas | 3821 | 98.35c | 98.70% | +0.35 pts | -0.00 a +0.71 | 51 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Spread: Preston North End FC (-3.5)
- 99.2c -> pago 0.0 | deportes_previo | tocada | FC UTA Arad vs. Universitatea Craiova CS: O/U 7.5
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.9c -> pago 0.0 | deportes_previo | tocada | Dundee FC vs. Heart of Midlothian FC: O/U 7.5
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.8c -> pago 0.0 | deportes_previo | tocada | Spread: Charlton Athletic FC (-3.5)

## Veredicto

Aun no hay veredicto: van 119 operaciones cerradas en 13.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
