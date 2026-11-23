# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.9 de 28 | corridas: 219
- Capital inicial: $1,000.00 | valor actual: $901.55 | P&L: $-98.45 (-9.85%)
- Efectivo libre: $0.00 | en ordenes abiertas: $428.68 (7) | en posiciones: $484.83 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 446 colocadas, 198 llenadas, 194 tocadas sin llenarse (sorteo 30%), 47 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 57 | 98.80c | 100.00% | 93.7-100.0% | +1.20 pts | $+46.29 | 0.17 |
| deportes_previo | 91 | 98.06c | 95.96% | 90.8-98.9% | -2.10 pts | $-154.68 | 0.27 |
| otros_cierre | 35 | 99.65c | 100.00% | 90.1-100.0% | +0.35 pts | $+8.31 | 0.36 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 191 | 98.52c | 97.92% | 95.5-99.5% | -0.59 pts | $-86.48 | 0.28 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 90.0c | otros_cierre | si | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 97.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $89.82 | 99.0c | 98.4c | deportes_previo |  | Spread: FK LNZ Cherkasy (-2.5) |
| $89.85 | 98.4c | 98.2c | deportes_previo |  | Spread: FK Polissia (-3.5) |
| $72.13 | 95.0c | 95.0c | deportes_previo |  | Spread: FK Epitsentr Dunaivtsi (-2.5) |
| $18.63 | 99.3c | 99.3c | deportes_previo |  | Spread: FK Neftchi Fargona (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 11643 | abiertas: 2127 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3099 | 98.82c | 99.03% | +0.21 pts | -0.14 a +0.55 | 30 |
| clima_cierre | tocadas | 2872 | 98.85c | 98.96% | +0.11 pts | -0.26 a +0.47 | 30 |
| cripto_cierre | todas | 1509 | 98.69c | 98.21% | -0.48 pts | -1.15 a +0.18 | 27 |
| cripto_cierre | tocadas | 1368 | 98.75c | 98.03% | -0.72 pts | -1.45 a +0.01 | 27 |
| deportes_previo | todas | 5590 | 98.02c | 97.42% | -0.61 pts | -1.02 a -0.20 | 147 |
| deportes_previo | tocadas | 5459 | 98.06c | 97.39% | -0.67 pts | -1.09 a -0.25 | 145 |
| otros_cierre | todas | 1238 | 99.00c | 97.01% | -1.99 pts | -2.93 a -1.05 | 37 |
| otros_cierre | tocadas | 1156 | 98.97c | 96.80% | -2.17 pts | -3.18 a -1.16 | 37 |
| post_fin_90_97 | todas | 207 | 94.04c | 92.27% | -1.77 pts | -5.37 a +1.83 | 16 |
| post_fin_90_97 | tocadas | 175 | 94.15c | 90.86% | -3.29 pts | -7.51 a +0.93 | 16 |
| TOTAL | todas | 11643 | 98.36c | 97.81% | -0.54 pts | -0.81 a -0.28 | 257 |
| TOTAL | tocadas | 11030 | 98.38c | 97.71% | -0.67 pts | -0.95 a -0.40 | 255 |

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

Aun no hay veredicto: van 191 operaciones cerradas en 9.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
