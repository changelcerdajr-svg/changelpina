# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.8 de 28 | corridas: 106
- Capital inicial: $1,000.00 | valor actual: $887.56 | P&L: $-112.44 (-11.24%)
- Efectivo libre: $0.00 | en ordenes abiertas: $531.58 (7) | en posiciones: $361.69 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 213 colocadas, 93 llenadas, 86 tocadas sin llenarse (sorteo 30%), 27 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 28 | 98.99c | 100.00% | 87.9-100.0% | +1.01 pts | $+18.68 | 0.10 |
| deportes_previo | 35 | 98.01c | 93.13% | 81.4-98.4% | -4.87 pts | $-141.51 | 0.40 |
| otros_cierre | 20 | 99.65c | 100.00% | 83.9-100.0% | +0.35 pts | $+4.52 | 0.42 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 88 | 98.59c | 96.98% | 92.1-99.4% | -1.61 pts | $-106.73 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.6c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.18 | 99.9c | 99.9c | deportes_previo |  | Valorant: XJG vs FunPlus Phoenix - Map 1 Winner |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5344 | abiertas: 1999 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1534 | 98.91c | 99.15% | +0.25 pts | -0.21 a +0.70 | 13 |
| clima_cierre | tocadas | 1404 | 98.92c | 99.07% | +0.16 pts | -0.34 a +0.66 | 13 |
| cripto_cierre | todas | 835 | 98.85c | 98.32% | -0.53 pts | -1.39 a +0.34 | 14 |
| cripto_cierre | tocadas | 767 | 98.88c | 98.17% | -0.71 pts | -1.64 a +0.23 | 14 |
| deportes_previo | todas | 2279 | 98.10c | 97.19% | -0.90 pts | -1.58 a -0.23 | 64 |
| deportes_previo | tocadas | 2228 | 98.13c | 97.13% | -1.00 pts | -1.69 a -0.31 | 64 |
| otros_cierre | todas | 643 | 99.22c | 98.44% | -0.78 pts | -1.73 a +0.17 | 10 |
| otros_cierre | tocadas | 586 | 99.19c | 98.29% | -0.89 pts | -1.94 a +0.15 | 10 |
| post_fin_90_97 | todas | 53 | 94.10c | 96.23% | +2.13 pts | -3.06 a +7.32 | 2 |
| post_fin_90_97 | tocadas | 41 | 94.17c | 95.12% | +0.96 pts | -5.73 a +7.64 | 2 |
| TOTAL | todas | 5344 | 98.54c | 98.07% | -0.47 pts | -0.84 a -0.10 | 103 |
| TOTAL | tocadas | 5026 | 98.55c | 97.95% | -0.60 pts | -0.99 a -0.21 | 103 |

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

Aun no hay veredicto: van 88 operaciones cerradas en 5.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
