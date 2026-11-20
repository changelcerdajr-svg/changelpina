# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 8.8 de 28 | corridas: 181
- Capital inicial: $1,000.00 | valor actual: $1,052.84 | P&L: $+52.84 (+5.28%)
- Efectivo libre: $370.91 | en ordenes abiertas: $472.68 (9) | en posiciones: $209.43 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 313 colocadas, 76 llenadas, 155 tocadas sin llenarse (sorteo 30%), 73 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 22 | 98.90c | 100.00% | 85.1-100.0% | +1.10 pts | $+12.63 | 0.23 |
| deportes_previo | 26 | 98.25c | 100.00% | 87.1-100.0% | +1.75 pts | $+23.60 | 0.35 |
| otros_cierre | 20 | 99.13c | 100.00% | 83.9-100.0% | +0.87 pts | $+9.03 | 0.47 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 72 | 98.59c | 100.00% | 94.9-100.0% | +1.41 pts | $+53.02 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.62 | 96.5c | 96.5c | post_fin_95_97 |  | Will the highest temperature in New York City be between 66-67°F on November 20? |
| $52.47 | 98.9c | 98.2c | deportes_previo |  | Spread: Ajman Club (-2.5) |
| $52.52 | 98.4c | 99.0c | otros_cierre |  | Will MrBeast's next video get between 87 and 88 million views on day 6? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2561 | abiertas: 596 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 897 | 98.74c | 99.22% | +0.48 pts | -0.10 a +1.05 | 7 |
| cripto_cierre | tocadas | 607 | 98.57c | 98.85% | +0.28 pts | -0.57 a +1.13 | 7 |
| deportes_previo | todas | 1229 | 98.36c | 99.10% | +0.74 pts | +0.23 a +1.26 | 12 |
| deportes_previo | tocadas | 1019 | 98.31c | 99.12% | +0.80 pts | +0.24 a +1.36 | 10 |
| otros_cierre | todas | 407 | 98.78c | 99.02% | +0.24 pts | -0.73 a +1.20 | 4 |
| otros_cierre | tocadas | 269 | 98.69c | 98.51% | -0.18 pts | -1.63 a +1.28 | 4 |
| post_fin_95_97 | todas | 28 | 96.09c | 92.86% | -3.23 pts | -12.91 a +6.45 | 2 |
| post_fin_95_97 | tocadas | 23 | 96.10c | 91.30% | -4.80 pts | -16.53 a +6.94 | 2 |
| TOTAL | todas | 2561 | 98.54c | 99.06% | +0.53 pts | +0.16 a +0.90 | 25 |
| TOTAL | tocadas | 1918 | 98.42c | 98.85% | +0.43 pts | -0.04 a +0.90 | 23 |

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

Aun no hay veredicto: van 72 operaciones cerradas en 8.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
