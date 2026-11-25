# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 14.0 de 28 | corridas: 318
- Capital inicial: $1,000.00 | valor actual: $1,041.32 | P&L: $+41.32 (+4.13%)
- Efectivo libre: $417.53 | en ordenes abiertas: $467.95 (9) | en posiciones: $155.91 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 550 colocadas, 125 llenadas, 297 tocadas sin llenarse (sorteo 30%), 119 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 39 | 98.95c | 100.00% | 91.0-100.0% | +1.05 pts | $+20.71 | 0.28 |
| deportes_previo | 43 | 98.18c | 100.00% | 91.8-100.0% | +1.82 pts | $+40.15 | 0.34 |
| otros_cierre | 30 | 99.07c | 100.00% | 88.6-100.0% | +0.93 pts | $+14.60 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 122 | 98.46c | 99.13% | 95.5-99.9% | +0.67 pts | $+41.40 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.03 | 97.6c | 97.7c | otros_cierre |  | Will Amazon (AMZN) close above $250 on November 25? |
| $52.07 | 97.1c | 97.1c | deportes_previo |  | Blackhawks vs. Kraken: O/U 2.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5074 | abiertas: 421 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1453 | 98.73c | 99.31% | +0.58 pts | +0.16 a +1.01 | 10 |
| cripto_cierre | tocadas | 1018 | 98.56c | 99.02% | +0.46 pts | -0.15 a +1.07 | 10 |
| deportes_previo | todas | 2797 | 98.31c | 98.73% | +0.43 pts | +0.02 a +0.84 | 37 |
| deportes_previo | tocadas | 2332 | 98.28c | 98.73% | +0.46 pts | +0.01 a +0.90 | 31 |
| otros_cierre | todas | 732 | 98.88c | 99.45% | +0.57 pts | +0.03 a +1.11 | 4 |
| otros_cierre | tocadas | 460 | 98.71c | 99.13% | +0.42 pts | -0.44 a +1.27 | 4 |
| post_fin_95_97 | todas | 92 | 95.89c | 93.48% | -2.41 pts | -7.48 a +2.67 | 6 |
| post_fin_95_97 | tocadas | 83 | 95.91c | 92.77% | -3.14 pts | -8.74 a +2.47 | 6 |
| TOTAL | todas | 5074 | 98.47c | 98.91% | +0.44 pts | +0.16 a +0.72 | 57 |
| TOTAL | tocadas | 3893 | 98.35c | 98.73% | +0.38 pts | +0.03 a +0.72 | 51 |

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

Aun no hay veredicto: van 122 operaciones cerradas en 14.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
