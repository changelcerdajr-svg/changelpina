# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.4 de 28 | corridas: 150
- Capital inicial: $1,000.00 | valor actual: $921.39 | P&L: $-78.61 (-7.86%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $345.53 (4) | en posiciones: $591.20 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 313 colocadas, 139 llenadas, 133 tocadas sin llenarse (sorteo 30%), 37 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 39 | 98.82c | 100.00% | 91.0-100.0% | +1.18 pts | $+31.97 | 0.16 |
| deportes_previo | 57 | 98.04c | 95.46% | 88.1-99.0% | -2.58 pts | $-113.69 | 0.33 |
| otros_cierre | 30 | 99.67c | 100.00% | 88.6-100.0% | +0.33 pts | $+6.86 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 131 | 98.59c | 97.95% | 94.6-99.6% | -0.64 pts | $-63.27 | 0.30 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $91.13 | 97.9c | 87.2c | deportes_previo |  | Spread: Real Murcia CF (-2.5) |
| $14.22 | 98.9c | 98.8c | cripto_cierre |  | Silver (XAGUSD) Up or Down on November 20? |
| $87.47 | 98.9c | 98.9c | cripto_cierre |  | Gold (XAUUSD) Up or Down on November 20? |
| $91.99 | 99.9c | 99.9c | deportes_previo |  | Games Total: O/U 2.5 |
| $91.99 | 97.8c | 97.8c | deportes_previo |  | Spread: CD Unión La Calera (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 7353 | abiertas: 2786 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2151 | 98.86c | 99.12% | +0.25 pts | -0.14 a +0.65 | 19 |
| clima_cierre | tocadas | 1980 | 98.88c | 99.04% | +0.16 pts | -0.27 a +0.58 | 19 |
| cripto_cierre | todas | 1120 | 98.71c | 98.21% | -0.50 pts | -1.26 a +0.27 | 20 |
| cripto_cierre | tocadas | 1029 | 98.75c | 98.06% | -0.69 pts | -1.52 a +0.14 | 20 |
| deportes_previo | todas | 2971 | 98.07c | 97.39% | -0.68 pts | -1.24 a -0.11 | 80 |
| deportes_previo | tocadas | 2902 | 98.10c | 97.33% | -0.77 pts | -1.35 a -0.19 | 80 |
| otros_cierre | todas | 1034 | 99.01c | 96.91% | -2.11 pts | -3.15 a -1.06 | 32 |
| otros_cierre | tocadas | 964 | 98.97c | 96.68% | -2.29 pts | -3.41 a -1.17 | 32 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 7353 | 98.49c | 97.95% | -0.54 pts | -0.86 a -0.22 | 153 |
| TOTAL | tocadas | 6936 | 98.51c | 97.83% | -0.68 pts | -1.02 a -0.34 | 153 |

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

Aun no hay veredicto: van 131 operaciones cerradas en 7.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
