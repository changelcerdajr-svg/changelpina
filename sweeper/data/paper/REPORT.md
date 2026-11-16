# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 4.7 de 28 | corridas: 73
- Capital inicial: $1,000.00 | valor actual: $1,020.69 | P&L: $+20.69 (+2.07%)
- Efectivo libre: $414.42 | en ordenes abiertas: $252.15 (5) | en posiciones: $353.95 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 126 colocadas, 36 llenadas, 52 tocadas sin llenarse (sorteo 30%), 33 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 6 | 98.86c | 100.00% | 61.0-100.0% | +1.14 pts | $+3.48 | 0.24 |
| deportes_previo | 13 | 98.72c | 100.00% | 77.2-100.0% | +1.28 pts | $+8.49 | 0.35 |
| otros_cierre | 8 | 98.76c | 100.00% | 67.6-100.0% | +1.24 pts | $+5.07 | 0.65 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 29 | 98.62c | 100.00% | 88.3-100.0% | +1.38 pts | $+20.53 | 0.44 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.92 | 99.2c | 96.0c | otros_cierre |  | Will the USS Theodore Roosevelt arrive in CENTCOM by November 15, 2026? |
| $50.91 | 97.1c | 99.5c | deportes_previo |  | Namibia vs. Cameroon: O/U 5.5 |
| $50.92 | 98.8c | 97.8c | deportes_previo |  | Spread: Moldova (-2.5) |
| $51.03 | 99.5c | 99.5c | otros_cierre |  | Will "Ebenezer" score at least 50 on the Rotten Tomatoes Tomatometer? |
| $51.01 | 99.6c | 100.0c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 16? |
| $51.03 | 97.9c | 99.5c | deportes_previo |  | Will Somalia win on 2026-11-16? |
| $48.14 | 98.0c | 98.2c | deportes_previo |  | Spread: Celta Fortuna (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1143 | abiertas: 438 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 384 | 98.74c | 98.18% | -0.56 pts | -1.89 a +0.77 | 7 |
| cripto_cierre | tocadas | 272 | 98.63c | 97.43% | -1.21 pts | -3.08 a +0.67 | 7 |
| deportes_previo | todas | 553 | 98.44c | 98.55% | +0.11 pts | -0.88 a +1.11 | 8 |
| deportes_previo | tocadas | 465 | 98.38c | 98.71% | +0.32 pts | -0.70 a +1.35 | 6 |
| otros_cierre | todas | 191 | 98.62c | 100.00% | +1.38 pts | +1.27 a +1.48 | 0 |
| otros_cierre | tocadas | 132 | 98.52c | 100.00% | +1.48 pts | +1.36 a +1.61 | 0 |
| post_fin_95_97 | todas | 15 | 96.13c | 86.67% | -9.47 pts | -27.20 a +8.26 | 2 |
| post_fin_95_97 | tocadas | 12 | 96.05c | 83.33% | -12.72 pts | -34.66 a +9.23 | 2 |
| TOTAL | todas | 1143 | 98.54c | 98.51% | -0.03 pts | -0.73 a +0.67 | 17 |
| TOTAL | tocadas | 881 | 98.45c | 98.30% | -0.15 pts | -1.00 a +0.70 | 15 |

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

Aun no hay veredicto: van 29 operaciones cerradas en 4.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
