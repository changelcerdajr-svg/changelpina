# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 7.3 de 28 | corridas: 147
- Capital inicial: $1,000.00 | valor actual: $917.94 | P&L: $-82.06 (-8.21%)
- Efectivo libre: $4.73 | en ordenes abiertas: $255.60 (3) | en posiciones: $670.37 (10)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 305 colocadas, 135 llenadas, 132 tocadas sin llenarse (sorteo 30%), 35 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 38 | 98.82c | 100.00% | 90.8-100.0% | +1.18 pts | $+30.95 | 0.16 |
| deportes_previo | 54 | 98.06c | 95.24% | 87.5-99.0% | -2.82 pts | $-118.39 | 0.34 |
| otros_cierre | 28 | 99.65c | 100.00% | 87.9-100.0% | +0.35 pts | $+6.55 | 0.35 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 125 | 98.59c | 97.85% | 94.4-99.6% | -0.73 pts | $-69.30 | 0.31 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 95.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $92.27 | 98.9c | 98.4c | deportes_previo |  | Alcorn State Braves vs. Tulane Green Wave (W) |
| $10.39 | 97.0c | 97.0c | deportes_previo |  | Will 1. FC Köln win on 2026-11-20? |
| $92.40 | 96.5c | 91.8c | deportes_previo |  | Spread: Le Havre AC (-2.5) |
| $91.13 | 97.9c | 97.9c | deportes_previo |  | Spread: Real Murcia CF (-2.5) |
| $92.49 | 99.8c | 98.3c | otros_cierre |  | Will Apple (AAPL) hit (HIGH) $376 Week of November 16 2026? |
| $63.06 | 99.8c | 98.3c | otros_cierre |  | Will Apple (AAPL) hit (HIGH) $372 Week of November 16 2026? |
| $14.22 | 98.9c | 98.5c | cripto_cierre |  | Silver (XAGUSD) Up or Down on November 20? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6847 | abiertas: 3146 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2098 | 98.87c | 99.14% | +0.27 pts | -0.12 a +0.66 | 18 |
| clima_cierre | tocadas | 1930 | 98.90c | 99.07% | +0.17 pts | -0.25 a +0.60 | 18 |
| cripto_cierre | todas | 1115 | 98.71c | 98.21% | -0.51 pts | -1.28 a +0.26 | 20 |
| cripto_cierre | tocadas | 1025 | 98.75c | 98.05% | -0.70 pts | -1.54 a +0.14 | 20 |
| deportes_previo | todas | 2801 | 98.07c | 97.27% | -0.80 pts | -1.39 a -0.20 | 79 |
| deportes_previo | tocadas | 2738 | 98.10c | 97.21% | -0.89 pts | -1.50 a -0.28 | 79 |
| otros_cierre | todas | 759 | 99.11c | 97.23% | -1.88 pts | -3.03 a -0.73 | 21 |
| otros_cierre | tocadas | 699 | 99.07c | 97.00% | -2.07 pts | -3.32 a -0.82 | 21 |
| post_fin_90_97 | todas | 74 | 94.26c | 97.30% | +3.04 pts | -0.69 a +6.77 | 2 |
| post_fin_90_97 | tocadas | 58 | 94.33c | 96.55% | +2.22 pts | -2.52 a +6.96 | 2 |
| TOTAL | todas | 6847 | 98.49c | 97.99% | -0.50 pts | -0.83 a -0.17 | 140 |
| TOTAL | tocadas | 6450 | 98.51c | 97.87% | -0.64 pts | -0.99 a -0.29 | 140 |

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

Aun no hay veredicto: van 125 operaciones cerradas en 7.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
