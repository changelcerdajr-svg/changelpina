# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.6 de 28 | corridas: 129
- Capital inicial: $1,000.00 | valor actual: $909.96 | P&L: $-90.04 (-9.00%)
- Efectivo libre: $0.00 | en ordenes abiertas: $380.94 (8) | en posiciones: $532.06 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 267 colocadas, 119 llenadas, 112 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 37 | 98.78c | 100.00% | 90.6-100.0% | +1.22 pts | $+30.77 | 0.17 |
| deportes_previo | 44 | 98.20c | 94.48% | 84.9-98.7% | -3.73 pts | $-134.67 | 0.37 |
| otros_cierre | 25 | 99.68c | 100.00% | 86.7-100.0% | +0.32 pts | $+5.33 | 0.36 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 111 | 98.64c | 97.62% | 93.7-99.5% | -1.03 pts | $-86.99 | 0.33 |

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
| $39.56 | 99.6c | 99.2c | deportes_previo |  | Spread: São Paulo FC (-3.5) |
| $88.92 | 95.6c | 98.2c | deportes_previo |  | Spread: Colts (-7.5) |
| $47.90 | 95.9c | 95.9c | deportes_previo |  | Will C.J. Stroud score the first touchdown? |
| $56.72 | 99.1c | 99.2c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 19, 2026? |
| $84.55 | 99.6c | 99.2c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 19, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6154 | abiertas: 2535 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1859 | 98.88c | 99.09% | +0.20 pts | -0.23 a +0.64 | 17 |
| clima_cierre | tocadas | 1708 | 98.90c | 99.00% | +0.11 pts | -0.36 a +0.58 | 17 |
| cripto_cierre | todas | 962 | 98.76c | 98.54% | -0.22 pts | -0.97 a +0.53 | 14 |
| cripto_cierre | tocadas | 883 | 98.80c | 98.41% | -0.39 pts | -1.21 a +0.43 | 14 |
| deportes_previo | todas | 2564 | 98.08c | 97.15% | -0.93 pts | -1.57 a -0.29 | 73 |
| deportes_previo | tocadas | 2506 | 98.11c | 97.09% | -1.02 pts | -1.68 a -0.37 | 73 |
| otros_cierre | todas | 703 | 99.15c | 98.44% | -0.71 pts | -1.62 a +0.20 | 11 |
| otros_cierre | tocadas | 645 | 99.11c | 98.29% | -0.81 pts | -1.81 a +0.18 | 11 |
| post_fin_90_97 | todas | 66 | 94.15c | 96.97% | +2.82 pts | -1.36 a +7.00 | 2 |
| post_fin_90_97 | tocadas | 50 | 94.20c | 96.00% | +1.80 pts | -3.69 a +7.29 | 2 |
| TOTAL | todas | 6154 | 98.51c | 98.10% | -0.41 pts | -0.75 a -0.07 | 117 |
| TOTAL | tocadas | 5792 | 98.52c | 97.98% | -0.54 pts | -0.90 a -0.18 | 117 |

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

Aun no hay veredicto: van 111 operaciones cerradas en 6.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
