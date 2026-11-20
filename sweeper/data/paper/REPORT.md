# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 8.3 de 28 | corridas: 168
- Capital inicial: $1,000.00 | valor actual: $1,049.18 | P&L: $+49.18 (+4.92%)
- Efectivo libre: $421.24 | en ordenes abiertas: $419.00 (8) | en posiciones: $208.99 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 291 colocadas, 71 llenadas, 143 tocadas sin llenarse (sorteo 30%), 69 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 20 | 98.88c | 100.00% | 83.9-100.0% | +1.12 pts | $+11.73 | 0.23 |
| deportes_previo | 24 | 98.30c | 100.00% | 86.2-100.0% | +1.70 pts | $+21.07 | 0.34 |
| otros_cierre | 19 | 99.12c | 100.00% | 83.2-100.0% | +0.88 pts | $+8.66 | 0.49 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 67 | 98.59c | 100.00% | 94.6-100.0% | +1.41 pts | $+49.23 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.37 | 99.3c | 99.4c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 19, 2026? |
| $52.36 | 97.6c | 97.5c | deportes_previo |  | Western Sydney Wanderers FC vs. Adelaide United FC: O/U 7.5 |
| $52.44 | 97.7c | 97.8c | deportes_previo |  | Spread: SC Delhi (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2433 | abiertas: 392 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 838 | 98.73c | 99.16% | +0.44 pts | -0.18 a +1.05 | 7 |
| cripto_cierre | tocadas | 569 | 98.55c | 98.77% | +0.22 pts | -0.69 a +1.12 | 7 |
| deportes_previo | todas | 1184 | 98.37c | 99.16% | +0.79 pts | +0.27 a +1.31 | 10 |
| deportes_previo | tocadas | 984 | 98.32c | 99.19% | +0.87 pts | +0.31 a +1.43 | 8 |
| otros_cierre | todas | 384 | 98.76c | 98.96% | +0.20 pts | -0.83 a +1.22 | 4 |
| otros_cierre | tocadas | 254 | 98.67c | 98.43% | -0.24 pts | -1.79 a +1.30 | 4 |
| post_fin_95_97 | todas | 27 | 96.10c | 92.59% | -3.51 pts | -13.54 a +6.52 | 2 |
| post_fin_95_97 | tocadas | 22 | 96.12c | 90.91% | -5.21 pts | -17.46 a +7.04 | 2 |
| TOTAL | todas | 2433 | 98.53c | 99.05% | +0.53 pts | +0.14 a +0.91 | 23 |
| TOTAL | tocadas | 1829 | 98.41c | 98.85% | +0.44 pts | -0.05 a +0.93 | 21 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5
- 98.4c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 98.4c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 14?

## Veredicto

Aun no hay veredicto: van 67 operaciones cerradas en 8.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
