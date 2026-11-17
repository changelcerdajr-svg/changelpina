# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.4 de 28 | corridas: 68
- Capital inicial: $1,000.00 | valor actual: $858.82 | P&L: $-141.18 (-14.12%)
- Efectivo libre: $0.00 | en ordenes abiertas: $620.46 (8) | en posiciones: $241.97 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 161 colocadas, 69 llenadas, 64 tocadas sin llenarse (sorteo 30%), 20 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 23 | 98.99c | 100.00% | 85.7-100.0% | +1.01 pts | $+14.87 | 0.10 |
| deportes_previo | 24 | 98.19c | 89.53% | 74.2-97.7% | -8.66 pts | $-164.67 | 0.49 |
| otros_cierre | 15 | 99.61c | 100.00% | 79.6-100.0% | +0.39 pts | $+3.77 | 0.48 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 65 | 98.68c | 95.76% | 89.5-99.2% | -2.92 pts | $-137.57 | 0.38 |

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
| $85.53 | 97.2c | 97.2c | deportes_previo |  | Denmark vs. Norway: Neither team to score first? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3735 | abiertas: 1868 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 941 | 99.02c | 99.26% | +0.24 pts | -0.31 a +0.78 | 7 |
| clima_cierre | tocadas | 863 | 99.00c | 99.19% | +0.19 pts | -0.40 a +0.79 | 7 |
| cripto_cierre | todas | 603 | 98.95c | 98.01% | -0.94 pts | -2.04 a +0.16 | 12 |
| cripto_cierre | tocadas | 556 | 98.98c | 97.84% | -1.14 pts | -2.33 a +0.06 | 12 |
| deportes_previo | todas | 1695 | 98.07c | 97.11% | -0.96 pts | -1.76 a -0.17 | 49 |
| deportes_previo | tocadas | 1656 | 98.11c | 97.04% | -1.07 pts | -1.89 a -0.26 | 49 |
| otros_cierre | todas | 456 | 99.28c | 99.34% | +0.06 pts | -0.68 a +0.80 | 3 |
| otros_cierre | tocadas | 411 | 99.25c | 99.27% | +0.02 pts | -0.80 a +0.84 | 3 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 3735 | 98.56c | 98.07% | -0.49 pts | -0.92 a -0.05 | 72 |
| TOTAL | tocadas | 3519 | 98.56c | 97.95% | -0.61 pts | -1.07 a -0.15 | 72 |

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

Aun no hay veredicto: van 65 operaciones cerradas en 4.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
