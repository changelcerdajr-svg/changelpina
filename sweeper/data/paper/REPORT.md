# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 5.3 de 28 | corridas: 88
- Capital inicial: $1,000.00 | valor actual: $1,029.48 | P&L: $+29.48 (+2.95%)
- Efectivo libre: $361.78 | en ordenes abiertas: $411.09 (8) | en posiciones: $255.97 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 151 colocadas, 44 llenadas, 61 tocadas sin llenarse (sorteo 30%), 38 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 9 | 98.83c | 100.00% | 70.1-100.0% | +1.17 pts | $+5.40 | 0.22 |
| deportes_previo | 18 | 98.46c | 100.00% | 82.4-100.0% | +1.54 pts | $+14.21 | 0.33 |
| otros_cierre | 10 | 98.88c | 100.00% | 72.2-100.0% | +1.12 pts | $+5.74 | 0.62 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 39 | 98.56c | 100.00% | 91.0-100.0% | +1.44 pts | $+28.85 | 0.41 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.57 | 95.9c | 99.6c | post_fin_95_97 |  | Will the highest temperature in Atlanta be between 60-61°F on November 16? |
| $51.30 | 99.4c | 99.5c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 16, 2026? |
| $51.30 | 99.5c | 99.5c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 16, 2026? |
| $51.37 | 99.4c | 96.9c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 16, 2026? |
| $51.42 | 99.1c | 99.1c | otros_cierre |  | Will MrBeast's next video get less than 66 million views on day 3? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1503 | abiertas: 329 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 478 | 98.73c | 98.54% | -0.19 pts | -1.26 a +0.88 | 7 |
| cripto_cierre | tocadas | 339 | 98.61c | 97.94% | -0.67 pts | -2.18 a +0.84 | 7 |
| deportes_previo | todas | 764 | 98.47c | 98.82% | +0.35 pts | -0.41 a +1.11 | 9 |
| deportes_previo | tocadas | 641 | 98.40c | 98.91% | +0.51 pts | -0.29 a +1.31 | 7 |
| otros_cierre | todas | 243 | 98.65c | 100.00% | +1.35 pts | +1.26 a +1.45 | 0 |
| otros_cierre | tocadas | 166 | 98.55c | 100.00% | +1.45 pts | +1.34 a +1.57 | 0 |
| post_fin_95_97 | todas | 18 | 96.16c | 88.89% | -7.27 pts | -22.14 a +7.61 | 2 |
| post_fin_95_97 | tocadas | 15 | 96.09c | 86.67% | -9.43 pts | -27.17 a +8.31 | 2 |
| TOTAL | todas | 1503 | 98.55c | 98.80% | +0.25 pts | -0.30 a +0.80 | 18 |
| TOTAL | tocadas | 1161 | 98.45c | 98.62% | +0.17 pts | -0.49 a +0.84 | 16 |

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

Aun no hay veredicto: van 39 operaciones cerradas en 5.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
