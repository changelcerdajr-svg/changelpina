# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 8.5 de 28 | corridas: 173
- Capital inicial: $1,000.00 | valor actual: $1,048.02 | P&L: $+48.02 (+4.80%)
- Efectivo libre: $421.24 | en ordenes abiertas: $419.27 (8) | en posiciones: $209.09 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 301 colocadas, 72 llenadas, 149 tocadas sin llenarse (sorteo 30%), 72 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 20 | 98.88c | 100.00% | 83.9-100.0% | +1.12 pts | $+11.73 | 0.23 |
| deportes_previo | 24 | 98.30c | 100.00% | 86.2-100.0% | +1.70 pts | $+21.07 | 0.34 |
| otros_cierre | 20 | 99.13c | 100.00% | 83.9-100.0% | +0.87 pts | $+9.03 | 0.47 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 68 | 98.60c | 100.00% | 94.7-100.0% | +1.40 pts | $+49.60 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.36 | 97.6c | 95.0c | deportes_previo |  | Western Sydney Wanderers FC vs. Adelaide United FC: O/U 7.5 |
| $52.44 | 97.7c | 97.7c | deportes_previo |  | Spread: SC Delhi (-2.5) |
| $52.47 | 99.1c | 98.9c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 20? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2466 | abiertas: 488 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 847 | 98.72c | 99.17% | +0.45 pts | -0.16 a +1.06 | 7 |
| cripto_cierre | tocadas | 573 | 98.55c | 98.78% | +0.23 pts | -0.67 a +1.12 | 7 |
| deportes_previo | todas | 1194 | 98.37c | 99.08% | +0.71 pts | +0.18 a +1.24 | 12 |
| deportes_previo | tocadas | 992 | 98.32c | 99.09% | +0.77 pts | +0.20 a +1.35 | 10 |
| otros_cierre | todas | 397 | 98.77c | 98.99% | +0.23 pts | -0.76 a +1.22 | 4 |
| otros_cierre | tocadas | 262 | 98.67c | 98.47% | -0.20 pts | -1.69 a +1.30 | 4 |
| post_fin_95_97 | todas | 28 | 96.09c | 92.86% | -3.23 pts | -12.91 a +6.45 | 2 |
| post_fin_95_97 | tocadas | 23 | 96.10c | 91.30% | -4.80 pts | -16.53 a +6.94 | 2 |
| TOTAL | todas | 2466 | 98.53c | 99.03% | +0.50 pts | +0.12 a +0.88 | 25 |
| TOTAL | tocadas | 1850 | 98.41c | 98.81% | +0.40 pts | -0.09 a +0.88 | 23 |

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

Aun no hay veredicto: van 68 operaciones cerradas en 8.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
