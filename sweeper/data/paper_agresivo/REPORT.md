# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.1 de 28 | corridas: 141
- Capital inicial: $1,000.00 | valor actual: $922.74 | P&L: $-77.26 (-7.73%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $528.45 (9) | en posiciones: $398.64 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 288 colocadas, 127 llenadas, 121 tocadas sin llenarse (sorteo 30%), 31 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 37 | 98.78c | 100.00% | 90.6-100.0% | +1.22 pts | $+30.77 | 0.17 |
| deportes_previo | 53 | 98.09c | 95.12% | 87.2-99.0% | -2.96 pts | $-121.43 | 0.34 |
| otros_cierre | 27 | 99.66c | 100.00% | 87.5-100.0% | +0.34 pts | $+6.18 | 0.36 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 122 | 98.58c | 97.78% | 94.2-99.5% | -0.80 pts | $-72.90 | 0.32 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.12 | 99.6c | 99.5c | otros_cierre |  | Will UMich Consumer Sentiment be below 40.0 in November? |
| $92.12 | 96.8c | 97.8c | deportes_previo |  | Sumqayit FK vs. Sabah Masazir: O/U 0.5 |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6518 | abiertas: 3095 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1972 | 98.88c | 99.14% | +0.26 pts | -0.15 a +0.66 | 17 |
| clima_cierre | tocadas | 1815 | 98.90c | 99.06% | +0.16 pts | -0.28 a +0.61 | 17 |
| cripto_cierre | todas | 1014 | 98.74c | 98.52% | -0.22 pts | -0.96 a +0.51 | 15 |
| cripto_cierre | tocadas | 929 | 98.79c | 98.39% | -0.40 pts | -1.20 a +0.40 | 15 |
| deportes_previo | todas | 2744 | 98.08c | 97.21% | -0.87 pts | -1.48 a -0.26 | 79 |
| deportes_previo | tocadas | 2683 | 98.11c | 97.15% | -0.96 pts | -1.58 a -0.34 | 79 |
| otros_cierre | todas | 718 | 99.14c | 97.91% | -1.23 pts | -2.27 a -0.20 | 15 |
| otros_cierre | tocadas | 660 | 99.10c | 97.73% | -1.37 pts | -2.50 a -0.25 | 15 |
| post_fin_90_97 | todas | 70 | 94.20c | 97.14% | +2.94 pts | -1.00 a +6.88 | 2 |
| post_fin_90_97 | tocadas | 54 | 94.27c | 96.30% | +2.03 pts | -3.06 a +7.11 | 2 |
| TOTAL | todas | 6518 | 98.50c | 98.07% | -0.43 pts | -0.76 a -0.10 | 128 |
| TOTAL | tocadas | 6141 | 98.52c | 97.96% | -0.56 pts | -0.91 a -0.21 | 128 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.7c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Milan be 11°C on November 18?

## Veredicto

Aun no hay veredicto: van 122 operaciones cerradas en 7.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
