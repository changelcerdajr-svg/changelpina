# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.3 de 28 | corridas: 202
- Capital inicial: $1,000.00 | valor actual: $888.79 | P&L: $-111.21 (-11.12%)
- Efectivo libre: $4.38 | en ordenes abiertas: $394.56 (7) | en posiciones: $499.31 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 410 colocadas, 183 llenadas, 178 tocadas sin llenarse (sorteo 30%), 42 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 52 | 98.76c | 100.00% | 93.1-100.0% | +1.24 pts | $+42.08 | 0.17 |
| deportes_previo | 84 | 98.01c | 95.58% | 90.0-98.8% | -2.42 pts | $-163.55 | 0.28 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 176 | 98.49c | 97.72% | 95.1-99.4% | -0.77 pts | $-101.75 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 89.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $26.13 | 95.0c | 100.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $87.57 | 99.0c | 99.0c | deportes_previo |  | Spread: Clube do Remo (-2.5) |
| $88.03 | 95.0c | 95.0c | deportes_previo |  | Spread: Clube do Remo (-1.5) |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 10349 | abiertas: 2764 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2819 | 98.83c | 99.04% | +0.21 pts | -0.14 a +0.57 | 27 |
| clima_cierre | tocadas | 2614 | 98.85c | 98.97% | +0.12 pts | -0.27 a +0.51 | 27 |
| cripto_cierre | todas | 1399 | 98.71c | 98.07% | -0.64 pts | -1.36 a +0.07 | 27 |
| cripto_cierre | tocadas | 1274 | 98.75c | 97.88% | -0.87 pts | -1.65 a -0.09 | 27 |
| deportes_previo | todas | 4789 | 98.00c | 97.36% | -0.64 pts | -1.09 a -0.19 | 129 |
| deportes_previo | tocadas | 4670 | 98.04c | 97.33% | -0.70 pts | -1.16 a -0.24 | 127 |
| otros_cierre | todas | 1209 | 99.01c | 97.27% | -1.74 pts | -2.65 a -0.82 | 33 |
| otros_cierre | tocadas | 1129 | 98.97c | 97.08% | -1.89 pts | -2.87 a -0.92 | 33 |
| post_fin_90_97 | todas | 133 | 94.13c | 93.23% | -0.90 pts | -5.11 a +3.32 | 9 |
| post_fin_90_97 | tocadas | 110 | 94.15c | 91.82% | -2.33 pts | -7.39 a +2.73 | 9 |
| TOTAL | todas | 10349 | 98.39c | 97.85% | -0.54 pts | -0.82 a -0.26 | 225 |
| TOTAL | tocadas | 9797 | 98.41c | 97.75% | -0.66 pts | -0.95 a -0.37 | 223 |

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

Aun no hay veredicto: van 176 operaciones cerradas en 9.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
