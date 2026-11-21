# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.9 de 28 | corridas: 164
- Capital inicial: $1,000.00 | valor actual: $947.19 | P&L: $-52.81 (-5.28%)
- Efectivo libre: $0.18 | en ordenes abiertas: $353.91 (5) | en posiciones: $598.95 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 356 colocadas, 156 llenadas, 157 tocadas sin llenarse (sorteo 30%), 38 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 49 | 98.78c | 100.00% | 92.7-100.0% | +1.22 pts | $+40.02 | 0.14 |
| deportes_previo | 63 | 98.10c | 95.98% | 89.1-99.1% | -2.12 pts | $-105.60 | 0.31 |
| otros_cierre | 31 | 99.67c | 100.00% | 89.0-100.0% | +0.33 pts | $+7.04 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 148 | 98.60c | 98.18% | 95.2-99.6% | -0.41 pts | $-46.96 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.9c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $93.89 | 95.0c | 95.0c | deportes_previo |  | Spread: Gangwon FC (-2.5) |
| $93.93 | 97.9c | 96.5c | deportes_previo |  | Spread: Gençlerbirliği SK (-3.5) |
| $94.55 | 96.2c | 96.2c | deportes_previo |  | Hannover 96 vs. SpVgg Greuther Fürth: Neither team to score first? |
| $93.98 | 98.5c | 99.3c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $8.19 | 97.9c | 97.8c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 8107 | abiertas: 2601 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2344 | 98.85c | 99.02% | +0.17 pts | -0.23 a +0.57 | 23 |
| clima_cierre | tocadas | 2166 | 98.87c | 98.94% | +0.07 pts | -0.36 a +0.50 | 23 |
| cripto_cierre | todas | 1173 | 98.70c | 97.95% | -0.75 pts | -1.55 a +0.05 | 24 |
| cripto_cierre | tocadas | 1068 | 98.75c | 97.75% | -0.99 pts | -1.87 a -0.12 | 24 |
| deportes_previo | todas | 3413 | 98.05c | 97.44% | -0.61 pts | -1.14 a -0.09 | 90 |
| deportes_previo | tocadas | 3336 | 98.07c | 97.38% | -0.70 pts | -1.23 a -0.16 | 90 |
| otros_cierre | todas | 1100 | 98.98c | 97.00% | -1.98 pts | -2.98 a -0.98 | 33 |
| otros_cierre | tocadas | 1027 | 98.94c | 96.79% | -2.15 pts | -3.22 a -1.08 | 33 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 8107 | 98.46c | 97.91% | -0.56 pts | -0.86 a -0.25 | 172 |
| TOTAL | tocadas | 7658 | 98.48c | 97.79% | -0.69 pts | -1.02 a -0.37 | 172 |

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

Aun no hay veredicto: van 148 operaciones cerradas en 7.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
