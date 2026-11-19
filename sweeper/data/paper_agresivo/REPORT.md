# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.6 de 28 | corridas: 101
- Capital inicial: $1,000.00 | valor actual: $840.52 | P&L: $-159.48 (-15.95%)
- Efectivo libre: $0.90 | en ordenes abiertas: $210.78 (3) | en posiciones: $675.64 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 204 colocadas, 92 llenadas, 83 tocadas sin llenarse (sorteo 30%), 26 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 28 | 98.99c | 100.00% | 87.9-100.0% | +1.01 pts | $+18.68 | 0.10 |
| deportes_previo | 32 | 98.01c | 92.41% | 79.9-98.3% | -5.60 pts | $-147.02 | 0.42 |
| otros_cierre | 18 | 99.64c | 100.00% | 82.4-100.0% | +0.36 pts | $+4.07 | 0.44 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 83 | 98.59c | 96.77% | 91.6-99.3% | -1.81 pts | $-112.69 | 0.35 |

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
| $87.27 | 99.8c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.20 | 97.8c | 98.9c | deportes_previo |  | Texas Southern Tigers vs. San Diego State Aztecs |
| $88.20 | 97.1c | 51.5c | deportes_previo |  | Jazz vs. Lakers: O/U 202.5 |
| $88.21 | 99.0c | 98.7c | deportes_previo |  | Cal State Fullerton Titans vs. UCLA Bruins |
| $85.74 | 99.6c | 99.2c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 18, 2026? |
| $51.78 | 99.8c | 99.8c | otros_cierre |  | Will the next Gemini Carbon model (4.1+) be released on November 18, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5100 | abiertas: 2051 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1434 | 98.92c | 99.16% | +0.24 pts | -0.23 a +0.71 | 12 |
| clima_cierre | tocadas | 1309 | 98.93c | 99.08% | +0.15 pts | -0.36 a +0.67 | 12 |
| cripto_cierre | todas | 803 | 98.83c | 98.26% | -0.57 pts | -1.47 a +0.32 | 14 |
| cripto_cierre | tocadas | 735 | 98.86c | 98.10% | -0.76 pts | -1.74 a +0.21 | 14 |
| deportes_previo | todas | 2181 | 98.10c | 97.20% | -0.89 pts | -1.58 a -0.21 | 61 |
| deportes_previo | tocadas | 2130 | 98.13c | 97.14% | -0.99 pts | -1.70 a -0.29 | 61 |
| otros_cierre | todas | 631 | 99.24c | 98.57% | -0.67 pts | -1.59 a +0.26 | 9 |
| otros_cierre | tocadas | 575 | 99.20c | 98.43% | -0.76 pts | -1.78 a +0.25 | 9 |
| post_fin_90_97 | todas | 51 | 94.12c | 96.08% | +1.96 pts | -3.43 a +7.35 | 2 |
| post_fin_90_97 | tocadas | 41 | 94.17c | 95.12% | +0.96 pts | -5.73 a +7.64 | 2 |
| TOTAL | todas | 5100 | 98.55c | 98.08% | -0.47 pts | -0.84 a -0.09 | 98 |
| TOTAL | tocadas | 4790 | 98.55c | 97.95% | -0.60 pts | -1.00 a -0.20 | 98 |

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

Aun no hay veredicto: van 83 operaciones cerradas en 5.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
