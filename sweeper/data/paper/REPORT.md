# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.1 de 28 | corridas: 107
- Capital inicial: $1,000.00 | valor actual: $1,036.39 | P&L: $+36.39 (+3.64%)
- Efectivo libre: $415.94 | en ordenes abiertas: $413.86 (8) | en posiciones: $206.67 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 190 colocadas, 53 llenadas, 84 tocadas sin llenarse (sorteo 30%), 45 expiradas

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
| $51.67 | 98.3c | 98.1c | deportes_previo |  | Spread: Jamaica (-1.5) |
| $51.59 | 99.4c | 99.7c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 17, 2026? |
| $51.82 | 99.4c | 99.7c | cripto_cierre |  | Will Bitcoin reach $69,000 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1734 | abiertas: 309 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 551 | 98.73c | 98.73% | -0.00 pts | -0.93 a +0.93 | 7 |
| cripto_cierre | tocadas | 378 | 98.58c | 98.15% | -0.43 pts | -1.78 a +0.93 | 7 |
| deportes_previo | todas | 900 | 98.43c | 99.00% | +0.57 pts | -0.08 a +1.22 | 9 |
| deportes_previo | tocadas | 759 | 98.37c | 99.08% | +0.71 pts | +0.03 a +1.39 | 7 |
| otros_cierre | todas | 264 | 98.66c | 100.00% | +1.34 pts | +1.25 a +1.43 | 0 |
| otros_cierre | tocadas | 176 | 98.56c | 100.00% | +1.44 pts | +1.33 a +1.55 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1734 | 98.54c | 98.96% | +0.43 pts | -0.05 a +0.90 | 18 |
| TOTAL | tocadas | 1329 | 98.43c | 98.80% | +0.37 pts | -0.21 a +0.95 | 16 |

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

Aun no hay veredicto: van 49 operaciones cerradas en 6.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
