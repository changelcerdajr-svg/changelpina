# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.5 de 28 | corridas: 152
- Capital inicial: $1,000.00 | valor actual: $929.09 | P&L: $-70.91 (-7.09%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $276.85 (3) | en posiciones: $663.06 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 318 colocadas, 144 llenadas, 134 tocadas sin llenarse (sorteo 30%), 37 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 41 | 98.82c | 100.00% | 91.4-100.0% | +1.18 pts | $+33.11 | 0.16 |
| deportes_previo | 59 | 98.08c | 95.65% | 88.5-99.1% | -2.43 pts | $-111.64 | 0.32 |
| otros_cierre | 30 | 99.67c | 100.00% | 88.6-100.0% | +0.33 pts | $+6.86 | 0.34 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 135 | 98.60c | 98.01% | 94.8-99.6% | -0.58 pts | $-60.09 | 0.30 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $91.99 | 97.8c | 92.5c | deportes_previo |  | Spread: CD Unión La Calera (-2.5) |
| $92.14 | 99.8c | 99.8c | deportes_previo |  | Spread: Clemson (-17.5) |
| $92.14 | 97.8c | 98.7c | cripto_cierre |  | Solana Up or Down - November 20, 4:00PM-8:00PM ET |
| $69.26 | 99.8c | 98.0c | cripto_cierre |  | Dogecoin Up or Down - November 20, 4:00PM-8:00PM ET |
| $21.93 | 97.9c | 97.9c | cripto_cierre |  | Bitcoin Up or Down - November 20, 4:00PM-8:00PM ET |
| $81.19 | 99.9c | 99.9c | deportes_previo |  | Games Total: O/U 2.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 7474 | abiertas: 2744 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2212 | 98.86c | 99.10% | +0.24 pts | -0.15 a +0.63 | 20 |
| clima_cierre | tocadas | 2039 | 98.88c | 99.02% | +0.14 pts | -0.29 a +0.56 | 20 |
| cripto_cierre | todas | 1120 | 98.71c | 98.21% | -0.50 pts | -1.26 a +0.27 | 20 |
| cripto_cierre | tocadas | 1029 | 98.75c | 98.06% | -0.69 pts | -1.52 a +0.14 | 20 |
| deportes_previo | todas | 3014 | 98.07c | 97.40% | -0.68 pts | -1.24 a -0.11 | 81 |
| deportes_previo | tocadas | 2944 | 98.10c | 97.33% | -0.77 pts | -1.34 a -0.20 | 81 |
| otros_cierre | todas | 1051 | 98.99c | 96.96% | -2.04 pts | -3.07 a -1.00 | 32 |
| otros_cierre | tocadas | 981 | 98.95c | 96.74% | -2.21 pts | -3.31 a -1.11 | 32 |
| post_fin_90_97 | todas | 77 | 94.31c | 97.40% | +3.09 pts | -0.49 a +6.68 | 2 |
| post_fin_90_97 | tocadas | 61 | 94.40c | 96.72% | +2.32 pts | -2.18 a +6.83 | 2 |
| TOTAL | todas | 7474 | 98.49c | 97.96% | -0.53 pts | -0.85 a -0.21 | 155 |
| TOTAL | tocadas | 7054 | 98.51c | 97.84% | -0.67 pts | -1.00 a -0.33 | 155 |

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

Aun no hay veredicto: van 135 operaciones cerradas en 7.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
