# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 11.5 de 28 | corridas: 262
- Capital inicial: $1,000.00 | valor actual: $949.52 | P&L: $-50.48 (-5.05%)
- Efectivo libre: $0.69 | en ordenes abiertas: $422.12 (7) | en posiciones: $542.10 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 525 colocadas, 242 llenadas, 222 tocadas sin llenarse (sorteo 30%), 54 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 68 | 98.84c | 100.00% | 94.7-100.0% | +1.16 pts | $+53.87 | 0.18 |
| deportes_previo | 117 | 98.05c | 96.86% | 92.7-99.1% | -1.19 pts | $-113.47 | 0.26 |
| otros_cierre | 42 | 99.63c | 100.00% | 91.6-100.0% | +0.37 pts | $+10.90 | 0.33 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 235 | 98.52c | 98.33% | 96.3-99.6% | -0.19 pts | $-35.10 | 0.27 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 85.8c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $94.67 | 99.9c | 99.9c | deportes_previo |  | Game Handicap: ICxI (-1.5) vs Power Rangers (+1.5) |
| $95.27 | 99.7c | 99.5c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 24, 2026? |
| $95.27 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 24? |
| $42.49 | 99.5c | 99.2c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 24? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 13703 | abiertas: 2180 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3761 | 98.81c | 98.91% | +0.10 pts | -0.23 a +0.43 | 41 |
| clima_cierre | tocadas | 3488 | 98.83c | 98.82% | -0.01 pts | -0.36 a +0.35 | 41 |
| cripto_cierre | todas | 1769 | 98.66c | 98.08% | -0.58 pts | -1.22 a +0.05 | 34 |
| cripto_cierre | tocadas | 1618 | 98.70c | 97.90% | -0.81 pts | -1.50 a -0.11 | 34 |
| deportes_previo | todas | 6494 | 98.05c | 97.37% | -0.68 pts | -1.06 a -0.29 | 173 |
| deportes_previo | tocadas | 6340 | 98.09c | 97.34% | -0.74 pts | -1.14 a -0.35 | 171 |
| otros_cierre | todas | 1426 | 98.96c | 97.34% | -1.63 pts | -2.46 a -0.80 | 38 |
| otros_cierre | tocadas | 1314 | 98.92c | 97.11% | -1.81 pts | -2.71 a -0.91 | 38 |
| post_fin_90_97 | todas | 253 | 94.03c | 93.68% | -0.35 pts | -3.32 a +2.62 | 16 |
| post_fin_90_97 | tocadas | 215 | 94.14c | 92.56% | -1.58 pts | -5.05 a +1.89 | 16 |
| TOTAL | todas | 13703 | 98.36c | 97.81% | -0.54 pts | -0.79 a -0.30 | 302 |
| TOTAL | tocadas | 12975 | 98.38c | 97.71% | -0.68 pts | -0.93 a -0.42 | 300 |

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

Aun no hay veredicto: van 235 operaciones cerradas en 11.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
