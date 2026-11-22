# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 10.4 de 28 | corridas: 225
- Capital inicial: $1,000.00 | valor actual: $1,021.81 | P&L: $+21.81 (+2.18%)
- Efectivo libre: $397.46 | en ordenes abiertas: $464.38 (9) | en posiciones: $159.20 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 379 colocadas, 95 llenadas, 189 tocadas sin llenarse (sorteo 30%), 86 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 26 | 98.90c | 100.00% | 87.1-100.0% | +1.10 pts | $+15.05 | 0.28 |
| deportes_previo | 34 | 98.26c | 100.00% | 89.8-100.0% | +1.74 pts | $+31.04 | 0.34 |
| otros_cierre | 23 | 99.07c | 100.00% | 85.7-100.0% | +0.93 pts | $+11.17 | 0.45 |
| post_fin_95_97 | 9 | 95.96c | 88.56% | 56.5-98.0% | -7.40 pts | $-36.21 | 0.38 |
| TOTAL | 92 | 98.41c | 98.87% | 94.1-99.8% | +0.45 pts | $+21.04 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-53.71 | 95.9c | 0.0 | post_fin_95_97 | San Diego State vs. Boise State |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $53.66 | 98.1c | 99.8c | otros_cierre |  | Will xQc finish GTA VI by November 22, 3:59 AM ET? |
| $53.71 | 99.0c | 98.9c | cripto_cierre |  | Will Bitcoin reach $66,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3395 | abiertas: 676 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 1001 | 98.73c | 99.00% | +0.27 pts | -0.34 a +0.89 | 10 |
| cripto_cierre | tocadas | 683 | 98.56c | 98.54% | -0.02 pts | -0.92 a +0.88 | 10 |
| deportes_previo | todas | 1830 | 98.31c | 99.02% | +0.70 pts | +0.26 a +1.15 | 19 |
| deportes_previo | tocadas | 1541 | 98.27c | 98.96% | +0.69 pts | +0.19 a +1.19 | 17 |
| otros_cierre | todas | 535 | 98.81c | 99.25% | +0.44 pts | -0.29 a +1.18 | 4 |
| otros_cierre | tocadas | 359 | 98.70c | 98.89% | +0.19 pts | -0.91 a +1.28 | 4 |
| post_fin_95_97 | todas | 29 | 96.10c | 93.10% | -3.00 pts | -12.35 a +6.35 | 2 |
| post_fin_95_97 | tocadas | 24 | 96.12c | 91.67% | -4.45 pts | -15.70 a +6.80 | 2 |
| TOTAL | todas | 3395 | 98.49c | 99.00% | +0.50 pts | +0.17 a +0.84 | 35 |
| TOTAL | tocadas | 2607 | 98.39c | 98.77% | +0.39 pts | -0.03 a +0.81 | 33 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.9c -> pago 0.0 | deportes_previo | tocada | Dundee FC vs. Heart of Midlothian FC: O/U 7.5
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $56,000 on November 20?
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?

## Veredicto

Aun no hay veredicto: van 92 operaciones cerradas en 10.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
