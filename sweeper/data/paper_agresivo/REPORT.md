# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.5 de 28 | corridas: 97
- Capital inicial: $1,000.00 | valor actual: $878.36 | P&L: $-121.64 (-12.16%)
- Efectivo libre: $0.00 | en ordenes abiertas: $346.48 (4) | en posiciones: $535.84 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 195 colocadas, 87 llenadas, 78 tocadas sin llenarse (sorteo 30%), 26 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 3 | 97.87c | 100.00% | 43.8-100.0% | +2.13 pts | $+5.88 | 1.10 |
| cripto_cierre | 28 | 98.99c | 100.00% | 87.9-100.0% | +1.01 pts | $+18.68 | 0.10 |
| deportes_previo | 30 | 97.99c | 91.84% | 78.7-98.2% | -6.15 pts | $-150.14 | 0.43 |
| otros_cierre | 18 | 99.64c | 100.00% | 82.4-100.0% | +0.36 pts | $+4.07 | 0.44 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 80 | 98.61c | 96.62% | 91.3-99.3% | -1.98 pts | $-117.68 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.4c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.6c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.28 | 97.9c | 98.4c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $87.52 | 98.2c | 99.0c | deportes_previo |  | Spread: Reus FC Reddis (-2.5) |
| $87.52 | 98.3c | 98.3c | deportes_previo |  | Spread: Barakaldo CF (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5023 | abiertas: 2038 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1400 | 98.93c | 99.14% | +0.21 pts | -0.27 a +0.69 | 12 |
| clima_cierre | tocadas | 1279 | 98.94c | 99.06% | +0.12 pts | -0.40 a +0.65 | 12 |
| cripto_cierre | todas | 792 | 98.84c | 98.23% | -0.60 pts | -1.51 a +0.31 | 14 |
| cripto_cierre | tocadas | 724 | 98.87c | 98.07% | -0.80 pts | -1.79 a +0.19 | 14 |
| deportes_previo | todas | 2157 | 98.10c | 97.17% | -0.93 pts | -1.62 a -0.23 | 61 |
| deportes_previo | tocadas | 2106 | 98.13c | 97.10% | -1.03 pts | -1.74 a -0.31 | 61 |
| otros_cierre | todas | 628 | 99.24c | 98.57% | -0.67 pts | -1.60 a +0.25 | 9 |
| otros_cierre | tocadas | 572 | 99.20c | 98.43% | -0.77 pts | -1.79 a +0.24 | 9 |
| post_fin_90_97 | todas | 46 | 94.18c | 95.65% | +1.47 pts | -4.49 a +7.43 | 2 |
| post_fin_90_97 | tocadas | 37 | 94.26c | 94.59% | +0.34 pts | -7.05 a +7.72 | 2 |
| TOTAL | todas | 5023 | 98.55c | 98.05% | -0.50 pts | -0.88 a -0.12 | 98 |
| TOTAL | tocadas | 4718 | 98.56c | 97.92% | -0.64 pts | -1.04 a -0.23 | 98 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.7c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Milan be 11°C on November 18?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.5c -> pago 0.0 | otros_cierre | tocada | Will "A Dog's Perfect Christmas" be the #2 global Netflix movie this week?

## Veredicto

Aun no hay veredicto: van 80 operaciones cerradas en 5.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
