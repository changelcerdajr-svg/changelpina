# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 10.1 de 28 | corridas: 217
- Capital inicial: $1,000.00 | valor actual: $1,067.49 | P&L: $+67.49 (+6.75%)
- Efectivo libre: $430.44 | en ordenes abiertas: $212.29 (4) | en posiciones: $423.65 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 367 colocadas, 92 llenadas, 187 tocadas sin llenarse (sorteo 30%), 84 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 23 | 98.91c | 100.00% | 85.7-100.0% | +1.09 pts | $+13.16 | 0.22 |
| deportes_previo | 33 | 98.26c | 100.00% | 89.6-100.0% | +1.74 pts | $+30.01 | 0.34 |
| otros_cierre | 22 | 99.06c | 100.00% | 85.1-100.0% | +0.94 pts | $+10.74 | 0.44 |
| post_fin_95_97 | 6 | 96.13c | 100.00% | 61.0-100.0% | +3.87 pts | $+12.47 | 0.55 |
| TOTAL | 84 | 98.49c | 100.00% | 95.6-100.0% | +1.51 pts | $+66.38 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $53.34 | 95.0c | 95.0c | post_fin_95_97 |  | Spread: Georgia State (-5.5) |
| $53.34 | 96.0c | 96.0c | post_fin_95_97 |  | Spread: North Dakota State (-23.5) |
| $53.07 | 98.1c | 98.9c | deportes_previo |  | Spread: Pumas de la UNAM (-3.5) |
| $53.03 | 99.2c | 99.3c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $53.03 | 99.2c | 99.4c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $52.99 | 97.9c | 98.8c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |
| $53.01 | 99.4c | 99.8c | cripto_cierre |  | Will Ethereum reach $1,900 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3292 | abiertas: 387 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 970 | 98.74c | 98.97% | +0.23 pts | -0.41 a +0.86 | 10 |
| cripto_cierre | tocadas | 654 | 98.57c | 98.47% | -0.10 pts | -1.04 a +0.84 | 10 |
| deportes_previo | todas | 1763 | 98.33c | 99.04% | +0.71 pts | +0.26 a +1.16 | 18 |
| deportes_previo | tocadas | 1483 | 98.29c | 98.99% | +0.70 pts | +0.20 a +1.20 | 16 |
| otros_cierre | todas | 530 | 98.80c | 99.25% | +0.44 pts | -0.30 a +1.18 | 4 |
| otros_cierre | tocadas | 358 | 98.70c | 98.88% | +0.19 pts | -0.91 a +1.28 | 4 |
| post_fin_95_97 | todas | 29 | 96.10c | 93.10% | -3.00 pts | -12.35 a +6.35 | 2 |
| post_fin_95_97 | tocadas | 24 | 96.12c | 91.67% | -4.45 pts | -15.70 a +6.80 | 2 |
| TOTAL | todas | 3292 | 98.51c | 99.00% | +0.49 pts | +0.15 a +0.83 | 34 |
| TOTAL | tocadas | 2519 | 98.40c | 98.77% | +0.37 pts | -0.05 a +0.80 | 32 |

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

Aun no hay veredicto: van 84 operaciones cerradas en 10.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
