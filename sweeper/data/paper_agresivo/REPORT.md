# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 14.2 de 28 | corridas: 330
- Capital inicial: $1,000.00 | valor actual: $913.26 | P&L: $-86.74 (-8.67%)
- Efectivo libre: $0.00 | en ordenes abiertas: $167.33 (3) | en posiciones: $762.99 (11)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 656 colocadas, 302 llenadas, 277 tocadas sin llenarse (sorteo 30%), 74 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 81 | 98.81c | 100.00% | 95.5-100.0% | +1.19 pts | $+66.40 | 0.17 |
| deportes_previo | 153 | 98.05c | 96.70% | 93.5-99.0% | -1.35 pts | $-163.42 | 0.25 |
| otros_cierre | 48 | 99.61c | 100.00% | 92.6-100.0% | +0.39 pts | $+12.91 | 0.32 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 291 | 98.48c | 98.17% | 96.5-99.5% | -0.31 pts | $-69.69 | 0.25 |

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
| $91.77 | 99.8c | 81.4c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.56 | 98.3c | 98.7c | deportes_previo |  | Spread: Al-Sailiya SC (-2.5) |
| $88.11 | 96.2c | 100.0c | deportes_previo |  | Al-Sailiya SC vs. Al Gharafa SC: O/U 0.5 |
| $45.26 | 98.8c | 98.5c | deportes_previo |  | Spread: Zira FK (-2.5) |
| $91.63 | 97.9c | 97.2c | deportes_previo |  | Spread: PFC Slavia Sofia (-2.5) |
| $52.95 | 97.3c | 97.2c | deportes_previo |  | Spread: FC Lokomotiv 1929 Sofia (-3.5) |
| $88.73 | 99.8c | 98.6c | cripto_cierre |  | Will the price of Bitcoin be between $54,000 and $56,000 on November 27? |
| $10.94 | 99.7c | 99.0c | cripto_cierre |  | Will the price of Bitcoin be between $56,000 and $58,000 on November 27? |
| $82.41 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Bitcoin be between $52,000 and $54,000 on November 27? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 16815 | abiertas: 2915 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4756 | 98.80c | 98.97% | +0.17 pts | -0.12 a +0.46 | 49 |
| clima_cierre | tocadas | 4431 | 98.82c | 98.89% | +0.07 pts | -0.24 a +0.38 | 49 |
| cripto_cierre | todas | 2157 | 98.60c | 98.10% | -0.50 pts | -1.07 a +0.07 | 41 |
| cripto_cierre | tocadas | 1957 | 98.66c | 97.90% | -0.76 pts | -1.38 a -0.13 | 41 |
| deportes_previo | todas | 7884 | 98.04c | 97.38% | -0.66 pts | -1.01 a -0.31 | 211 |
| deportes_previo | tocadas | 7671 | 98.09c | 97.33% | -0.75 pts | -1.11 a -0.40 | 209 |
| otros_cierre | todas | 1738 | 98.99c | 97.58% | -1.41 pts | -2.12 a -0.69 | 42 |
| otros_cierre | tocadas | 1584 | 98.94c | 97.35% | -1.60 pts | -2.38 a -0.81 | 42 |
| post_fin_90_97 | todas | 280 | 94.01c | 93.93% | -0.08 pts | -2.85 a +2.69 | 17 |
| post_fin_90_97 | tocadas | 236 | 94.11c | 92.80% | -1.31 pts | -4.57 a +1.95 | 17 |
| TOTAL | todas | 16815 | 98.36c | 97.89% | -0.47 pts | -0.69 a -0.26 | 360 |
| TOTAL | tocadas | 15879 | 98.39c | 97.77% | -0.62 pts | -0.84 a -0.39 | 358 |

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

Aun no hay veredicto: van 291 operaciones cerradas en 14.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
