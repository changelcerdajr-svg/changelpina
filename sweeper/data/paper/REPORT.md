# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 7.2 de 28 | corridas: 139
- Capital inicial: $1,000.00 | valor actual: $1,042.79 | P&L: $+42.79 (+4.28%)
- Efectivo libre: $364.71 | en ordenes abiertas: $521.26 (10) | en posiciones: $156.03 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 240 colocadas, 60 llenadas, 111 tocadas sin llenarse (sorteo 30%), 59 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 17 | 98.77c | 100.00% | 81.6-100.0% | +1.23 pts | $+10.88 | 0.19 |
| deportes_previo | 22 | 98.41c | 100.00% | 85.1-100.0% | +1.59 pts | $+18.06 | 0.35 |
| otros_cierre | 15 | 99.04c | 100.00% | 79.6-100.0% | +0.96 pts | $+7.40 | 0.58 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 57 | 98.58c | 100.00% | 93.7-100.0% | +1.42 pts | $+42.00 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.7c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.07 | 96.1c | 97.4c | post_fin_95_97 |  | Will the highest temperature in Seattle be between 54-55°F on November 18? |
| $52.14 | 99.2c | 99.2c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 18, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2087 | abiertas: 240 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 681 | 98.74c | 98.97% | +0.23 pts | -0.52 a +0.99 | 7 |
| cripto_cierre | tocadas | 462 | 98.56c | 98.48% | -0.07 pts | -1.18 a +1.04 | 7 |
| deportes_previo | todas | 1043 | 98.38c | 99.14% | +0.76 pts | +0.19 a +1.32 | 9 |
| deportes_previo | tocadas | 875 | 98.33c | 99.20% | +0.87 pts | +0.28 a +1.46 | 7 |
| otros_cierre | todas | 341 | 98.75c | 100.00% | +1.25 pts | +1.17 a +1.33 | 0 |
| otros_cierre | tocadas | 225 | 98.65c | 100.00% | +1.35 pts | +1.25 a +1.45 | 0 |
| post_fin_95_97 | todas | 22 | 96.07c | 90.91% | -5.16 pts | -17.41 a +7.10 | 2 |
| post_fin_95_97 | tocadas | 18 | 96.06c | 88.89% | -7.17 pts | -22.06 a +7.72 | 2 |
| TOTAL | todas | 2087 | 98.53c | 99.14% | +0.60 pts | +0.21 a +1.00 | 18 |
| TOTAL | tocadas | 1580 | 98.42c | 98.99% | +0.57 pts | +0.08 a +1.06 | 16 |

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

Aun no hay veredicto: van 57 operaciones cerradas en 7.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
