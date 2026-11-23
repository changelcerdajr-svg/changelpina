# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.7 de 28 | corridas: 212
- Capital inicial: $1,000.00 | valor actual: $897.82 | P&L: $-102.18 (-10.22%)
- Efectivo libre: $0.00 | en ordenes abiertas: $275.80 (5) | en posiciones: $631.87 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 429 colocadas, 193 llenadas, 185 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 55 | 98.82c | 100.00% | 93.5-100.0% | +1.18 pts | $+43.25 | 0.17 |
| deportes_previo | 89 | 98.02c | 95.86% | 90.6-98.8% | -2.15 pts | $-155.29 | 0.27 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 184 | 98.51c | 97.85% | 95.3-99.4% | -0.66 pts | $-92.33 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 89.8c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $26.13 | 95.0c | 100.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $89.53 | 99.4c | 99.4c | deportes_previo |  | Spread: Aurora FC (-2.5) |
| $89.56 | 99.7c | 99.5c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 22, 2026? |
| $54.02 | 99.0c | 99.0c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 22, 2026? |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |
| $75.05 | 99.9c | 99.9c | deportes_previo |  | Counter-Strike: regain vs Iowa Stormboar (BO3) - CROSSFIRE Playoffs |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 11094 | abiertas: 2445 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2996 | 98.83c | 99.03% | +0.20 pts | -0.15 a +0.55 | 29 |
| clima_cierre | tocadas | 2779 | 98.85c | 98.96% | +0.10 pts | -0.27 a +0.48 | 29 |
| cripto_cierre | todas | 1415 | 98.70c | 98.09% | -0.61 pts | -1.31 a +0.10 | 27 |
| cripto_cierre | tocadas | 1281 | 98.75c | 97.89% | -0.86 pts | -1.63 a -0.08 | 27 |
| deportes_previo | todas | 5270 | 98.01c | 97.45% | -0.56 pts | -0.99 a -0.14 | 137 |
| deportes_previo | tocadas | 5140 | 98.05c | 97.42% | -0.63 pts | -1.05 a -0.20 | 135 |
| otros_cierre | todas | 1220 | 99.00c | 97.21% | -1.78 pts | -2.70 a -0.87 | 34 |
| otros_cierre | tocadas | 1138 | 98.96c | 97.01% | -1.95 pts | -2.93 a -0.97 | 34 |
| post_fin_90_97 | todas | 193 | 94.12c | 93.26% | -0.85 pts | -4.34 a +2.64 | 13 |
| post_fin_90_97 | tocadas | 164 | 94.20c | 92.07% | -2.13 pts | -6.20 a +1.94 | 13 |
| TOTAL | todas | 11094 | 98.36c | 97.86% | -0.50 pts | -0.77 a -0.24 | 240 |
| TOTAL | tocadas | 10502 | 98.39c | 97.76% | -0.63 pts | -0.91 a -0.35 | 238 |

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

Aun no hay veredicto: van 184 operaciones cerradas en 9.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
