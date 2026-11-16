# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 5.0 de 28 | corridas: 80
- Capital inicial: $1,000.00 | valor actual: $1,027.45 | P&L: $+27.45 (+2.74%)
- Efectivo libre: $366.74 | en ordenes abiertas: $457.25 (9) | en posiciones: $201.32 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 140 colocadas, 40 llenadas, 57 tocadas sin llenarse (sorteo 30%), 34 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 8 | 98.94c | 100.00% | 67.6-100.0% | +1.06 pts | $+4.35 | 0.24 |
| deportes_previo | 16 | 98.57c | 100.00% | 80.6-100.0% | +1.43 pts | $+11.72 | 0.34 |
| otros_cierre | 10 | 98.88c | 100.00% | 72.2-100.0% | +1.12 pts | $+5.74 | 0.62 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 36 | 98.63c | 100.00% | 90.4-100.0% | +1.37 pts | $+25.30 | 0.43 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.57 | 95.9c | 99.6c | post_fin_95_97 |  | Will the highest temperature in Atlanta be between 60-61°F on November 16? |
| $48.14 | 98.0c | 98.4c | deportes_previo |  | Spread: Celta Fortuna (-2.5) |
| $51.30 | 99.4c | 99.5c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 16, 2026? |
| $51.30 | 99.5c | 99.5c | otros_cierre |  | Will GPT Astra 6.1+ be released on November 16, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1321 | abiertas: 361 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 439 | 98.72c | 98.41% | -0.32 pts | -1.48 a +0.85 | 7 |
| cripto_cierre | tocadas | 308 | 98.59c | 97.73% | -0.87 pts | -2.53 a +0.79 | 7 |
| deportes_previo | todas | 647 | 98.44c | 98.61% | +0.17 pts | -0.74 a +1.07 | 9 |
| deportes_previo | tocadas | 551 | 98.39c | 98.73% | +0.34 pts | -0.59 a +1.27 | 7 |
| otros_cierre | todas | 218 | 98.65c | 100.00% | +1.35 pts | +1.25 a +1.45 | 0 |
| otros_cierre | tocadas | 147 | 98.55c | 100.00% | +1.45 pts | +1.33 a +1.57 | 0 |
| post_fin_95_97 | todas | 17 | 96.16c | 88.24% | -7.93 pts | -23.65 a +7.79 | 2 |
| post_fin_95_97 | tocadas | 14 | 96.10c | 85.71% | -10.39 pts | -29.33 a +8.56 | 2 |
| TOTAL | todas | 1321 | 98.54c | 98.64% | +0.10 pts | -0.52 a +0.72 | 18 |
| TOTAL | tocadas | 1020 | 98.44c | 98.43% | -0.01 pts | -0.77 a +0.75 | 16 |

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

Aun no hay veredicto: van 36 operaciones cerradas en 5.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
