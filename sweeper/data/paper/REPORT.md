# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.3 de 28 | corridas: 114
- Capital inicial: $1,000.00 | valor actual: $1,037.29 | P&L: $+37.29 (+3.73%)
- Efectivo libre: $416.80 | en ordenes abiertas: $414.66 (8) | en posiciones: $206.75 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 200 colocadas, 55 llenadas, 91 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 15 | 98.74c | 100.00% | 79.6-100.0% | +1.26 pts | $+9.83 | 0.17 |
| deportes_previo | 19 | 98.40c | 100.00% | 83.2-100.0% | +1.60 pts | $+15.65 | 0.34 |
| otros_cierre | 14 | 99.02c | 100.00% | 78.5-100.0% | +0.98 pts | $+7.08 | 0.56 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 51 | 98.55c | 100.00% | 93.0-100.0% | +1.45 pts | $+38.22 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.67 | 98.3c | 97.7c | deportes_previo |  | Spread: Jamaica (-1.5) |
| $51.67 | 98.2c | 97.0c | deportes_previo |  | Spread: Montserrat (-1.5) |
| $51.59 | 99.4c | 99.7c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 17, 2026? |
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1896 | abiertas: 214 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 599 | 98.74c | 98.83% | +0.10 pts | -0.76 a +0.95 | 7 |
| cripto_cierre | tocadas | 417 | 98.59c | 98.32% | -0.26 pts | -1.49 a +0.97 | 7 |
| deportes_previo | todas | 970 | 98.40c | 99.07% | +0.68 pts | +0.07 a +1.28 | 9 |
| deportes_previo | tocadas | 817 | 98.35c | 99.14% | +0.80 pts | +0.17 a +1.43 | 7 |
| otros_cierre | todas | 308 | 98.72c | 100.00% | +1.28 pts | +1.20 a +1.36 | 0 |
| otros_cierre | tocadas | 206 | 98.63c | 100.00% | +1.37 pts | +1.26 a +1.47 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1896 | 98.53c | 99.05% | +0.52 pts | +0.08 a +0.95 | 18 |
| TOTAL | tocadas | 1456 | 98.43c | 98.90% | +0.47 pts | -0.06 a +1.00 | 16 |

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

Aun no hay veredicto: van 51 operaciones cerradas en 6.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
