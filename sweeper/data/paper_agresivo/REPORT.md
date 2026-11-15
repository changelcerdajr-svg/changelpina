# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 1.9 de 28 | corridas: 8
- Capital inicial: $1,000.00 | valor actual: $908.58 | P&L: $-91.42 (-9.14%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $902.02 (10) | en posiciones: $6.55 (1)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 35 colocadas, 12 llenadas, 10 tocadas sin llenarse (sorteo 30%), 3 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 3 | 99.43c | 100.00% | 43.8-100.0% | +0.57 pts | $+1.72 | 0.11 |
| deportes_previo | 4 | 98.05c | 75.13% | 30.1-95.4% | -22.92 pts | $-93.76 | 1.83 |
| otros_cierre | 3 | 99.85c | 100.00% | 43.8-100.0% | +0.15 pts | $+0.32 | 1.16 |
| TOTAL | 11 | 99.00c | 90.16% | 62.3-98.4% | -8.84 pts | $-91.42 | 1.18 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $6.55 | 97.9c | 97.9c | otros_cierre |  | Will Apple (AAPL) hit (HIGH) $364 Week of November 9 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1288 | abiertas: 1405 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 254 | 98.97c | 99.21% | +0.24 pts | -0.83 a +1.32 | 2 |
| clima_cierre | tocadas | 227 | 98.89c | 99.12% | +0.23 pts | -0.97 a +1.43 | 2 |
| cripto_cierre | todas | 174 | 98.91c | 96.55% | -2.36 pts | -5.03 a +0.32 | 6 |
| cripto_cierre | tocadas | 155 | 98.96c | 96.13% | -2.83 pts | -5.83 a +0.16 | 6 |
| deportes_previo | todas | 580 | 97.99c | 95.34% | -2.65 pts | -4.36 a -0.94 | 27 |
| deportes_previo | tocadas | 567 | 98.04c | 95.24% | -2.80 pts | -4.55 a -1.06 | 27 |
| otros_cierre | todas | 272 | 99.43c | 99.63% | +0.20 pts | -0.52 a +0.92 | 1 |
| otros_cierre | tocadas | 262 | 99.42c | 99.62% | +0.19 pts | -0.56 a +0.94 | 1 |
| post_fin_90_97 | todas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| post_fin_90_97 | tocadas | 8 | 94.79c | 100.00% | +5.21 pts | +4.59 a +5.84 | 0 |
| TOTAL | todas | 1288 | 98.59c | 97.20% | -1.39 pts | -2.28 a -0.50 | 36 |
| TOTAL | tocadas | 1219 | 98.59c | 97.05% | -1.55 pts | -2.49 a -0.60 | 36 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?
- 98.7c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 98.7c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Chongqing be 22°C on November 14?

## Veredicto

Aun no hay veredicto: van 11 operaciones cerradas en 1.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
