# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 5.9 de 28 | corridas: 103
- Capital inicial: $1,000.00 | valor actual: $1,033.37 | P&L: $+33.37 (+3.34%)
- Efectivo libre: $413.65 | en ordenes abiertas: $464.80 (9) | en posiciones: $154.85 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 181 colocadas, 49 llenadas, 80 tocadas sin llenarse (sorteo 30%), 43 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 11 | 98.88c | 100.00% | 74.1-100.0% | +1.12 pts | $+6.34 | 0.19 |
| deportes_previo | 18 | 98.46c | 100.00% | 82.4-100.0% | +1.54 pts | $+14.21 | 0.33 |
| otros_cierre | 14 | 99.02c | 100.00% | 78.5-100.0% | +0.98 pts | $+7.08 | 0.56 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 46 | 98.60c | 100.00% | 92.3-100.0% | +1.40 pts | $+33.30 | 0.39 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.59 | 97.3c | 96.8c | deportes_previo |  | Rwanda vs. Mali: O/U 5.5 |
| $51.66 | 97.8c | 98.2c | cripto_cierre |  | SPY (SPY) Up or Down on November 17? |
| $51.59 | 99.4c | 99.7c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 17, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1646 | abiertas: 367 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 542 | 98.74c | 98.71% | -0.03 pts | -0.98 a +0.92 | 7 |
| cripto_cierre | tocadas | 375 | 98.58c | 98.13% | -0.45 pts | -1.82 a +0.92 | 7 |
| deportes_previo | todas | 821 | 98.46c | 98.90% | +0.44 pts | -0.27 a +1.15 | 9 |
| deportes_previo | tocadas | 685 | 98.40c | 98.98% | +0.58 pts | -0.17 a +1.33 | 7 |
| otros_cierre | todas | 264 | 98.66c | 100.00% | +1.34 pts | +1.25 a +1.43 | 0 |
| otros_cierre | tocadas | 176 | 98.56c | 100.00% | +1.44 pts | +1.33 a +1.55 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1646 | 98.56c | 98.91% | +0.35 pts | -0.15 a +0.85 | 18 |
| TOTAL | tocadas | 1252 | 98.45c | 98.72% | +0.27 pts | -0.34 a +0.89 | 16 |

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

Aun no hay veredicto: van 46 operaciones cerradas en 5.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
