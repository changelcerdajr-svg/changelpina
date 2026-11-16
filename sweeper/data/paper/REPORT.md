# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 5.0 de 28 | corridas: 78
- Capital inicial: $1,000.00 | valor actual: $1,026.09 | P&L: $+26.09 (+2.61%)
- Efectivo libre: $367.65 | en ordenes abiertas: $456.31 (9) | en posiciones: $200.26 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 135 colocadas, 38 llenadas, 54 tocadas sin llenarse (sorteo 30%), 34 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 7 | 98.97c | 100.00% | 64.6-100.0% | +1.03 pts | $+3.68 | 0.26 |
| deportes_previo | 16 | 98.57c | 100.00% | 80.6-100.0% | +1.43 pts | $+11.72 | 0.34 |
| otros_cierre | 9 | 98.84c | 100.00% | 70.1-100.0% | +1.16 pts | $+5.33 | 0.58 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 34 | 98.61c | 100.00% | 89.8-100.0% | +1.39 pts | $+24.23 | 0.42 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.92 | 99.2c | 100.0c | otros_cierre |  | Will the USS Theodore Roosevelt arrive in CENTCOM by November 15, 2026? |
| $50.57 | 95.9c | 99.6c | post_fin_95_97 |  | Will the highest temperature in Atlanta be between 60-61°F on November 16? |
| $48.14 | 98.0c | 98.4c | deportes_previo |  | Spread: Celta Fortuna (-2.5) |
| $50.64 | 98.7c | 97.5c | cripto_cierre |  | Amazon (AMZN) Up or Down on November 16? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1252 | abiertas: 409 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 432 | 98.73c | 98.38% | -0.35 pts | -1.54 a +0.83 | 7 |
| cripto_cierre | tocadas | 303 | 98.61c | 97.69% | -0.92 pts | -2.61 a +0.77 | 7 |
| deportes_previo | todas | 600 | 98.45c | 98.67% | +0.21 pts | -0.70 a +1.13 | 8 |
| deportes_previo | tocadas | 507 | 98.40c | 98.82% | +0.41 pts | -0.53 a +1.35 | 6 |
| otros_cierre | todas | 204 | 98.64c | 100.00% | +1.36 pts | +1.26 a +1.47 | 0 |
| otros_cierre | tocadas | 136 | 98.51c | 100.00% | +1.49 pts | +1.36 a +1.61 | 0 |
| post_fin_95_97 | todas | 16 | 96.12c | 87.50% | -8.62 pts | -25.29 a +8.05 | 2 |
| post_fin_95_97 | tocadas | 13 | 96.04c | 84.62% | -11.42 pts | -31.77 a +8.92 | 2 |
| TOTAL | todas | 1252 | 98.55c | 98.64% | +0.09 pts | -0.54 a +0.73 | 17 |
| TOTAL | tocadas | 959 | 98.45c | 98.44% | -0.02 pts | -0.80 a +0.77 | 15 |

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

Aun no hay veredicto: van 34 operaciones cerradas en 5.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
