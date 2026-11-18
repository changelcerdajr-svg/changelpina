# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 5.2 de 28 | corridas: 90
- Capital inicial: $1,000.00 | valor actual: $875.23 | P&L: $-124.77 (-12.48%)
- Efectivo libre: $1.82 | en ordenes abiertas: $436.33 (5) | en posiciones: $442.92 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 191 colocadas, 85 llenadas, 77 tocadas sin llenarse (sorteo 30%), 24 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 28 | 98.99c | 100.00% | 87.9-100.0% | +1.01 pts | $+18.68 | 0.10 |
| deportes_previo | 30 | 97.99c | 91.84% | 78.7-98.2% | -6.15 pts | $-150.14 | 0.43 |
| otros_cierre | 18 | 99.64c | 100.00% | 82.4-100.0% | +0.36 pts | $+4.07 | 0.44 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 79 | 98.61c | 96.57% | 91.2-99.3% | -2.04 pts | $-118.93 | 0.34 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $35.36 | 99.8c | 99.0c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.6c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.28 | 97.9c | 98.4c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $82.12 | 98.5c | 97.9c | clima_cierre |  | Will the highest temperature in Paris be 13°C on November 18? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4783 | abiertas: 1956 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1290 | 98.95c | 99.22% | +0.27 pts | -0.20 a +0.75 | 10 |
| clima_cierre | tocadas | 1178 | 98.95c | 99.15% | +0.20 pts | -0.32 a +0.72 | 10 |
| cripto_cierre | todas | 773 | 98.86c | 98.19% | -0.67 pts | -1.60 a +0.26 | 14 |
| cripto_cierre | tocadas | 707 | 98.89c | 98.02% | -0.87 pts | -1.88 a +0.15 | 14 |
| deportes_previo | todas | 2067 | 98.07c | 97.10% | -0.98 pts | -1.70 a -0.26 | 60 |
| deportes_previo | tocadas | 2016 | 98.11c | 97.02% | -1.08 pts | -1.82 a -0.34 | 60 |
| otros_cierre | todas | 609 | 99.26c | 98.69% | -0.57 pts | -1.47 a +0.33 | 8 |
| otros_cierre | tocadas | 553 | 99.22c | 98.55% | -0.66 pts | -1.65 a +0.33 | 8 |
| post_fin_90_97 | todas | 44 | 94.13c | 95.45% | +1.32 pts | -4.91 a +7.56 | 2 |
| post_fin_90_97 | tocadas | 36 | 94.25c | 94.44% | +0.19 pts | -7.39 a +7.78 | 2 |
| TOTAL | todas | 4783 | 98.55c | 98.03% | -0.52 pts | -0.91 a -0.13 | 94 |
| TOTAL | tocadas | 4490 | 98.56c | 97.91% | -0.65 pts | -1.07 a -0.23 | 94 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.5c -> pago 0.0 | otros_cierre | tocada | Will "A Dog's Perfect Christmas" be the #2 global Netflix movie this week?
- 99.5c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Denver be between 60-61°F on November 17?

## Veredicto

Aun no hay veredicto: van 79 operaciones cerradas en 5.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
