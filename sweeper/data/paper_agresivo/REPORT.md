# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.3 de 28 | corridas: 93
- Capital inicial: $1,000.00 | valor actual: $876.32 | P&L: $-123.68 (-12.37%)
- Efectivo libre: $1.75 | en ordenes abiertas: $261.36 (3) | en posiciones: $617.97 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 192 colocadas, 87 llenadas, 78 tocadas sin llenarse (sorteo 30%), 24 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 28 | 98.99c | 100.00% | 87.9-100.0% | +1.01 pts | $+18.68 | 0.10 |
| deportes_previo | 30 | 97.99c | 91.84% | 78.7-98.2% | -6.15 pts | $-150.14 | 0.43 |
| otros_cierre | 18 | 99.64c | 100.00% | 82.4-100.0% | +0.36 pts | $+4.07 | 0.44 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 79 | 98.61c | 96.57% | 91.2-99.3% | -2.04 pts | $-118.93 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.6c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 99.2c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.28 | 97.9c | 98.4c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $82.12 | 98.5c | 97.9c | clima_cierre |  | Will the highest temperature in Paris be 13°C on November 18? |
| $87.52 | 98.2c | 99.0c | deportes_previo |  | Spread: Reus FC Reddis (-2.5) |
| $87.52 | 98.3c | 98.3c | deportes_previo |  | Spread: Barakaldo CF (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4831 | abiertas: 2066 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1306 | 98.95c | 99.23% | +0.28 pts | -0.19 a +0.75 | 10 |
| clima_cierre | tocadas | 1190 | 98.95c | 99.16% | +0.21 pts | -0.31 a +0.72 | 10 |
| cripto_cierre | todas | 780 | 98.85c | 98.21% | -0.64 pts | -1.57 a +0.28 | 14 |
| cripto_cierre | tocadas | 713 | 98.88c | 98.04% | -0.84 pts | -1.85 a +0.17 | 14 |
| deportes_previo | todas | 2084 | 98.08c | 97.07% | -1.01 pts | -1.73 a -0.29 | 61 |
| deportes_previo | tocadas | 2033 | 98.11c | 97.00% | -1.11 pts | -1.85 a -0.37 | 61 |
| otros_cierre | todas | 615 | 99.25c | 98.70% | -0.56 pts | -1.45 a +0.34 | 8 |
| otros_cierre | tocadas | 559 | 99.22c | 98.57% | -0.65 pts | -1.63 a +0.33 | 8 |
| post_fin_90_97 | todas | 46 | 94.18c | 95.65% | +1.47 pts | -4.49 a +7.43 | 2 |
| post_fin_90_97 | tocadas | 37 | 94.26c | 94.59% | +0.34 pts | -7.05 a +7.72 | 2 |
| TOTAL | todas | 4831 | 98.55c | 98.03% | -0.52 pts | -0.91 a -0.13 | 95 |
| TOTAL | tocadas | 4532 | 98.56c | 97.90% | -0.65 pts | -1.07 a -0.24 | 95 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.5c -> pago 0.0 | otros_cierre | tocada | Will "A Dog's Perfect Christmas" be the #2 global Netflix movie this week?
- 99.5c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Denver be between 60-61°F on November 17?

## Veredicto

Aun no hay veredicto: van 79 operaciones cerradas en 5.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
