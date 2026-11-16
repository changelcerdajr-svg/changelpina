# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 4.4 de 28 | corridas: 65
- Capital inicial: $1,000.00 | valor actual: $1,020.76 | P&L: $+20.76 (+2.08%)
- Efectivo libre: $409.17 | en ordenes abiertas: $560.44 (11) | en posiciones: $50.92 (1)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 117 colocadas, 30 llenadas, 48 tocadas sin llenarse (sorteo 30%), 28 expiradas

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
| $50.92 | 99.2c | 99.7c | otros_cierre |  | Will the USS Theodore Roosevelt arrive in CENTCOM by November 15, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1113 | abiertas: 365 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 364 | 98.77c | 98.08% | -0.69 pts | -2.10 a +0.71 | 7 |
| cripto_cierre | tocadas | 257 | 98.67c | 97.28% | -1.39 pts | -3.37 a +0.59 | 7 |
| deportes_previo | todas | 551 | 98.45c | 98.55% | +0.10 pts | -0.90 a +1.10 | 8 |
| deportes_previo | tocadas | 463 | 98.39c | 98.70% | +0.32 pts | -0.71 a +1.34 | 6 |
| otros_cierre | todas | 190 | 98.62c | 100.00% | +1.38 pts | +1.28 a +1.49 | 0 |
| otros_cierre | tocadas | 131 | 98.51c | 100.00% | +1.49 pts | +1.37 a +1.62 | 0 |
| post_fin_95_97 | todas | 8 | 95.96c | 75.00% | -20.96 pts | -52.95 a +11.03 | 2 |
| post_fin_95_97 | tocadas | 8 | 95.96c | 75.00% | -20.96 pts | -52.95 a +11.03 | 2 |
| TOTAL | todas | 1113 | 98.56c | 98.47% | -0.09 pts | -0.81 a +0.63 | 17 |
| TOTAL | tocadas | 859 | 98.47c | 98.25% | -0.21 pts | -1.08 a +0.66 | 15 |

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

Aun no hay veredicto: van 29 operaciones cerradas en 4.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
