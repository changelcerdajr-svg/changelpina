# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 9.1 de 28 | corridas: 190
- Capital inicial: $1,000.00 | valor actual: $1,054.98 | P&L: $+54.98 (+5.50%)
- Efectivo libre: $372.16 | en ordenes abiertas: $474.29 (9) | en posiciones: $209.78 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 327 colocadas, 80 llenadas, 163 tocadas sin llenarse (sorteo 30%), 75 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 22 | 98.90c | 100.00% | 85.1-100.0% | +1.10 pts | $+12.63 | 0.23 |
| deportes_previo | 28 | 98.28c | 100.00% | 87.9-100.0% | +1.72 pts | $+25.09 | 0.34 |
| otros_cierre | 22 | 99.06c | 100.00% | 85.1-100.0% | +0.94 pts | $+10.74 | 0.44 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 76 | 98.58c | 100.00% | 95.2-100.0% | +1.42 pts | $+56.22 | 0.36 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.62 | 96.5c | 94.7c | post_fin_95_97 |  | Will the highest temperature in New York City be between 66-67°F on November 20? |
| $52.67 | 97.0c | 96.9c | deportes_previo |  | FC Juárez vs. Atlas FC: O/U 6.5 |
| $52.67 | 98.9c | 98.8c | deportes_previo |  | FC Juárez vs. Atlas FC: O/U 7.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2762 | abiertas: 495 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 903 | 98.74c | 99.22% | +0.49 pts | -0.09 a +1.06 | 7 |
| cripto_cierre | tocadas | 611 | 98.56c | 98.85% | +0.29 pts | -0.55 a +1.13 | 7 |
| deportes_previo | todas | 1390 | 98.34c | 99.14% | +0.79 pts | +0.32 a +1.27 | 13 |
| deportes_previo | tocadas | 1156 | 98.30c | 99.13% | +0.84 pts | +0.32 a +1.36 | 11 |
| otros_cierre | todas | 441 | 98.79c | 99.09% | +0.31 pts | -0.59 a +1.20 | 4 |
| otros_cierre | tocadas | 296 | 98.69c | 98.65% | -0.04 pts | -1.37 a +1.28 | 4 |
| post_fin_95_97 | todas | 28 | 96.09c | 92.86% | -3.23 pts | -12.91 a +6.45 | 2 |
| post_fin_95_97 | tocadas | 23 | 96.10c | 91.30% | -4.80 pts | -16.53 a +6.94 | 2 |
| TOTAL | todas | 2762 | 98.52c | 99.09% | +0.57 pts | +0.22 a +0.92 | 26 |
| TOTAL | tocadas | 2086 | 98.41c | 98.90% | +0.49 pts | +0.05 a +0.93 | 24 |

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

Aun no hay veredicto: van 76 operaciones cerradas en 9.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
