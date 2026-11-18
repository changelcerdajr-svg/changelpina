# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.6 de 28 | corridas: 122
- Capital inicial: $1,000.00 | valor actual: $1,040.68 | P&L: $+40.68 (+4.07%)
- Efectivo libre: $416.94 | en ordenes abiertas: $467.88 (9) | en posiciones: $155.55 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 209 colocadas, 57 llenadas, 92 tocadas sin llenarse (sorteo 30%), 51 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 15 | 98.74c | 100.00% | 79.6-100.0% | +1.26 pts | $+9.83 | 0.17 |
| deportes_previo | 21 | 98.38c | 100.00% | 84.5-100.0% | +1.62 pts | $+17.49 | 0.34 |
| otros_cierre | 15 | 99.04c | 100.00% | 79.6-100.0% | +0.96 pts | $+7.40 | 0.58 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 54 | 98.56c | 100.00% | 93.4-100.0% | +1.44 pts | $+40.37 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 99.1c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.86 | 99.8c | 99.9c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 18? |
| $51.86 | 98.9c | 98.8c | deportes_previo |  | Jackson State Tigers vs. Baylor Bears |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1938 | abiertas: 217 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 613 | 98.73c | 98.86% | +0.13 pts | -0.71 a +0.97 | 7 |
| cripto_cierre | tocadas | 429 | 98.57c | 98.37% | -0.20 pts | -1.40 a +0.99 | 7 |
| deportes_previo | todas | 983 | 98.39c | 99.08% | +0.69 pts | +0.09 a +1.29 | 9 |
| deportes_previo | tocadas | 827 | 98.35c | 99.15% | +0.81 pts | +0.18 a +1.43 | 7 |
| otros_cierre | todas | 323 | 98.74c | 100.00% | +1.26 pts | +1.18 a +1.34 | 0 |
| otros_cierre | tocadas | 215 | 98.65c | 100.00% | +1.35 pts | +1.25 a +1.44 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1938 | 98.54c | 99.07% | +0.54 pts | +0.11 a +0.96 | 18 |
| TOTAL | tocadas | 1487 | 98.43c | 98.92% | +0.49 pts | -0.03 a +1.01 | 16 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5
- 98.4c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 98.4c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 14?
- 98.3c -> pago 0.0 | deportes_previo | no tocada | Spread: Denmark (-2.5)
- 98.2c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.7c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $66,000 on November 14?

## Veredicto

Aun no hay veredicto: van 54 operaciones cerradas en 6.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
