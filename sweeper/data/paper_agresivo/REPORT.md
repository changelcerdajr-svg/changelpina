# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.2 de 28 | corridas: 117
- Capital inicial: $1,000.00 | valor actual: $901.27 | P&L: $-98.73 (-9.87%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $562.85 (8) | en posiciones: $342.93 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 237 colocadas, 106 llenadas, 95 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 34 | 98.78c | 100.00% | 89.8-100.0% | +1.22 pts | $+27.63 | 0.17 |
| deportes_previo | 40 | 98.16c | 94.01% | 83.5-98.6% | -4.15 pts | $-138.24 | 0.38 |
| otros_cierre | 22 | 99.66c | 100.00% | 85.1-100.0% | +0.34 pts | $+4.80 | 0.40 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 101 | 98.60c | 97.37% | 93.1-99.5% | -1.23 pts | $-94.23 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.6c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $39.06 | 99.0c | 98.5c | deportes_previo |  | Spread: Al Dhafra SSC (-1.5) |
| $89.46 | 99.8c | 99.8c | deportes_previo |  | Spread: CA Progreso (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5764 | abiertas: 2371 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1677 | 98.90c | 99.11% | +0.21 pts | -0.24 a +0.66 | 15 |
| clima_cierre | tocadas | 1538 | 98.91c | 99.02% | +0.12 pts | -0.37 a +0.61 | 15 |
| cripto_cierre | todas | 942 | 98.80c | 98.51% | -0.28 pts | -1.05 a +0.48 | 14 |
| cripto_cierre | tocadas | 869 | 98.83c | 98.39% | -0.44 pts | -1.27 a +0.39 | 14 |
| deportes_previo | todas | 2411 | 98.08c | 97.14% | -0.94 pts | -1.60 a -0.28 | 69 |
| deportes_previo | tocadas | 2355 | 98.11c | 97.07% | -1.04 pts | -1.71 a -0.36 | 69 |
| otros_cierre | todas | 676 | 99.17c | 98.52% | -0.65 pts | -1.56 a +0.25 | 10 |
| otros_cierre | tocadas | 618 | 99.13c | 98.38% | -0.75 pts | -1.74 a +0.24 | 10 |
| post_fin_90_97 | todas | 58 | 94.06c | 96.55% | +2.49 pts | -2.26 a +7.24 | 2 |
| post_fin_90_97 | tocadas | 46 | 94.12c | 95.65% | +1.53 pts | -4.43 a +7.50 | 2 |
| TOTAL | todas | 5764 | 98.52c | 98.09% | -0.43 pts | -0.78 a -0.08 | 110 |
| TOTAL | tocadas | 5426 | 98.53c | 97.97% | -0.56 pts | -0.93 a -0.19 | 110 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.7c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Milan be 11°C on November 18?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?

## Veredicto

Aun no hay veredicto: van 101 operaciones cerradas en 6.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
