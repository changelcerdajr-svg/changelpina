# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.4 de 28 | corridas: 115
- Capital inicial: $1,000.00 | valor actual: $1,038.66 | P&L: $+38.66 (+3.87%)
- Efectivo libre: $417.43 | en ordenes abiertas: $466.60 (9) | en posiciones: $155.08 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 201 colocadas, 55 llenadas, 91 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 15 | 98.74c | 100.00% | 79.6-100.0% | +1.26 pts | $+9.83 | 0.17 |
| deportes_previo | 20 | 98.39c | 100.00% | 83.9-100.0% | +1.61 pts | $+16.54 | 0.35 |
| otros_cierre | 14 | 99.02c | 100.00% | 78.5-100.0% | +0.98 pts | $+7.08 | 0.56 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 52 | 98.55c | 100.00% | 93.1-100.0% | +1.45 pts | $+39.11 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.67 | 98.2c | 97.0c | deportes_previo |  | Spread: Montserrat (-1.5) |
| $51.59 | 99.4c | 99.7c | otros_cierre |  | Will the next Gemini Flash-Lite model (3.6+) be released on November 17, 2026? |
| $51.82 | 98.5c | 98.6c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1907 | abiertas: 211 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 600 | 98.73c | 98.83% | +0.10 pts | -0.76 a +0.96 | 7 |
| cripto_cierre | tocadas | 418 | 98.58c | 98.33% | -0.26 pts | -1.49 a +0.97 | 7 |
| deportes_previo | todas | 977 | 98.39c | 99.08% | +0.68 pts | +0.08 a +1.28 | 9 |
| deportes_previo | tocadas | 822 | 98.35c | 99.15% | +0.80 pts | +0.17 a +1.43 | 7 |
| otros_cierre | todas | 311 | 98.72c | 100.00% | +1.28 pts | +1.20 a +1.36 | 0 |
| otros_cierre | tocadas | 208 | 98.63c | 100.00% | +1.37 pts | +1.27 a +1.47 | 0 |
| post_fin_95_97 | todas | 19 | 96.14c | 89.47% | -6.67 pts | -20.79 a +7.45 | 2 |
| post_fin_95_97 | tocadas | 16 | 96.08c | 87.50% | -8.58 pts | -25.26 a +8.10 | 2 |
| TOTAL | todas | 1907 | 98.53c | 99.06% | +0.52 pts | +0.09 a +0.96 | 18 |
| TOTAL | tocadas | 1464 | 98.43c | 98.91% | +0.48 pts | -0.05 a +1.01 | 16 |

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

Aun no hay veredicto: van 52 operaciones cerradas en 6.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
