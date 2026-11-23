# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.5 de 28 | corridas: 209
- Capital inicial: $1,000.00 | valor actual: $895.10 | P&L: $-104.90 (-10.49%)
- Efectivo libre: $0.00 | en ordenes abiertas: $223.77 (4) | en posiciones: $681.34 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 422 colocadas, 191 llenadas, 181 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 55 | 98.82c | 100.00% | 93.5-100.0% | +1.18 pts | $+43.25 | 0.17 |
| deportes_previo | 87 | 98.00c | 95.75% | 90.3-98.8% | -2.25 pts | $-157.85 | 0.28 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 182 | 98.50c | 97.82% | 95.3-99.4% | -0.69 pts | $-94.89 | 0.28 |

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
| $35.36 | 99.8c | 97.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $26.13 | 95.0c | 100.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $88.97 | 97.3c | 97.2c | deportes_previo |  | Spread: Antigua GFC (-1.5) |
| $89.53 | 99.4c | 99.4c | deportes_previo |  | Spread: Aurora FC (-2.5) |
| $89.56 | 99.9c | 99.9c | deportes_previo |  | Games Total: O/U 2.5 |
| $89.56 | 99.7c | 99.7c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 22, 2026? |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 10752 | abiertas: 2602 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2927 | 98.83c | 99.04% | +0.21 pts | -0.14 a +0.57 | 28 |
| clima_cierre | tocadas | 2714 | 98.85c | 98.97% | +0.12 pts | -0.26 a +0.49 | 28 |
| cripto_cierre | todas | 1401 | 98.71c | 98.07% | -0.64 pts | -1.35 a +0.07 | 27 |
| cripto_cierre | tocadas | 1275 | 98.75c | 97.88% | -0.87 pts | -1.65 a -0.09 | 27 |
| deportes_previo | todas | 5033 | 98.00c | 97.43% | -0.58 pts | -1.01 a -0.14 | 132 |
| deportes_previo | tocadas | 4905 | 98.04c | 97.40% | -0.64 pts | -1.08 a -0.20 | 130 |
| otros_cierre | todas | 1212 | 99.00c | 97.28% | -1.73 pts | -2.64 a -0.82 | 33 |
| otros_cierre | tocadas | 1132 | 98.97c | 97.08% | -1.88 pts | -2.86 a -0.91 | 33 |
| post_fin_90_97 | todas | 179 | 94.17c | 93.30% | -0.88 pts | -4.49 a +2.74 | 12 |
| post_fin_90_97 | tocadas | 154 | 94.19c | 92.21% | -1.98 pts | -6.16 a +2.19 | 12 |
| TOTAL | todas | 10752 | 98.37c | 97.87% | -0.50 pts | -0.77 a -0.23 | 232 |
| TOTAL | tocadas | 10180 | 98.39c | 97.77% | -0.62 pts | -0.91 a -0.34 | 230 |

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

Aun no hay veredicto: van 182 operaciones cerradas en 9.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
