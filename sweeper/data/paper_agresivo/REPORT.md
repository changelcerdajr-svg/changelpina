# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 10.1 de 28 | corridas: 224
- Capital inicial: $1,000.00 | valor actual: $845.18 | P&L: $-154.82 (-15.48%)
- Efectivo libre: $0.00 | en ordenes abiertas: $352.59 (5) | en posiciones: $564.72 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 448 colocadas, 201 llenadas, 195 tocadas sin llenarse (sorteo 30%), 47 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 57 | 98.80c | 100.00% | 93.7-100.0% | +1.20 pts | $+46.29 | 0.17 |
| deportes_previo | 92 | 98.02c | 96.00% | 90.8-98.9% | -2.02 pts | $-150.88 | 0.27 |
| otros_cierre | 35 | 99.65c | 100.00% | 90.1-100.0% | +0.35 pts | $+8.31 | 0.36 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 192 | 98.50c | 97.93% | 95.5-99.5% | -0.57 pts | $-82.69 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 82.9c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 88.7c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $89.82 | 99.0c | 87.7c | deportes_previo |  | Spread: FK LNZ Cherkasy (-2.5) |
| $89.85 | 98.4c | 52.8c | deportes_previo |  | Spread: FK Polissia (-3.5) |
| $18.63 | 99.3c | 99.6c | deportes_previo |  | Spread: FK Neftchi Fargona (-2.5) |
| $88.14 | 97.1c | 97.5c | deportes_previo |  | Spread: FK Neftchi Fargona (-1.5) |
| $56.03 | 99.8c | 100.0c | otros_cierre |  | Will "I Play Rocky" score at least 60 on the Rotten Tomatoes Tomatometer? |
| $7.85 | 99.7c | 99.1c | cripto_cierre |  | Will the price of Bitcoin be less than $56,000 on November 23? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 11736 | abiertas: 2284 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3130 | 98.82c | 99.01% | +0.19 pts | -0.16 a +0.53 | 31 |
| clima_cierre | tocadas | 2902 | 98.85c | 98.93% | +0.08 pts | -0.29 a +0.46 | 31 |
| cripto_cierre | todas | 1511 | 98.69c | 98.21% | -0.48 pts | -1.14 a +0.18 | 27 |
| cripto_cierre | tocadas | 1370 | 98.74c | 98.03% | -0.72 pts | -1.44 a +0.01 | 27 |
| deportes_previo | todas | 5646 | 98.03c | 97.42% | -0.60 pts | -1.01 a -0.19 | 148 |
| deportes_previo | tocadas | 5514 | 98.06c | 97.40% | -0.66 pts | -1.08 a -0.25 | 146 |
| otros_cierre | todas | 1239 | 99.00c | 97.01% | -1.99 pts | -2.93 a -1.05 | 37 |
| otros_cierre | tocadas | 1157 | 98.97c | 96.80% | -2.17 pts | -3.17 a -1.16 | 37 |
| post_fin_90_97 | todas | 210 | 94.06c | 92.38% | -1.68 pts | -5.22 a +1.87 | 16 |
| post_fin_90_97 | tocadas | 178 | 94.16c | 91.01% | -3.15 pts | -7.30 a +1.00 | 16 |
| TOTAL | todas | 11736 | 98.36c | 97.81% | -0.54 pts | -0.80 a -0.28 | 259 |
| TOTAL | tocadas | 11121 | 98.38c | 97.71% | -0.67 pts | -0.95 a -0.40 | 257 |

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

Aun no hay veredicto: van 192 operaciones cerradas en 10.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
