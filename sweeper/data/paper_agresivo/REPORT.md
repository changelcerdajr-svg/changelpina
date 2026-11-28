# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 14.5 de 28 | corridas: 339
- Capital inicial: $1,000.00 | valor actual: $922.92 | P&L: $-77.08 (-7.71%)
- Efectivo libre: $0.35 | en ordenes abiertas: $376.31 (6) | en posiciones: $565.28 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 678 colocadas, 310 llenadas, 286 tocadas sin llenarse (sorteo 30%), 76 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 84 | 98.84c | 100.00% | 95.6-100.0% | +1.16 pts | $+66.77 | 0.17 |
| deportes_previo | 160 | 98.04c | 96.85% | 93.7-99.0% | -1.20 pts | $-152.29 | 0.24 |
| otros_cierre | 49 | 99.62c | 100.00% | 92.7-100.0% | +0.38 pts | $+13.04 | 0.31 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 302 | 98.48c | 98.23% | 96.6-99.5% | -0.25 pts | $-58.06 | 0.25 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-99.67 | 97.3c | 0.0 | deportes_previo | Spread: CF Cruz Azul (-3.5) |
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.0c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $36.42 | 98.9c | 98.9c | deportes_previo |  | Villanova Wildcats vs. LSU Tigers (W) |
| $92.43 | 98.9c | 98.9c | deportes_previo |  | Penn State Nittany Lions vs. Baylor Bears (W) |
| $92.23 | 97.9c | 97.8c | deportes_previo |  | Penguins vs. Sabres: O/U 2.5 |
| $92.43 | 98.2c | 97.5c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 27, 2026? |
| $37.36 | 97.4c | 97.5c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 27, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 17587 | abiertas: 2636 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4899 | 98.80c | 99.00% | +0.20 pts | -0.08 a +0.48 | 49 |
| clima_cierre | tocadas | 4566 | 98.83c | 98.93% | +0.10 pts | -0.20 a +0.40 | 49 |
| cripto_cierre | todas | 2244 | 98.58c | 98.17% | -0.41 pts | -0.96 a +0.14 | 41 |
| cripto_cierre | tocadas | 2040 | 98.65c | 97.99% | -0.66 pts | -1.26 a -0.05 | 41 |
| deportes_previo | todas | 8149 | 98.05c | 97.40% | -0.64 pts | -0.98 a -0.30 | 216 |
| deportes_previo | tocadas | 7934 | 98.09c | 97.36% | -0.73 pts | -1.08 a -0.38 | 214 |
| otros_cierre | todas | 1999 | 98.92c | 97.75% | -1.18 pts | -1.82 a -0.53 | 45 |
| otros_cierre | tocadas | 1841 | 98.88c | 97.56% | -1.32 pts | -2.02 a -0.62 | 45 |
| post_fin_90_97 | todas | 296 | 94.05c | 93.24% | -0.80 pts | -3.63 a +2.02 | 20 |
| post_fin_90_97 | tocadas | 251 | 94.14c | 92.03% | -2.11 pts | -5.42 a +1.20 | 20 |
| TOTAL | todas | 17587 | 98.36c | 97.92% | -0.44 pts | -0.65 a -0.23 | 371 |
| TOTAL | tocadas | 16632 | 98.39c | 97.81% | -0.58 pts | -0.80 a -0.36 | 369 |

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

Aun no hay veredicto: van 302 operaciones cerradas en 14.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
