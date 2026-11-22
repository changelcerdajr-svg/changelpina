# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 8.8 de 28 | corridas: 188
- Capital inicial: $1,000.00 | valor actual: $831.45 | P&L: $-168.55 (-16.85%)
- Efectivo libre: $1.04 | en ordenes abiertas: $552.73 (8) | en posiciones: $329.45 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 388 colocadas, 173 llenadas, 168 tocadas sin llenarse (sorteo 30%), 39 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 51 | 98.77c | 100.00% | 93.0-100.0% | +1.23 pts | $+41.62 | 0.18 |
| deportes_previo | 76 | 98.04c | 95.12% | 89.0-98.6% | -2.92 pts | $-178.11 | 0.29 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 167 | 98.53c | 97.60% | 94.9-99.4% | -0.93 pts | $-116.77 | 0.30 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 92.4c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $86.75 | 98.5c | 49.9c | deportes_previo |  | Spread: Tokushima Vortis (-3.5) |
| $6.94 | 98.6c | 91.5c | deportes_previo |  | Spread: Shōnan Bellmāre (-3.5) |
| $21.37 | 97.9c | 97.9c | cripto_cierre |  | Bitcoin Up or Down - November 22, 2:00AM-2:05AM ET |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 9619 | abiertas: 2800 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2656 | 98.83c | 99.06% | +0.22 pts | -0.14 a +0.59 | 25 |
| clima_cierre | tocadas | 2459 | 98.85c | 98.98% | +0.13 pts | -0.26 a +0.52 | 25 |
| cripto_cierre | todas | 1310 | 98.71c | 98.09% | -0.62 pts | -1.35 a +0.11 | 25 |
| cripto_cierre | tocadas | 1190 | 98.75c | 97.90% | -0.85 pts | -1.66 a -0.05 | 25 |
| deportes_previo | todas | 4354 | 98.02c | 97.42% | -0.60 pts | -1.07 a -0.13 | 115 |
| deportes_previo | tocadas | 4248 | 98.05c | 97.38% | -0.68 pts | -1.15 a -0.20 | 114 |
| otros_cierre | todas | 1204 | 99.01c | 97.26% | -1.75 pts | -2.66 a -0.83 | 33 |
| otros_cierre | tocadas | 1125 | 98.97c | 97.07% | -1.91 pts | -2.88 a -0.93 | 33 |
| post_fin_90_97 | todas | 95 | 94.32c | 96.84% | +2.52 pts | -1.01 a +6.05 | 3 |
| post_fin_90_97 | tocadas | 77 | 94.37c | 96.10% | +1.73 pts | -2.60 a +6.06 | 3 |
| TOTAL | todas | 9619 | 98.42c | 97.94% | -0.49 pts | -0.77 a -0.21 | 201 |
| TOTAL | tocadas | 9099 | 98.44c | 97.83% | -0.61 pts | -0.91 a -0.32 | 200 |

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

Aun no hay veredicto: van 167 operaciones cerradas en 8.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
