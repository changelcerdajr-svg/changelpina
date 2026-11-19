# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.8 de 28 | corridas: 107
- Capital inicial: $1,000.00 | valor actual: $887.97 | P&L: $-112.03 (-11.20%)
- Efectivo libre: $0.00 | en ordenes abiertas: $177.00 (3) | en posiciones: $716.27 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 213 colocadas, 97 llenadas, 86 tocadas sin llenarse (sorteo 30%), 27 expiradas

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
| $91.77 | 99.8c | 96.2c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.6c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $88.76 | 97.9c | 97.9c | cripto_cierre |  | Ethereum above 1,820 on November 19, 4AM ET? |
| $88.18 | 99.9c | 100.0c | deportes_previo |  | Valorant: XJG vs FunPlus Phoenix - Map 1 Winner |
| $88.76 | 97.5c | 97.5c | deportes_previo |  | Will Shan United win on 2026-11-19? |
| $88.76 | 99.3c | 99.3c | deportes_previo |  | Spread: Hatta SC (-1.5) |
| $88.31 | 99.8c | 99.8c | otros_cierre |  | Walmart (WMT) Q3 US comp sales (ex-fuel) growth <1%? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5384 | abiertas: 1990 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1538 | 98.90c | 99.15% | +0.25 pts | -0.21 a +0.71 | 13 |
| clima_cierre | tocadas | 1408 | 98.91c | 99.08% | +0.16 pts | -0.33 a +0.66 | 13 |
| cripto_cierre | todas | 842 | 98.84c | 98.34% | -0.51 pts | -1.36 a +0.35 | 14 |
| cripto_cierre | tocadas | 773 | 98.88c | 98.19% | -0.69 pts | -1.62 a +0.24 | 14 |
| deportes_previo | todas | 2307 | 98.10c | 97.23% | -0.87 pts | -1.54 a -0.20 | 64 |
| deportes_previo | tocadas | 2256 | 98.13c | 97.16% | -0.96 pts | -1.64 a -0.28 | 64 |
| otros_cierre | todas | 644 | 99.22c | 98.45% | -0.77 pts | -1.72 a +0.18 | 10 |
| otros_cierre | tocadas | 587 | 99.18c | 98.30% | -0.89 pts | -1.93 a +0.15 | 10 |
| post_fin_90_97 | todas | 53 | 94.10c | 96.23% | +2.13 pts | -3.06 a +7.32 | 2 |
| post_fin_90_97 | tocadas | 41 | 94.17c | 95.12% | +0.96 pts | -5.73 a +7.64 | 2 |
| TOTAL | todas | 5384 | 98.54c | 98.09% | -0.45 pts | -0.82 a -0.09 | 103 |
| TOTAL | tocadas | 5065 | 98.55c | 97.97% | -0.58 pts | -0.97 a -0.20 | 103 |

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
