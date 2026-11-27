# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 16.1 de 28 | corridas: 374
- Capital inicial: $1,000.00 | valor actual: $1,002.74 | P&L: $+2.74 (+0.27%)
- Efectivo libre: $403.00 | en ordenes abiertas: $493.70 (10) | en posiciones: $106.03 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $51.82 en 1 posiciones
- Ordenes virtuales: 642 colocadas, 141 llenadas, 350 tocadas sin llenarse (sorteo 30%), 141 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 42 | 98.98c | 100.00% | 91.6-100.0% | +1.02 pts | $+21.81 | 0.28 |
| deportes_previo | 53 | 98.10c | 98.04% | 90.1-99.7% | -0.06 pts | $-2.10 | 0.32 |
| otros_cierre | 33 | 99.00c | 100.00% | 89.6-100.0% | +1.00 pts | $+17.09 | 0.38 |
| post_fin_95_97 | 10 | 95.96c | 89.69% | 59.6-98.2% | -6.27 pts | $-34.07 | 0.39 |
| TOTAL | 138 | 98.43c | 98.48% | 94.9-99.6% | +0.06 pts | $+2.73 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |
| $-52.40 | 97.0c | 0.0 | deportes_previo | Spread: CF Cruz Azul (-3.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $5.51 | 98.5c | 98.7c | deportes_previo |  | Spread: Manta FC (-2.5) |
| $48.70 | 97.3c | 97.5c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 27, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5898 | abiertas: 469 | abiertas mas de 7 dias despues de su fecha de fin: 5

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1684 | 98.72c | 99.35% | +0.63 pts | +0.25 a +1.01 | 11 |
| cripto_cierre | tocadas | 1168 | 98.54c | 99.06% | +0.51 pts | -0.04 a +1.07 | 11 |
| deportes_previo | todas | 3309 | 98.31c | 98.69% | +0.38 pts | -0.00 a +0.76 | 45 |
| deportes_previo | tocadas | 2713 | 98.27c | 98.62% | +0.35 pts | -0.09 a +0.78 | 39 |
| otros_cierre | todas | 799 | 98.86c | 99.37% | +0.51 pts | -0.04 a +1.06 | 5 |
| otros_cierre | tocadas | 517 | 98.69c | 99.03% | +0.35 pts | -0.50 a +1.19 | 5 |
| post_fin_95_97 | todas | 106 | 95.91c | 91.51% | -4.40 pts | -9.73 a +0.94 | 9 |
| post_fin_95_97 | tocadas | 94 | 95.92c | 90.43% | -5.50 pts | -11.48 a +0.48 | 9 |
| TOTAL | todas | 5898 | 98.46c | 98.84% | +0.38 pts | +0.11 a +0.65 | 70 |
| TOTAL | tocadas | 4492 | 98.34c | 98.61% | +0.27 pts | -0.07 a +0.61 | 64 |

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

Aun no hay veredicto: van 138 operaciones cerradas en 16.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
