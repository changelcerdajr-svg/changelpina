# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.8 de 28 | corridas: 80
- Capital inicial: $1,000.00 | valor actual: $872.75 | P&L: $-127.25 (-12.72%)
- Efectivo libre: $0.00 | en ordenes abiertas: $260.95 (3) | en posiciones: $617.38 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 183 colocadas, 83 llenadas, 74 tocadas sin llenarse (sorteo 30%), 23 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 26 | 99.03c | 100.00% | 87.1-100.0% | +0.97 pts | $+16.20 | 0.09 |
| deportes_previo | 29 | 97.92c | 91.53% | 78.0-98.1% | -6.40 pts | $-150.31 | 0.44 |
| otros_cierre | 17 | 99.62c | 100.00% | 81.6-100.0% | +0.38 pts | $+3.98 | 0.45 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 75 | 98.57c | 96.35% | 90.8-99.3% | -2.22 pts | $-121.67 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.6c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 97.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.18 | 98.8c | 98.8c | cripto_cierre |  | XRP Up or Down - November 18, 12:00AM-4:00AM ET |
| $87.28 | 99.8c | 99.8c | deportes_previo |  | Will UK annual inflation be between 4.0% and 4.2% in October? |
| $87.28 | 97.9c | 98.4c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $82.12 | 98.5c | 97.9c | clima_cierre |  | Will the highest temperature in Paris be 13°C on November 18? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4391 | abiertas: 1642 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1164 | 98.97c | 99.31% | +0.34 pts | -0.13 a +0.82 | 8 |
| clima_cierre | tocadas | 1061 | 98.96c | 99.25% | +0.29 pts | -0.23 a +0.81 | 8 |
| cripto_cierre | todas | 661 | 98.92c | 98.18% | -0.74 pts | -1.75 a +0.27 | 12 |
| cripto_cierre | tocadas | 610 | 98.95c | 98.03% | -0.92 pts | -2.01 a +0.17 | 12 |
| deportes_previo | todas | 1946 | 98.07c | 97.28% | -0.79 pts | -1.51 a -0.07 | 53 |
| deportes_previo | tocadas | 1905 | 98.11c | 97.22% | -0.89 pts | -1.63 a -0.16 | 53 |
| otros_cierre | todas | 580 | 99.30c | 98.79% | -0.50 pts | -1.39 a +0.38 | 7 |
| otros_cierre | tocadas | 524 | 99.26c | 98.66% | -0.59 pts | -1.57 a +0.38 | 7 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 4391 | 98.56c | 98.16% | -0.41 pts | -0.80 a -0.01 | 81 |
| TOTAL | tocadas | 4133 | 98.57c | 98.04% | -0.53 pts | -0.95 a -0.11 | 81 |

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

Aun no hay veredicto: van 75 operaciones cerradas en 4.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
