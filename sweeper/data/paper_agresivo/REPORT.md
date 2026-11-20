# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.2 de 28 | corridas: 144
- Capital inicial: $1,000.00 | valor actual: $924.88 | P&L: $-75.12 (-7.51%)
- Efectivo libre: $0.00 | en ordenes abiertas: $528.86 (8) | en posiciones: $398.80 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 299 colocadas, 129 llenadas, 127 tocadas sin llenarse (sorteo 30%), 35 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 38 | 98.82c | 100.00% | 90.8-100.0% | +1.18 pts | $+30.95 | 0.16 |
| deportes_previo | 53 | 98.09c | 95.12% | 87.2-99.0% | -2.96 pts | $-121.43 | 0.34 |
| otros_cierre | 28 | 99.65c | 100.00% | 87.9-100.0% | +0.35 pts | $+6.55 | 0.35 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 124 | 98.60c | 97.83% | 94.3-99.6% | -0.77 pts | $-72.35 | 0.31 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.12 | 96.8c | 100.0c | deportes_previo |  | Sumqayit FK vs. Sabah Masazir: O/U 0.5 |
| $92.27 | 98.9c | 98.4c | deportes_previo |  | Alcorn State Braves vs. Tulane Green Wave (W) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6755 | abiertas: 3137 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2083 | 98.87c | 99.14% | +0.26 pts | -0.13 a +0.66 | 18 |
| clima_cierre | tocadas | 1917 | 98.89c | 99.06% | +0.17 pts | -0.26 a +0.60 | 18 |
| cripto_cierre | todas | 1103 | 98.73c | 98.19% | -0.54 pts | -1.32 a +0.24 | 20 |
| cripto_cierre | tocadas | 1014 | 98.76c | 98.03% | -0.73 pts | -1.58 a +0.11 | 20 |
| deportes_previo | todas | 2759 | 98.08c | 97.23% | -0.85 pts | -1.45 a -0.24 | 79 |
| deportes_previo | tocadas | 2698 | 98.10c | 97.16% | -0.94 pts | -1.56 a -0.32 | 79 |
| otros_cierre | todas | 738 | 99.14c | 97.97% | -1.17 pts | -2.18 a -0.16 | 15 |
| otros_cierre | tocadas | 679 | 99.10c | 97.79% | -1.31 pts | -2.40 a -0.21 | 15 |
| post_fin_90_97 | todas | 72 | 94.24c | 97.22% | +2.98 pts | -0.85 a +6.81 | 2 |
| post_fin_90_97 | tocadas | 56 | 94.31c | 96.43% | +2.12 pts | -2.79 a +7.02 | 2 |
| TOTAL | todas | 6755 | 98.50c | 98.05% | -0.45 pts | -0.77 a -0.12 | 134 |
| TOTAL | tocadas | 6364 | 98.52c | 97.93% | -0.58 pts | -0.93 a -0.24 | 134 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.7c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Milan be 11°C on November 18?

## Veredicto

Aun no hay veredicto: van 124 operaciones cerradas en 7.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
