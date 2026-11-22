# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.2 de 28 | corridas: 200
- Capital inicial: $1,000.00 | valor actual: $869.95 | P&L: $-130.05 (-13.01%)
- Efectivo libre: $0.71 | en ordenes abiertas: $304.83 (6) | en posiciones: $587.79 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 408 colocadas, 182 llenadas, 178 tocadas sin llenarse (sorteo 30%), 42 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 52 | 98.76c | 100.00% | 93.1-100.0% | +1.24 pts | $+42.08 | 0.17 |
| deportes_previo | 82 | 98.02c | 95.46% | 89.8-98.7% | -2.57 pts | $-168.47 | 0.28 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 174 | 98.51c | 97.69% | 95.1-99.4% | -0.82 pts | $-106.67 | 0.29 |

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
| $26.13 | 95.0c | 98.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $88.25 | 98.4c | 98.4c | deportes_previo |  | Spread: Málaga CF (-2.5) |
| $88.25 | 96.2c | 81.5c | deportes_previo |  | Spread: CA Osasuna (-3.5) |
| $87.57 | 99.0c | 99.0c | deportes_previo |  | Spread: Clube do Remo (-2.5) |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 10165 | abiertas: 2821 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2804 | 98.83c | 99.04% | +0.21 pts | -0.15 a +0.57 | 27 |
| clima_cierre | tocadas | 2600 | 98.85c | 98.96% | +0.11 pts | -0.27 a +0.50 | 27 |
| cripto_cierre | todas | 1396 | 98.71c | 98.07% | -0.64 pts | -1.36 a +0.07 | 27 |
| cripto_cierre | tocadas | 1271 | 98.75c | 97.88% | -0.88 pts | -1.66 a -0.09 | 27 |
| deportes_previo | todas | 4659 | 98.00c | 97.44% | -0.57 pts | -1.02 a -0.12 | 122 |
| deportes_previo | tocadas | 4546 | 98.04c | 97.42% | -0.62 pts | -1.08 a -0.17 | 120 |
| otros_cierre | todas | 1209 | 99.01c | 97.27% | -1.74 pts | -2.65 a -0.82 | 33 |
| otros_cierre | tocadas | 1129 | 98.97c | 97.08% | -1.89 pts | -2.87 a -0.92 | 33 |
| post_fin_90_97 | todas | 97 | 94.33c | 96.91% | +2.57 pts | -0.88 a +6.03 | 3 |
| post_fin_90_97 | tocadas | 78 | 94.37c | 96.15% | +1.79 pts | -2.49 a +6.07 | 3 |
| TOTAL | todas | 10165 | 98.41c | 97.94% | -0.47 pts | -0.75 a -0.20 | 212 |
| TOTAL | tocadas | 9624 | 98.43c | 97.84% | -0.59 pts | -0.87 a -0.30 | 210 |

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

Aun no hay veredicto: van 174 operaciones cerradas en 9.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
