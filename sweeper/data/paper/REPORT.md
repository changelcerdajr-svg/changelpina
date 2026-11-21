# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 9.4 de 28 | corridas: 197
- Capital inicial: $1,000.00 | valor actual: $1,060.46 | P&L: $+60.46 (+6.05%)
- Efectivo libre: $426.96 | en ordenes abiertas: $528.82 (10) | en posiciones: $104.57 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 336 colocadas, 81 llenadas, 167 tocadas sin llenarse (sorteo 30%), 78 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 22 | 98.90c | 100.00% | 85.1-100.0% | +1.10 pts | $+12.63 | 0.23 |
| deportes_previo | 30 | 98.26c | 100.00% | 88.6-100.0% | +1.74 pts | $+27.30 | 0.34 |
| otros_cierre | 22 | 99.06c | 100.00% | 85.1-100.0% | +0.94 pts | $+10.74 | 0.44 |
| post_fin_95_97 | 5 | 96.36c | 100.00% | 56.6-100.0% | +3.64 pts | $+9.68 | 0.65 |
| TOTAL | 79 | 98.54c | 100.00% | 95.4-100.0% | +1.46 pts | $+60.35 | 0.36 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.75 | 97.1c | 97.5c | deportes_previo |  | Gençlerbirliği SK vs. Gaziantep FK: O/U 6.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2994 | abiertas: 388 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 961 | 98.75c | 98.96% | +0.21 pts | -0.43 a +0.85 | 10 |
| cripto_cierre | tocadas | 651 | 98.57c | 98.46% | -0.11 pts | -1.05 a +0.84 | 10 |
| deportes_previo | todas | 1475 | 98.34c | 99.19% | +0.85 pts | +0.40 a +1.30 | 13 |
| deportes_previo | tocadas | 1229 | 98.29c | 99.19% | +0.89 pts | +0.41 a +1.38 | 11 |
| otros_cierre | todas | 529 | 98.80c | 99.24% | +0.44 pts | -0.30 a +1.19 | 4 |
| otros_cierre | tocadas | 357 | 98.69c | 98.88% | +0.19 pts | -0.91 a +1.28 | 4 |
| post_fin_95_97 | todas | 29 | 96.10c | 93.10% | -3.00 pts | -12.35 a +6.35 | 2 |
| post_fin_95_97 | tocadas | 24 | 96.12c | 91.67% | -4.45 pts | -15.70 a +6.80 | 2 |
| TOTAL | todas | 2994 | 98.53c | 99.06% | +0.54 pts | +0.19 a +0.88 | 29 |
| TOTAL | tocadas | 2261 | 98.41c | 98.85% | +0.44 pts | +0.00 a +0.87 | 27 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $56,000 on November 20?
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5

## Veredicto

Aun no hay veredicto: van 79 operaciones cerradas en 9.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
