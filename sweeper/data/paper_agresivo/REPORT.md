# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 14.7 de 28 | corridas: 343
- Capital inicial: $1,000.00 | valor actual: $883.54 | P&L: $-116.46 (-11.65%)
- Efectivo libre: $0.00 | en ordenes abiertas: $294.10 (5) | en posiciones: $651.26 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $214.40 en 3 posiciones
- Ordenes virtuales: 687 colocadas, 314 llenadas, 292 tocadas sin llenarse (sorteo 30%), 76 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 84 | 98.84c | 100.00% | 95.6-100.0% | +1.16 pts | $+66.77 | 0.17 |
| deportes_previo | 163 | 98.05c | 96.90% | 93.9-99.0% | -1.15 pts | $-148.88 | 0.24 |
| otros_cierre | 49 | 99.62c | 100.00% | 92.7-100.0% | +0.38 pts | $+13.04 | 0.31 |
| post_fin_90_97 | 4 | 95.70c | 100.00% | 51.0-100.0% | +4.30 pts | $+6.48 | 0.65 |
| TOTAL | 305 | 98.48c | 98.25% | 96.7-99.5% | -0.23 pts | $-54.64 | 0.25 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-99.67 | 97.3c | 0.0 | deportes_previo | Spread: CF Cruz Azul (-3.5) |
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 90.3c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.1c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre | si | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.43 | 98.2c | 97.5c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 27, 2026? |
| $37.36 | 97.4c | 98.0c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 27, 2026? |
| $27.95 | 99.8c | 99.8c | otros_cierre |  | Will the next Gemini Carbon model (4.1+) be released on November 27, 2026? |
| $93.04 | 99.8c | 86.8c | deportes_previo |  | Prairie View A&M Panthers vs. Iowa Hawkeyes |
| $93.04 | 97.8c | 97.0c | deportes_previo |  | Spread: Shimizu S-Pulse (-2.5) |
| $93.04 | 99.6c | 59.1c | deportes_previo |  | Spread: Shimizu S-Pulse (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 17851 | abiertas: 3439 | abiertas mas de 7 dias despues de su fecha de fin: 8

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 4920 | 98.80c | 99.00% | +0.20 pts | -0.07 a +0.48 | 49 |
| clima_cierre | tocadas | 4584 | 98.83c | 98.93% | +0.10 pts | -0.19 a +0.40 | 49 |
| cripto_cierre | todas | 2260 | 98.58c | 98.19% | -0.39 pts | -0.94 a +0.15 | 41 |
| cripto_cierre | tocadas | 2048 | 98.65c | 98.00% | -0.65 pts | -1.25 a -0.05 | 41 |
| deportes_previo | todas | 8354 | 98.05c | 97.41% | -0.64 pts | -0.97 a -0.30 | 221 |
| deportes_previo | tocadas | 8139 | 98.09c | 97.36% | -0.72 pts | -1.07 a -0.38 | 219 |
| otros_cierre | todas | 2020 | 98.92c | 97.77% | -1.15 pts | -1.79 a -0.51 | 45 |
| otros_cierre | tocadas | 1861 | 98.87c | 97.58% | -1.29 pts | -1.98 a -0.60 | 45 |
| post_fin_90_97 | todas | 297 | 94.05c | 92.93% | -1.13 pts | -4.01 a +1.76 | 21 |
| post_fin_90_97 | tocadas | 252 | 94.15c | 91.67% | -2.48 pts | -5.86 a +0.89 | 21 |
| TOTAL | todas | 17851 | 98.35c | 97.91% | -0.44 pts | -0.65 a -0.23 | 377 |
| TOTAL | tocadas | 16884 | 98.38c | 97.81% | -0.58 pts | -0.80 a -0.36 | 375 |

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

Aun no hay veredicto: van 305 operaciones cerradas en 14.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
