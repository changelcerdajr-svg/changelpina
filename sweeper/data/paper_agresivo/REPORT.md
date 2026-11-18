# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.5 de 28 | corridas: 72
- Capital inicial: $1,000.00 | valor actual: $865.49 | P&L: $-134.51 (-13.45%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $370.80 (5) | en posiciones: $495.11 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 168 colocadas, 75 llenadas, 67 tocadas sin llenarse (sorteo 30%), 21 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 25 | 99.00c | 100.00% | 86.7-100.0% | +1.00 pts | $+15.85 | 0.10 |
| deportes_previo | 25 | 98.15c | 90.00% | 75.0-97.8% | -8.15 pts | $-162.20 | 0.48 |
| otros_cierre | 16 | 99.61c | 100.00% | 80.6-100.0% | +0.39 pts | $+3.81 | 0.48 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 69 | 98.67c | 95.94% | 90.0-99.2% | -2.72 pts | $-134.09 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $85.88 | 97.2c | 97.2c | deportes_previo |  | Will Dominican Republic win on 2026-11-17? |
| $85.88 | 95.0c | 95.0c | deportes_previo |  | Dominican Republic leading at halftime? |
| $86.13 | 96.1c | 99.7c | deportes_previo |  | Tennessee Volunteers vs. Belmont Bruins (W) |
| $86.34 | 98.4c | 98.4c | deportes_previo |  | Spread: Jamaica (-1.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3932 | abiertas: 1836 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1030 | 99.00c | 99.32% | +0.32 pts | -0.18 a +0.82 | 7 |
| clima_cierre | tocadas | 942 | 98.98c | 99.26% | +0.28 pts | -0.27 a +0.82 | 7 |
| cripto_cierre | todas | 611 | 98.92c | 98.04% | -0.88 pts | -1.97 a +0.21 | 12 |
| cripto_cierre | tocadas | 563 | 98.95c | 97.87% | -1.08 pts | -2.26 a +0.10 | 12 |
| deportes_previo | todas | 1772 | 98.07c | 97.23% | -0.84 pts | -1.60 a -0.08 | 49 |
| deportes_previo | tocadas | 1733 | 98.11c | 97.17% | -0.94 pts | -1.72 a -0.16 | 49 |
| otros_cierre | todas | 479 | 99.30c | 99.37% | +0.07 pts | -0.64 a +0.78 | 3 |
| otros_cierre | tocadas | 431 | 99.27c | 99.30% | +0.04 pts | -0.75 a +0.82 | 3 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 3932 | 98.56c | 98.17% | -0.39 pts | -0.80 a +0.03 | 72 |
| TOTAL | tocadas | 3702 | 98.56c | 98.06% | -0.51 pts | -0.95 a -0.07 | 72 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 99.4c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Austin be between 62-63°F on November 16?
- 99.2c -> pago 0.0 | otros_cierre | tocada | Will Home Depot (HD) Q3 comparable sales growth be from 2% to under 2.25%?

## Veredicto

Aun no hay veredicto: van 69 operaciones cerradas en 4.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
