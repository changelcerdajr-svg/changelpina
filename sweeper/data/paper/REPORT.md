# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 4.0 de 28 | corridas: 55
- Capital inicial: $1,000.00 | valor actual: $1,018.32 | P&L: $+18.32 (+1.83%)
- Efectivo libre: $407.94 | en ordenes abiertas: $457.96 (9) | en posiciones: $152.47 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 108 colocadas, 29 llenadas, 47 tocadas sin llenarse (sorteo 30%), 23 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 6 | 98.86c | 100.00% | 61.0-100.0% | +1.14 pts | $+3.48 | 0.24 |
| deportes_previo | 11 | 98.69c | 100.00% | 74.1-100.0% | +1.31 pts | $+7.36 | 0.37 |
| otros_cierre | 7 | 98.87c | 100.00% | 64.6-100.0% | +1.13 pts | $+4.03 | 0.67 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 26 | 98.62c | 100.00% | 87.1-100.0% | +1.38 pts | $+18.36 | 0.46 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.83 | 98.8c | 98.8c | deportes_previo |  | Stetson Hatters vs. Clemson Tigers (W) |
| $50.77 | 99.0c | 97.9c | deportes_previo |  | Spread: Curaçao (-2.5) |
| $50.87 | 98.0c | 99.0c | otros_cierre |  | Next Astra Model (6.1+) released by November 15, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1000 | abiertas: 344 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 313 | 98.80c | 97.76% | -1.03 pts | -2.66 a +0.60 | 7 |
| cripto_cierre | tocadas | 221 | 98.71c | 96.83% | -1.88 pts | -4.18 a +0.43 | 7 |
| deportes_previo | todas | 511 | 98.46c | 98.43% | -0.02 pts | -1.10 a +1.05 | 8 |
| deportes_previo | tocadas | 424 | 98.40c | 98.58% | +0.19 pts | -0.93 a +1.31 | 6 |
| otros_cierre | todas | 169 | 98.56c | 100.00% | +1.44 pts | +1.33 a +1.55 | 0 |
| otros_cierre | tocadas | 122 | 98.46c | 100.00% | +1.54 pts | +1.41 a +1.66 | 0 |
| post_fin_95_97 | todas | 7 | 95.91c | 71.43% | -24.49 pts | -60.55 a +11.58 | 2 |
| post_fin_95_97 | tocadas | 7 | 95.91c | 71.43% | -24.49 pts | -60.55 a +11.58 | 2 |
| TOTAL | todas | 1000 | 98.56c | 98.30% | -0.26 pts | -1.06 a +0.53 | 17 |
| TOTAL | tocadas | 774 | 98.47c | 98.06% | -0.41 pts | -1.38 a +0.55 | 15 |

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

Aun no hay veredicto: van 26 operaciones cerradas en 4.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
