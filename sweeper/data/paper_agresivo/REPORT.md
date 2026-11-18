# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.1 de 28 | corridas: 88
- Capital inicial: $1,000.00 | valor actual: $874.82 | P&L: $-125.18 (-12.52%)
- Efectivo libre: $0.72 | en ordenes abiertas: $261.24 (3) | en posiciones: $617.60 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 187 colocadas, 85 llenadas, 75 tocadas sin llenarse (sorteo 30%), 24 expiradas

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
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.28 | 97.9c | 98.4c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $82.12 | 98.5c | 97.9c | clima_cierre |  | Will the highest temperature in Paris be 13°C on November 18? |
| $87.34 | 99.9c | 100.0c | otros_cierre |  | Will the US national average gas price be less than $3.7600 on November 18? |
| $87.35 | 98.4c | 99.2c | cripto_cierre |  | Will the price of Ethereum be above $1,700 on November 18? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4582 | abiertas: 1943 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1216 | 98.97c | 99.26% | +0.29 pts | -0.19 a +0.77 | 9 |
| clima_cierre | tocadas | 1110 | 98.97c | 99.19% | +0.22 pts | -0.30 a +0.75 | 9 |
| cripto_cierre | todas | 694 | 98.87c | 97.98% | -0.88 pts | -1.92 a +0.15 | 14 |
| cripto_cierre | tocadas | 629 | 98.90c | 97.77% | -1.12 pts | -2.26 a +0.02 | 14 |
| deportes_previo | todas | 2034 | 98.07c | 97.05% | -1.02 pts | -1.75 a -0.29 | 60 |
| deportes_previo | tocadas | 1987 | 98.10c | 96.98% | -1.12 pts | -1.87 a -0.37 | 60 |
| otros_cierre | todas | 597 | 99.27c | 98.66% | -0.61 pts | -1.53 a +0.31 | 8 |
| otros_cierre | tocadas | 541 | 99.23c | 98.52% | -0.71 pts | -1.72 a +0.31 | 8 |
| post_fin_90_97 | todas | 41 | 94.21c | 97.56% | +3.35 pts | -1.45 a +8.14 | 1 |
| post_fin_90_97 | tocadas | 34 | 94.32c | 97.06% | +2.74 pts | -3.03 a +8.50 | 1 |
| TOTAL | todas | 4582 | 98.55c | 97.99% | -0.56 pts | -0.96 a -0.15 | 92 |
| TOTAL | tocadas | 4301 | 98.55c | 97.86% | -0.69 pts | -1.12 a -0.26 | 92 |

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

Aun no hay veredicto: van 77 operaciones cerradas en 5.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
