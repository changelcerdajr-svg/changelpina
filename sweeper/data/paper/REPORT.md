# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 8.7 de 28 | corridas: 177
- Capital inicial: $1,000.00 | valor actual: $1,050.39 | P&L: $+50.39 (+5.04%)
- Efectivo libre: $421.99 | en ordenes abiertas: $367.23 (7) | en posiciones: $261.66 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 305 colocadas, 74 llenadas, 151 tocadas sin llenarse (sorteo 30%), 73 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 20 | 98.88c | 100.00% | 83.9-100.0% | +1.12 pts | $+11.73 | 0.23 |
| deportes_previo | 25 | 98.28c | 100.00% | 86.7-100.0% | +1.72 pts | $+22.36 | 0.34 |
| otros_cierre | 20 | 99.13c | 100.00% | 83.9-100.0% | +0.87 pts | $+9.03 | 0.47 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 69 | 98.58c | 100.00% | 94.7-100.0% | +1.42 pts | $+50.89 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.44 | 97.7c | 98.3c | deportes_previo |  | Spread: SC Delhi (-2.5) |
| $52.47 | 98.9c | 98.0c | deportes_previo |  | Spread: Ajman Club (-2.5) |
| $52.47 | 99.1c | 99.2c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 20? |
| $52.47 | 99.2c | 98.6c | cripto_cierre |  | Will the price of Bitcoin be between $66,000 and $68,000 on November 20? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2481 | abiertas: 567 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 848 | 98.72c | 99.17% | +0.45 pts | -0.16 a +1.06 | 7 |
| cripto_cierre | tocadas | 574 | 98.55c | 98.78% | +0.23 pts | -0.67 a +1.12 | 7 |
| deportes_previo | todas | 1206 | 98.37c | 99.09% | +0.72 pts | +0.20 a +1.25 | 12 |
| deportes_previo | tocadas | 997 | 98.32c | 99.10% | +0.78 pts | +0.21 a +1.35 | 10 |
| otros_cierre | todas | 399 | 98.77c | 99.00% | +0.23 pts | -0.76 a +1.21 | 4 |
| otros_cierre | tocadas | 263 | 98.67c | 98.48% | -0.19 pts | -1.68 a +1.30 | 4 |
| post_fin_95_97 | todas | 28 | 96.09c | 92.86% | -3.23 pts | -12.91 a +6.45 | 2 |
| post_fin_95_97 | tocadas | 23 | 96.10c | 91.30% | -4.80 pts | -16.53 a +6.94 | 2 |
| TOTAL | todas | 2481 | 98.53c | 99.03% | +0.51 pts | +0.12 a +0.89 | 25 |
| TOTAL | tocadas | 1857 | 98.41c | 98.82% | +0.40 pts | -0.08 a +0.89 | 23 |

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

Aun no hay veredicto: van 69 operaciones cerradas en 8.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
