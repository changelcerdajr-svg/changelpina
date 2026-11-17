# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 5.1 de 28 | corridas: 81
- Capital inicial: $1,000.00 | valor actual: $1,028.24 | P&L: $+28.24 (+2.82%)
- Efectivo libre: $364.45 | en ordenes abiertas: $508.66 (10) | en posiciones: $153.18 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 141 colocadas, 40 llenadas, 57 tocadas sin llenarse (sorteo 30%), 34 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 8 | 98.94c | 100.00% | 67.6-100.0% | +1.06 pts | $+4.35 | 0.24 |
| deportes_previo | 17 | 98.54c | 100.00% | 81.6-100.0% | +1.46 pts | $+12.70 | 0.35 |
| otros_cierre | 10 | 98.88c | 100.00% | 72.2-100.0% | +1.12 pts | $+5.74 | 0.62 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 37 | 98.62c | 100.00% | 90.6-100.0% | +1.38 pts | $+26.29 | 0.43 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.57 | 95.9c | 99.6c | post_fin_95_97 |  | Will the highest temperature in Atlanta be between 60-61°F on November 16? |
| $51.30 | 99.4c | 99.5c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 16, 2026? |
| $51.30 | 99.5c | 99.5c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 16, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1335 | abiertas: 352 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 440 | 98.72c | 98.41% | -0.31 pts | -1.47 a +0.86 | 7 |
| cripto_cierre | tocadas | 309 | 98.59c | 97.73% | -0.86 pts | -2.51 a +0.80 | 7 |
| deportes_previo | todas | 657 | 98.43c | 98.63% | +0.20 pts | -0.69 a +1.08 | 9 |
| deportes_previo | tocadas | 561 | 98.38c | 98.75% | +0.37 pts | -0.55 a +1.29 | 7 |
| otros_cierre | todas | 220 | 98.65c | 100.00% | +1.35 pts | +1.25 a +1.45 | 0 |
| otros_cierre | tocadas | 147 | 98.55c | 100.00% | +1.45 pts | +1.33 a +1.57 | 0 |
| post_fin_95_97 | todas | 18 | 96.16c | 88.89% | -7.27 pts | -22.14 a +7.61 | 2 |
| post_fin_95_97 | tocadas | 15 | 96.09c | 86.67% | -9.43 pts | -27.17 a +8.31 | 2 |
| TOTAL | todas | 1335 | 98.53c | 98.65% | +0.12 pts | -0.50 a +0.73 | 18 |
| TOTAL | tocadas | 1032 | 98.43c | 98.45% | +0.02 pts | -0.73 a +0.77 | 16 |

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

Aun no hay veredicto: van 37 operaciones cerradas en 5.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
