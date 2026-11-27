# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 13.9 de 28 | corridas: 322
- Capital inicial: $1,000.00 | valor actual: $907.98 | P&L: $-92.02 (-9.20%)
- Efectivo libre: $0.00 | en ordenes abiertas: $553.46 (8) | en posiciones: $371.37 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 646 colocadas, 293 llenadas, 274 tocadas sin llenarse (sorteo 30%), 71 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 80 | 98.82c | 100.00% | 95.4-100.0% | +1.18 pts | $+65.56 | 0.17 |
| deportes_previo | 149 | 98.06c | 96.66% | 93.3-99.0% | -1.40 pts | $-168.07 | 0.25 |
| otros_cierre | 48 | 99.61c | 100.00% | 92.6-100.0% | +0.39 pts | $+12.91 | 0.32 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 286 | 98.49c | 98.15% | 96.5-99.5% | -0.34 pts | $-75.18 | 0.26 |

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
| $91.77 | 99.8c | 83.4c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $9.22 | 97.3c | 97.4c | deportes_previo |  | Spread: Melbourne City FC (-3.5) |
| $14.20 | 96.6c | 97.0c | deportes_previo |  | Macarthur FC vs. Melbourne City FC: O/U 6.5 |
| $89.65 | 97.6c | 97.8c | deportes_previo |  | Spread: Safa (-2.5) |
| $43.89 | 96.3c | 96.3c | deportes_previo |  | Spread: FK Kolos Kovalivka (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16626 | abiertas: 2576 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4651 | 98.80c | 98.95% | +0.15 pts | -0.14 a +0.44 | 49 |
| clima_cierre | tocadas | 4332 | 98.82c | 98.87% | +0.05 pts | -0.27 a +0.36 | 49 |
| cripto_cierre | todas | 2146 | 98.61c | 98.09% | -0.52 pts | -1.09 a +0.06 | 41 |
| cripto_cierre | tocadas | 1952 | 98.66c | 97.90% | -0.76 pts | -1.39 a -0.14 | 41 |
| deportes_previo | todas | 7814 | 98.04c | 97.37% | -0.67 pts | -1.02 a -0.32 | 210 |
| deportes_previo | tocadas | 7603 | 98.09c | 97.32% | -0.76 pts | -1.12 a -0.41 | 208 |
| otros_cierre | todas | 1737 | 98.99c | 97.58% | -1.41 pts | -2.13 a -0.69 | 42 |
| otros_cierre | tocadas | 1583 | 98.94c | 97.35% | -1.60 pts | -2.38 a -0.81 | 42 |
| post_fin_90_97 | todas | 278 | 94.00c | 93.88% | -0.11 pts | -2.90 a +2.68 | 17 |
| post_fin_90_97 | tocadas | 235 | 94.10c | 92.77% | -1.34 pts | -4.61 a +1.94 | 17 |
| TOTAL | todas | 16626 | 98.36c | 97.87% | -0.49 pts | -0.71 a -0.27 | 359 |
| TOTAL | tocadas | 15705 | 98.39c | 97.76% | -0.63 pts | -0.86 a -0.40 | 357 |

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

Aun no hay veredicto: van 286 operaciones cerradas en 13.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
