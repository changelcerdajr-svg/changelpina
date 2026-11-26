# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 14.2 de 28 | corridas: 326
- Capital inicial: $1,000.00 | valor actual: $1,036.30 | P&L: $+36.30 (+3.63%)
- Efectivo libre: $418.89 | en ordenes abiertas: $364.69 (7) | en posiciones: $260.21 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 561 colocadas, 129 llenadas, 304 tocadas sin llenarse (sorteo 30%), 121 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 39 | 98.95c | 100.00% | 91.0-100.0% | +1.05 pts | $+20.71 | 0.28 |
| deportes_previo | 44 | 98.18c | 100.00% | 92.0-100.0% | +1.82 pts | $+41.26 | 0.33 |
| otros_cierre | 31 | 99.02c | 100.00% | 89.0-100.0% | +0.98 pts | $+15.88 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 124 | 98.45c | 99.14% | 95.6-99.9% | +0.70 pts | $+43.79 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.07 | 97.1c | 82.7c | deportes_previo |  | Blackhawks vs. Kraken: O/U 2.5 |
| $52.07 | 97.4c | 97.4c | deportes_previo |  | Sharks vs. Ducks: O/U 2.5 |
| $52.13 | 99.3c | 99.3c | cripto_cierre |  | Will Ethereum reach $1,850 on November 25? |
| $52.13 | 99.1c | 99.8c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 25? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5216 | abiertas: 317 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1457 | 98.72c | 99.25% | +0.52 pts | +0.08 a +0.96 | 11 |
| cripto_cierre | tocadas | 1022 | 98.55c | 98.92% | +0.37 pts | -0.26 a +1.00 | 11 |
| deportes_previo | todas | 2931 | 98.31c | 98.79% | +0.48 pts | +0.09 a +0.87 | 37 |
| deportes_previo | tocadas | 2421 | 98.28c | 98.78% | +0.50 pts | +0.07 a +0.94 | 31 |
| otros_cierre | todas | 736 | 98.88c | 99.46% | +0.57 pts | +0.04 a +1.11 | 4 |
| otros_cierre | tocadas | 462 | 98.71c | 99.13% | +0.42 pts | -0.43 a +1.27 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 5216 | 98.46c | 98.92% | +0.46 pts | +0.18 a +0.73 | 58 |
| TOTAL | tocadas | 3988 | 98.35c | 98.73% | +0.38 pts | +0.04 a +0.73 | 52 |

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

Aun no hay veredicto: van 124 operaciones cerradas en 14.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
