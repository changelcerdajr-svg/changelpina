# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.0 de 28 | corridas: 106
- Capital inicial: $1,000.00 | valor actual: $1,036.20 | P&L: $+36.20 (+3.62%)
- Efectivo libre: $416.17 | en ordenes abiertas: $413.63 (8) | en posiciones: $206.67 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 188 colocadas, 53 llenadas, 83 tocadas sin llenarse (sorteo 30%), 44 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 14 | 98.69c | 100.00% | 78.5-100.0% | +1.31 pts | $+9.51 | 0.16 |
| deportes_previo | 18 | 98.46c | 100.00% | 82.4-100.0% | +1.54 pts | $+14.21 | 0.33 |
| otros_cierre | 14 | 99.02c | 100.00% | 78.5-100.0% | +0.98 pts | $+7.08 | 0.56 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 49 | 98.56c | 100.00% | 92.7-100.0% | +1.44 pts | $+36.47 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.59 | 97.3c | 96.8c | deportes_previo |  | Rwanda vs. Mali: O/U 5.5 |
| $51.67 | 98.3c | 98.0c | deportes_previo |  | Spread: Jamaica (-1.5) |
| $51.59 | 99.4c | 99.7c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 17, 2026? |
| $51.82 | 99.4c | 99.4c | cripto_cierre |  | Will Bitcoin reach $69,000 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1720 | abiertas: 313 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 544 | 98.73c | 98.71% | -0.02 pts | -0.96 a +0.92 | 7 |
| cripto_cierre | tocadas | 376 | 98.58c | 98.14% | -0.44 pts | -1.81 a +0.92 | 7 |
| deportes_previo | todas | 893 | 98.43c | 98.99% | +0.56 pts | -0.10 a +1.21 | 9 |
| deportes_previo | tocadas | 752 | 98.37c | 99.07% | +0.69 pts | +0.01 a +1.38 | 7 |
| otros_cierre | todas | 264 | 98.66c | 100.00% | +1.34 pts | +1.25 a +1.43 | 0 |
| otros_cierre | tocadas | 176 | 98.56c | 100.00% | +1.44 pts | +1.33 a +1.55 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1720 | 98.54c | 98.95% | +0.42 pts | -0.06 a +0.89 | 18 |
| TOTAL | tocadas | 1320 | 98.43c | 98.79% | +0.36 pts | -0.23 a +0.95 | 16 |

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

Aun no hay veredicto: van 49 operaciones cerradas en 6.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
