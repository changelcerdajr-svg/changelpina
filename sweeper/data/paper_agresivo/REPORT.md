# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.0 de 28 | corridas: 113
- Capital inicial: $1,000.00 | valor actual: $890.60 | P&L: $-109.40 (-10.94%)
- Efectivo libre: $0.00 | en ordenes abiertas: $0.00 (0) | en posiciones: $895.26 (13)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 219 colocadas, 103 llenadas, 88 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 29 | 98.94c | 100.00% | 88.3-100.0% | +1.06 pts | $+20.59 | 0.10 |
| deportes_previo | 36 | 98.07c | 93.35% | 81.9-98.5% | -4.72 pts | $-141.42 | 0.39 |
| otros_cierre | 20 | 99.65c | 100.00% | 83.9-100.0% | +0.35 pts | $+4.52 | 0.42 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 90 | 98.59c | 97.06% | 92.3-99.4% | -1.53 pts | $-104.74 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 100.0c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.76 | 97.5c | 97.4c | deportes_previo |  | Will Shan United win on 2026-11-19? |
| $88.94 | 99.8c | 99.5c | deportes_previo |  | Spread: Shan United (-2.5) |
| $88.76 | 99.3c | 98.8c | deportes_previo |  | Spread: Hatta SC (-1.5) |
| $50.27 | 99.8c | 99.8c | deportes_previo |  | Spread: Hatta SC (-2.5) |
| $88.31 | 99.8c | 99.8c | otros_cierre |  | Walmart (WMT) Q3 US comp sales (ex-fuel) growth <1%? |
| $53.02 | 99.8c | 99.8c | otros_cierre |  | Walmart (WMT) Q3 US comp sales (ex-fuel) growth 1% to 2.5%? |
| $39.06 | 99.0c | 99.0c | deportes_previo |  | Spread: Al Dhafra SSC (-1.5) |
| $36.90 | 95.6c | 96.7c | cripto_cierre |  | Will the price of Bitcoin be less than $62,000 on November 19? |
| $87.72 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5476 | abiertas: 2223 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1565 | 98.90c | 99.17% | +0.27 pts | -0.18 a +0.72 | 13 |
| clima_cierre | tocadas | 1435 | 98.91c | 99.09% | +0.18 pts | -0.31 a +0.67 | 13 |
| cripto_cierre | todas | 857 | 98.81c | 98.37% | -0.44 pts | -1.28 a +0.40 | 14 |
| cripto_cierre | tocadas | 787 | 98.84c | 98.22% | -0.62 pts | -1.53 a +0.30 | 14 |
| deportes_previo | todas | 2352 | 98.09c | 97.19% | -0.89 pts | -1.56 a -0.23 | 66 |
| deportes_previo | tocadas | 2297 | 98.12c | 97.13% | -0.99 pts | -1.67 a -0.31 | 66 |
| otros_cierre | todas | 649 | 99.21c | 98.46% | -0.75 pts | -1.69 a +0.19 | 10 |
| otros_cierre | tocadas | 592 | 99.17c | 98.31% | -0.86 pts | -1.89 a +0.17 | 10 |
| post_fin_90_97 | todas | 53 | 94.10c | 96.23% | +2.13 pts | -3.06 a +7.32 | 2 |
| post_fin_90_97 | tocadas | 41 | 94.17c | 95.12% | +0.96 pts | -5.73 a +7.64 | 2 |
| TOTAL | todas | 5476 | 98.53c | 98.08% | -0.44 pts | -0.81 a -0.08 | 105 |
| TOTAL | tocadas | 5152 | 98.54c | 97.96% | -0.58 pts | -0.96 a -0.19 | 105 |

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

Aun no hay veredicto: van 90 operaciones cerradas en 6.0 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
