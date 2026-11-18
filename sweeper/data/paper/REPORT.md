# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.2 de 28 | corridas: 112
- Capital inicial: $1,000.00 | valor actual: $1,036.61 | P&L: $+36.61 (+3.66%)
- Efectivo libre: $416.57 | en ordenes abiertas: $362.77 (7) | en posiciones: $258.57 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 197 colocadas, 55 llenadas, 89 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 14 | 98.69c | 100.00% | 78.5-100.0% | +1.31 pts | $+9.51 | 0.16 |
| deportes_previo | 19 | 98.40c | 100.00% | 83.2-100.0% | +1.60 pts | $+15.65 | 0.34 |
| otros_cierre | 14 | 99.02c | 100.00% | 78.5-100.0% | +0.98 pts | $+7.08 | 0.56 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 50 | 98.53c | 100.00% | 92.9-100.0% | +1.47 pts | $+37.90 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.67 | 98.3c | 97.7c | deportes_previo |  | Spread: Jamaica (-1.5) |
| $51.67 | 98.2c | 97.0c | deportes_previo |  | Spread: Montserrat (-1.5) |
| $51.59 | 99.4c | 99.7c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 17, 2026? |
| $51.82 | 98.5c | 97.2c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.82 | 99.4c | 99.8c | cripto_cierre |  | Will Bitcoin reach $69,000 on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1832 | abiertas: 239 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 556 | 98.73c | 98.74% | +0.02 pts | -0.91 a +0.94 | 7 |
| cripto_cierre | tocadas | 382 | 98.57c | 98.17% | -0.40 pts | -1.74 a +0.94 | 7 |
| deportes_previo | todas | 958 | 98.40c | 99.06% | +0.66 pts | +0.05 a +1.27 | 9 |
| deportes_previo | tocadas | 807 | 98.35c | 99.13% | +0.78 pts | +0.14 a +1.42 | 7 |
| otros_cierre | todas | 299 | 98.71c | 100.00% | +1.29 pts | +1.21 a +1.38 | 0 |
| otros_cierre | tocadas | 198 | 98.62c | 100.00% | +1.38 pts | +1.28 a +1.49 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1832 | 98.53c | 99.02% | +0.49 pts | +0.04 a +0.94 | 18 |
| TOTAL | tocadas | 1403 | 98.42c | 98.86% | +0.44 pts | -0.11 a +0.99 | 16 |

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

Aun no hay veredicto: van 50 operaciones cerradas en 6.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
