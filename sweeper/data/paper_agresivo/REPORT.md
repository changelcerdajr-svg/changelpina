# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.1 de 28 | corridas: 114
- Capital inicial: $1,000.00 | valor actual: $890.13 | P&L: $-109.87 (-10.99%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $200.79 (3) | en posiciones: $694.82 (10)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 222 colocadas, 103 llenadas, 88 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 30 | 98.97c | 100.00% | 88.6-100.0% | +1.03 pts | $+20.65 | 0.18 |
| deportes_previo | 36 | 98.07c | 93.35% | 81.9-98.5% | -4.72 pts | $-141.42 | 0.39 |
| otros_cierre | 22 | 99.66c | 100.00% | 85.1-100.0% | +0.34 pts | $+4.80 | 0.40 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 93 | 98.63c | 97.15% | 92.5-99.4% | -1.48 pts | $-104.40 | 0.35 |

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
| $87.27 | 99.8c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.76 | 97.5c | 97.4c | deportes_previo |  | Will Shan United win on 2026-11-19? |
| $88.94 | 99.8c | 99.5c | deportes_previo |  | Spread: Shan United (-2.5) |
| $88.76 | 99.3c | 98.8c | deportes_previo |  | Spread: Hatta SC (-1.5) |
| $50.27 | 99.8c | 99.8c | deportes_previo |  | Spread: Hatta SC (-2.5) |
| $39.06 | 99.0c | 98.5c | deportes_previo |  | Spread: Al Dhafra SSC (-1.5) |
| $36.90 | 95.6c | 95.2c | cripto_cierre |  | Will the price of Bitcoin be less than $62,000 on November 19? |
| $87.72 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5502 | abiertas: 2267 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1565 | 98.90c | 99.17% | +0.27 pts | -0.18 a +0.72 | 13 |
| clima_cierre | tocadas | 1435 | 98.91c | 99.09% | +0.18 pts | -0.31 a +0.67 | 13 |
| cripto_cierre | todas | 858 | 98.80c | 98.37% | -0.44 pts | -1.28 a +0.41 | 14 |
| cripto_cierre | tocadas | 788 | 98.84c | 98.22% | -0.61 pts | -1.53 a +0.30 | 14 |
| deportes_previo | todas | 2359 | 98.09c | 97.16% | -0.93 pts | -1.60 a -0.26 | 67 |
| deportes_previo | tocadas | 2304 | 98.12c | 97.09% | -1.03 pts | -1.71 a -0.34 | 67 |
| otros_cierre | todas | 663 | 99.18c | 98.49% | -0.69 pts | -1.61 a +0.23 | 10 |
| otros_cierre | tocadas | 605 | 99.14c | 98.35% | -0.80 pts | -1.81 a +0.22 | 10 |
| post_fin_90_97 | todas | 57 | 94.08c | 96.49% | +2.41 pts | -2.42 a +7.24 | 2 |
| post_fin_90_97 | tocadas | 45 | 94.14c | 95.56% | +1.41 pts | -4.68 a +7.51 | 2 |
| TOTAL | todas | 5502 | 98.52c | 98.07% | -0.45 pts | -0.81 a -0.09 | 106 |
| TOTAL | tocadas | 5177 | 98.53c | 97.95% | -0.58 pts | -0.96 a -0.20 | 106 |

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

Aun no hay veredicto: van 93 operaciones cerradas en 6.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
