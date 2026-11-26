# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.4 de 28 | corridas: 310
- Capital inicial: $1,000.00 | valor actual: $957.71 | P&L: $-42.29 (-4.23%)
- Efectivo libre: $0.00 | en ordenes abiertas: $393.99 (5) | en posiciones: $616.77 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 618 colocadas, 281 llenadas, 266 tocadas sin llenarse (sorteo 30%), 66 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 78 | 98.83c | 100.00% | 95.3-100.0% | +1.17 pts | $+63.18 | 0.17 |
| deportes_previo | 140 | 98.06c | 97.38% | 93.9-99.3% | -0.68 pts | $-78.29 | 0.25 |
| otros_cierre | 46 | 99.61c | 100.00% | 92.3-100.0% | +0.39 pts | $+12.27 | 0.32 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 272 | 98.50c | 98.56% | 96.8-99.6% | +0.06 pts | $+10.76 | 0.26 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 81.3c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $19.30 | 95.9c | 99.4c | post_fin_90_97 |  | Will the highest temperature in Dallas be between 56-57°F on November 26? |
| $24.48 | 96.1c | 99.7c | deportes_previo |  | Will Kuopion PS win on 2026-11-26? |
| $98.38 | 96.3c | 98.3c | deportes_previo |  | Spread: Eagles (-10.5) |
| $86.78 | 99.7c | 99.7c | deportes_previo |  | Spread: Clube do Remo (-2.5) |
| $99.62 | 99.9c | 69.3c | deportes_previo |  | Games Total: O/U 2.5 |
| $73.81 | 99.9c | 90.0c | deportes_previo |  | Games Total: O/U 2.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16119 | abiertas: 2398 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4454 | 98.80c | 98.92% | +0.12 pts | -0.18 a +0.43 | 48 |
| clima_cierre | tocadas | 4146 | 98.82c | 98.84% | +0.02 pts | -0.30 a +0.35 | 48 |
| cripto_cierre | todas | 2085 | 98.62c | 98.08% | -0.54 pts | -1.12 a +0.05 | 40 |
| cripto_cierre | tocadas | 1900 | 98.67c | 97.89% | -0.77 pts | -1.41 a -0.14 | 40 |
| deportes_previo | todas | 7585 | 98.05c | 97.45% | -0.60 pts | -0.95 a -0.25 | 198 |
| deportes_previo | tocadas | 7384 | 98.09c | 97.41% | -0.69 pts | -1.05 a -0.33 | 196 |
| otros_cierre | todas | 1725 | 99.00c | 97.57% | -1.43 pts | -2.15 a -0.71 | 42 |
| otros_cierre | tocadas | 1573 | 98.95c | 97.33% | -1.62 pts | -2.41 a -0.83 | 42 |
| post_fin_90_97 | todas | 270 | 94.06c | 94.07% | +0.02 pts | -2.77 a +2.80 | 16 |
| post_fin_90_97 | tocadas | 229 | 94.16c | 93.01% | -1.15 pts | -4.41 a +2.12 | 16 |
| TOTAL | todas | 16119 | 98.37c | 97.89% | -0.47 pts | -0.69 a -0.25 | 344 |
| TOTAL | tocadas | 15232 | 98.39c | 97.78% | -0.61 pts | -0.84 a -0.38 | 342 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) finish week of November 16 above $270?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Amazon (AMZN) close at $245-$250 on the final day of trading of the week of Nov 16 – 

## Veredicto

Aun no hay veredicto: van 272 operaciones cerradas en 13.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
