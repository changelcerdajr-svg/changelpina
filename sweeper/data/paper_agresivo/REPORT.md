# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.8 de 28 | corridas: 162
- Capital inicial: $1,000.00 | valor actual: $935.29 | P&L: $-64.71 (-6.47%)
- Efectivo libre: $0.00 | en ordenes abiertas: $166.10 (3) | en posiciones: $779.85 (11)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 348 colocadas, 155 llenadas, 153 tocadas sin llenarse (sorteo 30%), 37 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 46 | 98.81c | 100.00% | 92.3-100.0% | +1.19 pts | $+36.63 | 0.15 |
| deportes_previo | 62 | 98.14c | 95.90% | 89.0-99.1% | -2.24 pts | $-109.31 | 0.31 |
| otros_cierre | 31 | 99.67c | 100.00% | 89.0-100.0% | +0.33 pts | $+7.04 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 144 | 98.63c | 98.14% | 95.1-99.6% | -0.49 pts | $-54.06 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.9c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $93.89 | 96.2c | 89.2c | deportes_previo |  | Spread: Fagiano Okayama (-2.5) |
| $93.89 | 95.0c | 95.0c | deportes_previo |  | Spread: Gangwon FC (-2.5) |
| $19.59 | 96.8c | 100.0c | cripto_cierre |  | Bitcoin Up or Down - November 21, 12:00AM-4:00AM ET |
| $93.93 | 99.4c | 100.0c | cripto_cierre |  | Ethereum Up or Down - November 21, 12:00AM-4:00AM ET |
| $68.03 | 96.9c | 98.0c | cripto_cierre |  | Solana Up or Down - November 21, 12:00AM-4:00AM ET |
| $93.93 | 97.9c | 96.5c | deportes_previo |  | Spread: Gençlerbirliği SK (-3.5) |
| $93.98 | 98.5c | 99.4c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $8.19 | 97.9c | 98.5c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 8013 | abiertas: 2622 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2321 | 98.85c | 99.05% | +0.20 pts | -0.19 a +0.59 | 22 |
| clima_cierre | tocadas | 2143 | 98.87c | 98.97% | +0.10 pts | -0.32 a +0.53 | 22 |
| cripto_cierre | todas | 1161 | 98.71c | 97.93% | -0.78 pts | -1.59 a +0.03 | 24 |
| cripto_cierre | tocadas | 1063 | 98.76c | 97.74% | -1.01 pts | -1.90 a -0.13 | 24 |
| deportes_previo | todas | 3358 | 98.05c | 97.45% | -0.59 pts | -1.12 a -0.07 | 88 |
| deportes_previo | tocadas | 3284 | 98.07c | 97.40% | -0.68 pts | -1.21 a -0.14 | 88 |
| otros_cierre | todas | 1096 | 98.98c | 96.99% | -1.99 pts | -3.00 a -0.99 | 33 |
| otros_cierre | tocadas | 1023 | 98.94c | 96.77% | -2.17 pts | -3.24 a -1.09 | 33 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 8013 | 98.47c | 97.92% | -0.55 pts | -0.85 a -0.24 | 169 |
| TOTAL | tocadas | 7574 | 98.48c | 97.80% | -0.68 pts | -1.01 a -0.35 | 169 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) finish week of November 16 above $270?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Amazon (AMZN) close at $245-$250 on the final day of trading of the week of Nov 16 – 

## Veredicto

Aun no hay veredicto: van 144 operaciones cerradas en 7.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
