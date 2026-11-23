# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.8 de 28 | corridas: 217
- Capital inicial: $1,000.00 | valor actual: $898.24 | P&L: $-101.76 (-10.18%)
- Efectivo libre: $0.10 | en ordenes abiertas: $426.63 (6) | en posiciones: $483.92 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $91.77 en 1 posiciones
- Ordenes virtuales: 440 colocadas, 196 llenadas, 192 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 56 | 98.84c | 100.00% | 93.6-100.0% | +1.16 pts | $+43.42 | 0.18 |
| deportes_previo | 91 | 98.06c | 95.96% | 90.8-98.9% | -2.10 pts | $-154.68 | 0.27 |
| otros_cierre | 35 | 99.65c | 100.00% | 90.1-100.0% | +0.35 pts | $+8.31 | 0.36 |
| post_fin_90_97 | 3 | 95.67c | 100.00% | 43.8-100.0% | +4.33 pts | $+5.65 | 0.68 |
| TOTAL | 190 | 98.53c | 97.91% | 95.5-99.5% | -0.62 pts | $-89.36 | 0.28 |

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
| $35.36 | 99.8c | 96.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $89.85 | 96.9c | 96.9c | cripto_cierre |  | Solana Up or Down - November 23, 12:00AM-4:00AM ET |
| $89.82 | 99.0c | 98.3c | deportes_previo |  | Spread: FK LNZ Cherkasy (-2.5) |
| $89.85 | 98.4c | 98.0c | deportes_previo |  | Spread: FK Polissia (-3.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 11533 | abiertas: 2188 | abiertas mas de 7 dias despues de su fecha de fin: 1

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 3074 | 98.83c | 99.02% | +0.20 pts | -0.15 a +0.54 | 30 |
| clima_cierre | tocadas | 2849 | 98.85c | 98.95% | +0.10 pts | -0.28 a +0.47 | 30 |
| cripto_cierre | todas | 1488 | 98.69c | 98.19% | -0.51 pts | -1.18 a +0.17 | 27 |
| cripto_cierre | tocadas | 1350 | 98.74c | 98.00% | -0.74 pts | -1.48 a +0.00 | 27 |
| deportes_previo | todas | 5527 | 98.02c | 97.40% | -0.62 pts | -1.03 a -0.20 | 146 |
| deportes_previo | tocadas | 5396 | 98.05c | 97.38% | -0.68 pts | -1.10 a -0.25 | 144 |
| otros_cierre | todas | 1237 | 99.00c | 97.01% | -1.99 pts | -2.93 a -1.05 | 37 |
| otros_cierre | tocadas | 1155 | 98.97c | 96.80% | -2.17 pts | -3.18 a -1.16 | 37 |
| post_fin_90_97 | todas | 207 | 94.04c | 92.27% | -1.77 pts | -5.37 a +1.83 | 16 |
| post_fin_90_97 | tocadas | 175 | 94.15c | 90.86% | -3.29 pts | -7.51 a +0.93 | 16 |
| TOTAL | todas | 11533 | 98.36c | 97.80% | -0.55 pts | -0.82 a -0.29 | 256 |
| TOTAL | tocadas | 10925 | 98.38c | 97.70% | -0.68 pts | -0.96 a -0.40 | 254 |

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

Aun no hay veredicto: van 190 operaciones cerradas en 9.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
