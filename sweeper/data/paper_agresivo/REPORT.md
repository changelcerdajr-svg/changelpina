# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.7 de 28 | corridas: 214
- Capital inicial: $1,000.00 | valor actual: $898.48 | P&L: $-101.52 (-10.15%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $434.51 (6) | en posiciones: $473.94 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 434 colocadas, 194 llenadas, 188 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 56 | 98.84c | 100.00% | 93.6-100.0% | +1.16 pts | $+43.42 | 0.18 |
| deportes_previo | 91 | 98.06c | 95.96% | 90.8-98.9% | -2.10 pts | $-154.68 | 0.27 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 187 | 98.53c | 97.88% | 95.4-99.5% | -0.64 pts | $-91.55 | 0.28 |

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
| $35.36 | 99.8c | 98.1c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $26.13 | 95.0c | 100.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $89.56 | 99.7c | 99.5c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 22, 2026? |
| $54.02 | 99.0c | 99.0c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 22, 2026? |
| $89.82 | 99.0c | 99.0c | deportes_previo |  | Spread: FK LNZ Cherkasy (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 11454 | abiertas: 2147 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3034 | 98.83c | 99.04% | +0.22 pts | -0.13 a +0.56 | 29 |
| clima_cierre | tocadas | 2816 | 98.85c | 98.97% | +0.12 pts | -0.25 a +0.49 | 29 |
| cripto_cierre | todas | 1487 | 98.69c | 98.18% | -0.51 pts | -1.18 a +0.16 | 27 |
| cripto_cierre | tocadas | 1349 | 98.74c | 98.00% | -0.74 pts | -1.48 a -0.00 | 27 |
| deportes_previo | todas | 5497 | 98.02c | 97.41% | -0.61 pts | -1.03 a -0.19 | 145 |
| deportes_previo | tocadas | 5366 | 98.05c | 97.38% | -0.67 pts | -1.09 a -0.25 | 143 |
| otros_cierre | todas | 1229 | 99.00c | 97.07% | -1.93 pts | -2.87 a -0.99 | 36 |
| otros_cierre | tocadas | 1147 | 98.97c | 96.86% | -2.11 pts | -3.11 a -1.11 | 36 |
| post_fin_90_97 | todas | 207 | 94.04c | 92.27% | -1.77 pts | -5.37 a +1.83 | 16 |
| post_fin_90_97 | tocadas | 175 | 94.15c | 90.86% | -3.29 pts | -7.51 a +0.93 | 16 |
| TOTAL | todas | 11454 | 98.35c | 97.81% | -0.54 pts | -0.81 a -0.28 | 253 |
| TOTAL | tocadas | 10853 | 98.38c | 97.71% | -0.67 pts | -0.95 a -0.39 | 251 |

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

Aun no hay veredicto: van 187 operaciones cerradas en 9.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
