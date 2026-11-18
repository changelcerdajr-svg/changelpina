# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.2 de 28 | corridas: 89
- Capital inicial: $1,000.00 | valor actual: $875.47 | P&L: $-124.53 (-12.45%)
- Efectivo libre: $0.65 | en ordenes abiertas: $261.31 (3) | en posiciones: $617.60 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 188 colocadas, 85 llenadas, 76 tocadas sin llenarse (sorteo 30%), 24 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 27 | 99.02c | 100.00% | 87.5-100.0% | +0.98 pts | $+17.26 | 0.09 |
| deportes_previo | 30 | 97.99c | 91.84% | 78.7-98.2% | -6.15 pts | $-150.14 | 0.43 |
| otros_cierre | 17 | 99.62c | 100.00% | 81.6-100.0% | +0.38 pts | $+3.98 | 0.45 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 77 | 98.59c | 96.46% | 91.0-99.3% | -2.13 pts | $-120.44 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.2c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.28 | 97.9c | 98.4c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $82.12 | 98.5c | 97.9c | clima_cierre |  | Will the highest temperature in Paris be 13°C on November 18? |
| $87.34 | 99.9c | 100.0c | otros_cierre |  | Will the US national average gas price be less than $3.7600 on November 18? |
| $87.35 | 98.4c | 100.0c | cripto_cierre |  | Will the price of Ethereum be above $1,700 on November 18? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4671 | abiertas: 1949 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1290 | 98.95c | 99.22% | +0.27 pts | -0.20 a +0.75 | 10 |
| clima_cierre | tocadas | 1178 | 98.95c | 99.15% | +0.20 pts | -0.32 a +0.72 | 10 |
| cripto_cierre | todas | 695 | 98.86c | 97.99% | -0.88 pts | -1.91 a +0.15 | 14 |
| cripto_cierre | tocadas | 630 | 98.89c | 97.78% | -1.12 pts | -2.25 a +0.02 | 14 |
| deportes_previo | todas | 2044 | 98.07c | 97.06% | -1.00 pts | -1.73 a -0.27 | 60 |
| deportes_previo | tocadas | 1995 | 98.10c | 96.99% | -1.11 pts | -1.85 a -0.36 | 60 |
| otros_cierre | todas | 600 | 99.27c | 98.67% | -0.60 pts | -1.52 a +0.31 | 8 |
| otros_cierre | tocadas | 544 | 99.23c | 98.53% | -0.70 pts | -1.71 a +0.31 | 8 |
| post_fin_90_97 | todas | 42 | 94.16c | 97.62% | +3.46 pts | -1.23 a +8.14 | 1 |
| post_fin_90_97 | tocadas | 35 | 94.26c | 97.14% | +2.89 pts | -2.72 a +8.50 | 1 |
| TOTAL | todas | 4671 | 98.55c | 98.01% | -0.54 pts | -0.94 a -0.14 | 93 |
| TOTAL | tocadas | 4382 | 98.55c | 97.88% | -0.67 pts | -1.10 a -0.25 | 93 |

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

Aun no hay veredicto: van 77 operaciones cerradas en 5.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
