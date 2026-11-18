# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 6.9 de 28 | corridas: 129
- Capital inicial: $1,000.00 | valor actual: $1,041.37 | P&L: $+41.37 (+4.14%)
- Efectivo libre: $313.26 | en ordenes abiertas: $624.48 (12) | en posiciones: $103.68 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 224 colocadas, 58 llenadas, 100 tocadas sin llenarse (sorteo 30%), 54 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 17 | 98.77c | 100.00% | 81.6-100.0% | +1.23 pts | $+10.88 | 0.19 |
| deportes_previo | 21 | 98.38c | 100.00% | 84.5-100.0% | +1.62 pts | $+17.49 | 0.34 |
| otros_cierre | 15 | 99.04c | 100.00% | 79.6-100.0% | +0.96 pts | $+7.40 | 0.58 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 56 | 98.57c | 100.00% | 93.6-100.0% | +1.43 pts | $+41.43 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $51.86 | 98.9c | 98.9c | deportes_previo |  | Jackson State Tigers vs. Baylor Bears |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2012 | abiertas: 263 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 673 | 98.74c | 98.96% | +0.22 pts | -0.55 a +0.98 | 7 |
| cripto_cierre | tocadas | 457 | 98.57c | 98.47% | -0.10 pts | -1.22 a +1.02 | 7 |
| deportes_previo | todas | 983 | 98.39c | 99.08% | +0.69 pts | +0.09 a +1.29 | 9 |
| deportes_previo | tocadas | 827 | 98.35c | 99.15% | +0.81 pts | +0.18 a +1.43 | 7 |
| otros_cierre | todas | 334 | 98.75c | 100.00% | +1.25 pts | +1.17 a +1.33 | 0 |
| otros_cierre | tocadas | 220 | 98.65c | 100.00% | +1.35 pts | +1.25 a +1.44 | 0 |
| post_fin_95_97 | todas | 22 | 96.07c | 90.91% | -5.16 pts | -17.41 a +7.10 | 2 |
| post_fin_95_97 | tocadas | 18 | 96.06c | 88.89% | -7.17 pts | -22.06 a +7.72 | 2 |
| TOTAL | todas | 2012 | 98.55c | 99.11% | +0.56 pts | +0.15 a +0.97 | 18 |
| TOTAL | tocadas | 1522 | 98.43c | 98.95% | +0.52 pts | +0.01 a +1.03 | 16 |

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

Aun no hay veredicto: van 56 operaciones cerradas en 6.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
