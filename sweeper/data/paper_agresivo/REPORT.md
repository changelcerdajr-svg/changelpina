# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.4 de 28 | corridas: 69
- Capital inicial: $1,000.00 | valor actual: $861.29 | P&L: $-138.71 (-13.87%)
- Efectivo libre: $1.61 | en ordenes abiertas: $677.27 (8) | en posiciones: $186.01 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 163 colocadas, 70 llenadas, 65 tocadas sin llenarse (sorteo 30%), 20 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 23 | 98.99c | 100.00% | 85.7-100.0% | +1.01 pts | $+14.87 | 0.10 |
| deportes_previo | 25 | 98.15c | 90.00% | 75.0-97.8% | -8.15 pts | $-162.20 | 0.48 |
| otros_cierre | 15 | 99.61c | 100.00% | 79.6-100.0% | +0.39 pts | $+3.77 | 0.48 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 66 | 98.65c | 95.84% | 89.6-99.2% | -2.82 pts | $-135.10 | 0.37 |

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
| $5.56 | 99.3c | 99.3c | otros_cierre |  | Will MrBeast's next video get between 68 and 69 million views on day 3? |
| $29.57 | 99.9c | 99.9c | cripto_cierre |  | Natural Gas (NG) Up or Down on November 17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3833 | abiertas: 1812 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 963 | 99.01c | 99.27% | +0.27 pts | -0.27 a +0.80 | 7 |
| clima_cierre | tocadas | 882 | 98.99c | 99.21% | +0.22 pts | -0.36 a +0.80 | 7 |
| cripto_cierre | todas | 609 | 98.92c | 98.03% | -0.89 pts | -1.99 a +0.20 | 12 |
| cripto_cierre | tocadas | 561 | 98.96c | 97.86% | -1.09 pts | -2.28 a +0.09 | 12 |
| deportes_previo | todas | 1743 | 98.07c | 97.19% | -0.88 pts | -1.66 a -0.11 | 49 |
| deportes_previo | tocadas | 1704 | 98.11c | 97.12% | -0.99 pts | -1.78 a -0.20 | 49 |
| otros_cierre | todas | 478 | 99.30c | 99.37% | +0.07 pts | -0.64 a +0.78 | 3 |
| otros_cierre | tocadas | 430 | 99.27c | 99.30% | +0.04 pts | -0.75 a +0.82 | 3 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 3833 | 98.55c | 98.12% | -0.43 pts | -0.86 a -0.01 | 72 |
| TOTAL | tocadas | 3610 | 98.56c | 98.01% | -0.55 pts | -1.01 a -0.10 | 72 |

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

Aun no hay veredicto: van 66 operaciones cerradas en 4.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
