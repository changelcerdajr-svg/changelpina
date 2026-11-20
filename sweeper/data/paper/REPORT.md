# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 8.3 de 28 | corridas: 167
- Capital inicial: $1,000.00 | valor actual: $1,048.83 | P&L: $+48.83 (+4.88%)
- Efectivo libre: $420.84 | en ordenes abiertas: $314.08 (6) | en posiciones: $313.62 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 289 colocadas, 71 llenadas, 143 tocadas sin llenarse (sorteo 30%), 69 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 18 | 98.82c | 100.00% | 82.4-100.0% | +1.18 pts | $+11.04 | 0.20 |
| deportes_previo | 24 | 98.30c | 100.00% | 86.2-100.0% | +1.70 pts | $+21.07 | 0.34 |
| otros_cierre | 19 | 99.12c | 100.00% | 83.2-100.0% | +0.88 pts | $+8.66 | 0.49 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 65 | 98.57c | 100.00% | 94.4-100.0% | +1.43 pts | $+48.55 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.37 | 99.3c | 99.4c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 19, 2026? |
| $52.31 | 99.5c | 99.8c | cripto_cierre |  | Will Bitcoin reach $68,000 on November 19? |
| $52.32 | 99.2c | 99.6c | cripto_cierre |  | Will Ethereum reach $1,950 on November 19? |
| $52.36 | 97.6c | 97.5c | deportes_previo |  | Western Sydney Wanderers FC vs. Adelaide United FC: O/U 7.5 |
| $52.44 | 97.7c | 97.7c | deportes_previo |  | Spread: SC Delhi (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2386 | abiertas: 394 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 802 | 98.73c | 99.13% | +0.40 pts | -0.25 a +1.04 | 7 |
| cripto_cierre | tocadas | 541 | 98.55c | 98.71% | +0.16 pts | -0.79 a +1.11 | 7 |
| deportes_previo | todas | 1175 | 98.36c | 99.15% | +0.79 pts | +0.26 a +1.31 | 10 |
| deportes_previo | tocadas | 976 | 98.32c | 99.18% | +0.86 pts | +0.30 a +1.43 | 8 |
| otros_cierre | todas | 382 | 98.76c | 98.95% | +0.20 pts | -0.83 a +1.22 | 4 |
| otros_cierre | tocadas | 252 | 98.66c | 98.41% | -0.25 pts | -1.80 a +1.31 | 4 |
| post_fin_95_97 | todas | 27 | 96.10c | 92.59% | -3.51 pts | -13.54 a +6.52 | 2 |
| post_fin_95_97 | tocadas | 22 | 96.12c | 90.91% | -5.21 pts | -17.46 a +7.04 | 2 |
| TOTAL | todas | 2386 | 98.52c | 99.04% | +0.51 pts | +0.12 a +0.90 | 23 |
| TOTAL | tocadas | 1791 | 98.41c | 98.83% | +0.42 pts | -0.08 a +0.92 | 21 |

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

Aun no hay veredicto: van 65 operaciones cerradas en 8.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
