# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.5 de 28 | corridas: 127
- Capital inicial: $1,000.00 | valor actual: $906.92 | P&L: $-93.08 (-9.31%)
- Efectivo libre: $0.00 | en ordenes abiertas: $287.68 (5) | en posiciones: $622.44 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 264 colocadas, 119 llenadas, 112 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 37 | 98.78c | 100.00% | 90.6-100.0% | +1.22 pts | $+30.77 | 0.17 |
| deportes_previo | 43 | 98.24c | 94.33% | 84.5-98.7% | -3.91 pts | $-137.56 | 0.37 |
| otros_cierre | 25 | 99.68c | 100.00% | 86.7-100.0% | +0.32 pts | $+5.33 | 0.36 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 110 | 98.66c | 97.59% | 93.6-99.5% | -1.07 pts | $-89.88 | 0.33 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.9c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $90.38 | 96.9c | 96.7c | deportes_previo |  | Stetson Hatters vs. UCF Knights (W) |
| $39.56 | 99.6c | 99.2c | deportes_previo |  | Spread: São Paulo FC (-3.5) |
| $88.92 | 95.6c | 98.2c | deportes_previo |  | Spread: Colts (-7.5) |
| $47.90 | 95.9c | 95.9c | deportes_previo |  | Will C.J. Stroud score the first touchdown? |
| $56.72 | 99.1c | 99.2c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 19, 2026? |
| $84.55 | 99.6c | 99.3c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 19, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6063 | abiertas: 2490 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1824 | 98.89c | 99.07% | +0.18 pts | -0.26 a +0.62 | 17 |
| clima_cierre | tocadas | 1677 | 98.90c | 98.99% | +0.08 pts | -0.39 a +0.56 | 17 |
| cripto_cierre | todas | 956 | 98.78c | 98.54% | -0.24 pts | -1.00 a +0.52 | 14 |
| cripto_cierre | tocadas | 878 | 98.82c | 98.41% | -0.41 pts | -1.23 a +0.41 | 14 |
| deportes_previo | todas | 2526 | 98.08c | 97.11% | -0.97 pts | -1.62 a -0.32 | 73 |
| deportes_previo | tocadas | 2469 | 98.11c | 97.04% | -1.07 pts | -1.73 a -0.40 | 73 |
| otros_cierre | todas | 695 | 99.16c | 98.56% | -0.60 pts | -1.48 a +0.29 | 10 |
| otros_cierre | tocadas | 637 | 99.12c | 98.43% | -0.69 pts | -1.65 a +0.28 | 10 |
| post_fin_90_97 | todas | 62 | 94.14c | 96.77% | +2.63 pts | -1.81 a +7.07 | 2 |
| post_fin_90_97 | tocadas | 48 | 94.17c | 95.83% | +1.66 pts | -4.06 a +7.38 | 2 |
| TOTAL | todas | 6063 | 98.52c | 98.09% | -0.43 pts | -0.77 a -0.09 | 116 |
| TOTAL | tocadas | 5709 | 98.53c | 97.97% | -0.56 pts | -0.93 a -0.20 | 116 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.7c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Milan be 11°C on November 18?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?

## Veredicto

Aun no hay veredicto: van 110 operaciones cerradas en 6.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
