# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 3.5 de 28 | corridas: 45
- Capital inicial: $1,000.00 | valor actual: $1,015.58 | P&L: $+15.58 (+1.56%)
- Efectivo libre: $406.59 | en ordenes abiertas: $507.79 (10) | en posiciones: $101.20 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 91 colocadas, 24 llenadas, 38 tocadas sin llenarse (sorteo 30%), 19 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 5 | 98.96c | 100.00% | 56.6-100.0% | +1.04 pts | $+2.65 | 0.27 |
| deportes_previo | 8 | 98.68c | 100.00% | 67.6-100.0% | +1.32 pts | $+5.40 | 0.43 |
| otros_cierre | 7 | 98.87c | 100.00% | 64.6-100.0% | +1.13 pts | $+4.03 | 0.67 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 22 | 98.62c | 100.00% | 85.1-100.0% | +1.38 pts | $+15.58 | 0.51 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.60 | 98.7c | 98.7c | deportes_previo |  | Spread: Bolivia (-2.5) |
| $50.60 | 99.4c | 99.4c | deportes_previo |  | Spread: Bolivia (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 944 | abiertas: 232 | abiertas mas de 7 dias despues de su fecha de fin: 0

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

Aun no hay veredicto: van 22 operaciones cerradas en 3.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
