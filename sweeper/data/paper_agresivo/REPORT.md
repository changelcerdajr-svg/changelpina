# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.0 de 28 | corridas: 194
- Capital inicial: $1,000.00 | valor actual: $874.56 | P&L: $-125.44 (-12.54%)
- Efectivo libre: $0.00 | en ordenes abiertas: $242.13 (6) | en posiciones: $642.98 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 397 colocadas, 178 llenadas, 173 tocadas sin llenarse (sorteo 30%), 40 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 52 | 98.76c | 100.00% | 93.1-100.0% | +1.24 pts | $+42.08 | 0.17 |
| deportes_previo | 78 | 98.04c | 95.19% | 89.3-98.7% | -2.85 pts | $-176.69 | 0.29 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 170 | 98.53c | 97.62% | 94.9-99.4% | -0.91 pts | $-114.89 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 89.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.43 | 98.8c | 98.8c | deportes_previo |  | Spread: Erzurumspor FK (-3.5) |
| $87.43 | 99.8c | 99.5c | deportes_previo |  | Spread: Muglaspor (-3.5) |
| $83.15 | 95.0c | 95.0c | deportes_previo |  | Spread: Göztepe SK (-2.5) |
| $87.40 | 97.1c | 97.7c | deportes_previo |  | Will Willem II Tilburg win on 2026-11-22? |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 9781 | abiertas: 2891 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2688 | 98.83c | 99.07% | +0.24 pts | -0.13 a +0.60 | 25 |
| clima_cierre | tocadas | 2487 | 98.85c | 98.99% | +0.14 pts | -0.25 a +0.53 | 25 |
| cripto_cierre | todas | 1315 | 98.71c | 98.10% | -0.61 pts | -1.34 a +0.12 | 25 |
| cripto_cierre | tocadas | 1193 | 98.75c | 97.90% | -0.84 pts | -1.65 a -0.04 | 25 |
| deportes_previo | todas | 4478 | 98.02c | 97.47% | -0.55 pts | -1.01 a -0.10 | 116 |
| deportes_previo | tocadas | 4372 | 98.05c | 97.43% | -0.62 pts | -1.09 a -0.16 | 115 |
| otros_cierre | todas | 1205 | 99.00c | 97.26% | -1.74 pts | -2.66 a -0.83 | 33 |
| otros_cierre | tocadas | 1126 | 98.97c | 97.07% | -1.90 pts | -2.88 a -0.92 | 33 |
| post_fin_90_97 | todas | 95 | 94.32c | 96.84% | +2.52 pts | -1.01 a +6.05 | 3 |
| post_fin_90_97 | tocadas | 77 | 94.37c | 96.10% | +1.73 pts | -2.60 a +6.06 | 3 |
| TOTAL | todas | 9781 | 98.42c | 97.96% | -0.46 pts | -0.74 a -0.18 | 202 |
| TOTAL | tocadas | 9255 | 98.44c | 97.86% | -0.58 pts | -0.87 a -0.29 | 201 |

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

Aun no hay veredicto: van 170 operaciones cerradas en 9.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
