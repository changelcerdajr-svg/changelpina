# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.4 de 28 | corridas: 122
- Capital inicial: $1,000.00 | valor actual: $903.76 | P&L: $-96.24 (-9.62%)
- Efectivo libre: $0.00 | en ordenes abiertas: $554.15 (8) | en posiciones: $355.59 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 253 colocadas, 112 llenadas, 105 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 37 | 98.78c | 100.00% | 90.6-100.0% | +1.22 pts | $+30.77 | 0.17 |
| deportes_previo | 41 | 98.17c | 94.08% | 83.9-98.7% | -4.09 pts | $-137.85 | 0.38 |
| otros_cierre | 24 | 99.67c | 100.00% | 86.2-100.0% | +0.33 pts | $+5.24 | 0.38 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 107 | 98.63c | 97.52% | 93.4-99.5% | -1.11 pts | $-90.26 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $89.46 | 99.8c | 99.0c | deportes_previo |  | Spread: CA Progreso (-2.5) |
| $51.73 | 99.8c | 99.8c | deportes_previo |  | Spread: Cerro Largo FC (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5898 | abiertas: 2480 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1721 | 98.90c | 99.07% | +0.17 pts | -0.28 a +0.62 | 16 |
| clima_cierre | tocadas | 1581 | 98.91c | 98.99% | +0.08 pts | -0.41 a +0.57 | 16 |
| cripto_cierre | todas | 951 | 98.78c | 98.53% | -0.25 pts | -1.01 a +0.51 | 14 |
| cripto_cierre | tocadas | 874 | 98.82c | 98.40% | -0.42 pts | -1.25 a +0.40 | 14 |
| deportes_previo | todas | 2476 | 98.09c | 97.09% | -0.99 pts | -1.65 a -0.34 | 72 |
| deportes_previo | tocadas | 2419 | 98.11c | 97.02% | -1.09 pts | -1.76 a -0.42 | 72 |
| otros_cierre | todas | 688 | 99.17c | 98.55% | -0.63 pts | -1.51 a +0.26 | 10 |
| otros_cierre | tocadas | 630 | 99.13c | 98.41% | -0.72 pts | -1.69 a +0.25 | 10 |
| post_fin_90_97 | todas | 62 | 94.14c | 96.77% | +2.63 pts | -1.81 a +7.07 | 2 |
| post_fin_90_97 | tocadas | 48 | 94.17c | 95.83% | +1.66 pts | -4.06 a +7.38 | 2 |
| TOTAL | todas | 5898 | 98.52c | 98.07% | -0.45 pts | -0.80 a -0.10 | 114 |
| TOTAL | tocadas | 5552 | 98.53c | 97.95% | -0.59 pts | -0.96 a -0.21 | 114 |

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

Aun no hay veredicto: van 107 operaciones cerradas en 6.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
