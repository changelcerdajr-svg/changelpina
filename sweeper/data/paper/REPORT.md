# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 7.8 de 28 | corridas: 154
- Capital inicial: $1,000.00 | valor actual: $1,046.43 | P&L: $+46.43 (+4.64%)
- Efectivo libre: $419.40 | en ordenes abiertas: $522.87 (10) | en posiciones: $104.13 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 269 colocadas, 64 llenadas, 127 tocadas sin llenarse (sorteo 30%), 68 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 18 | 98.82c | 100.00% | 82.4-100.0% | +1.18 pts | $+11.04 | 0.20 |
| deportes_previo | 23 | 98.36c | 100.00% | 85.7-100.0% | +1.64 pts | $+19.51 | 0.36 |
| otros_cierre | 17 | 99.08c | 100.00% | 81.6-100.0% | +0.92 pts | $+8.08 | 0.54 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 62 | 98.56c | 100.00% | 94.2-100.0% | +1.44 pts | $+46.40 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.6c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.31 | 99.5c | 99.5c | cripto_cierre |  | Will Bitcoin reach $68,000 on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2265 | abiertas: 306 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 787 | 98.74c | 99.11% | +0.37 pts | -0.28 a +1.02 | 7 |
| cripto_cierre | tocadas | 533 | 98.56c | 98.69% | +0.13 pts | -0.84 a +1.09 | 7 |
| deportes_previo | todas | 1085 | 98.37c | 99.08% | +0.71 pts | +0.14 a +1.28 | 10 |
| deportes_previo | tocadas | 908 | 98.32c | 99.12% | +0.79 pts | +0.19 a +1.40 | 8 |
| otros_cierre | todas | 366 | 98.75c | 99.73% | +0.97 pts | +0.43 a +1.52 | 1 |
| otros_cierre | tocadas | 238 | 98.65c | 99.58% | +0.93 pts | +0.09 a +1.76 | 1 |
| post_fin_95_97 | todas | 27 | 96.10c | 92.59% | -3.51 pts | -13.54 a +6.52 | 2 |
| post_fin_95_97 | tocadas | 22 | 96.12c | 90.91% | -5.21 pts | -17.46 a +7.04 | 2 |
| TOTAL | todas | 2265 | 98.53c | 99.12% | +0.58 pts | +0.20 a +0.97 | 20 |
| TOTAL | tocadas | 1701 | 98.42c | 98.94% | +0.53 pts | +0.04 a +1.01 | 18 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5
- 98.4c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 98.4c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 14?
- 98.3c -> pago 0.0 | deportes_previo | no tocada | Spread: Denmark (-2.5)
- 98.2c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 62 operaciones cerradas en 7.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
