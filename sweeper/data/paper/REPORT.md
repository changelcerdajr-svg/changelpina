# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 3.9 de 28 | corridas: 52
- Capital inicial: $1,000.00 | valor actual: $1,017.77 | P&L: $+17.77 (+1.78%)
- Efectivo libre: $407.67 | en ordenes abiertas: $457.30 (9) | en posiciones: $152.42 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 103 colocadas, 28 llenadas, 47 tocadas sin llenarse (sorteo 30%), 19 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 6 | 98.86c | 100.00% | 61.0-100.0% | +1.14 pts | $+3.48 | 0.24 |
| deportes_previo | 10 | 98.75c | 100.00% | 72.2-100.0% | +1.25 pts | $+6.37 | 0.39 |
| otros_cierre | 7 | 98.87c | 100.00% | 64.6-100.0% | +1.13 pts | $+4.03 | 0.67 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 25 | 98.64c | 100.00% | 86.7-100.0% | +1.36 pts | $+17.38 | 0.47 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.78 | 98.1c | 98.1c | deportes_previo |  | Spread: Casertana FC (-3.5) |
| $50.77 | 99.0c | 99.1c | deportes_previo |  | Spread: Curaçao (-2.5) |
| $50.87 | 98.0c | 98.7c | otros_cierre |  | Next Astra Model (6.1+) released by November 15, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 944 | abiertas: 383 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 301 | 98.79c | 97.67% | -1.12 pts | -2.81 a +0.58 | 7 |
| cripto_cierre | tocadas | 214 | 98.71c | 96.73% | -1.98 pts | -4.36 a +0.39 | 7 |
| deportes_previo | todas | 467 | 98.43c | 98.50% | +0.07 pts | -1.03 a +1.17 | 7 |
| deportes_previo | tocadas | 381 | 98.36c | 98.69% | +0.32 pts | -0.82 a +1.47 | 5 |
| otros_cierre | todas | 169 | 98.56c | 100.00% | +1.44 pts | +1.33 a +1.55 | 0 |
| otros_cierre | tocadas | 122 | 98.46c | 100.00% | +1.54 pts | +1.41 a +1.66 | 0 |
| post_fin_95_97 | todas | 7 | 95.91c | 71.43% | -24.49 pts | -60.55 a +11.58 | 2 |
| post_fin_95_97 | tocadas | 7 | 95.91c | 71.43% | -24.49 pts | -60.55 a +11.58 | 2 |
| TOTAL | todas | 944 | 98.55c | 98.31% | -0.25 pts | -1.07 a +0.57 | 16 |
| TOTAL | tocadas | 724 | 98.46c | 98.07% | -0.39 pts | -1.39 a +0.60 | 14 |

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

Aun no hay veredicto: van 25 operaciones cerradas en 3.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
