# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.8 de 28 | corridas: 133
- Capital inicial: $1,000.00 | valor actual: $914.71 | P&L: $-85.29 (-8.53%)
- Efectivo libre: $0.00 | en ordenes abiertas: $574.40 (10) | en posiciones: $345.76 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 275 colocadas, 122 llenadas, 114 tocadas sin llenarse (sorteo 30%), 29 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 37 | 98.78c | 100.00% | 90.6-100.0% | +1.22 pts | $+30.77 | 0.17 |
| deportes_previo | 47 | 98.12c | 94.74% | 85.8-98.8% | -3.38 pts | $-128.37 | 0.35 |
| otros_cierre | 27 | 99.66c | 100.00% | 87.5-100.0% | +0.34 pts | $+6.18 | 0.36 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 116 | 98.61c | 97.71% | 93.9-99.5% | -0.91 pts | $-79.84 | 0.32 |

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
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $8.66 | 97.4c | 97.0c | deportes_previo |  | Spread: PSS Sleman (-3.5) |
| $91.37 | 98.5c | 98.3c | deportes_previo |  | Spread: Arema FC (-3.5) |
| $31.33 | 95.0c | 95.0c | deportes_previo |  | Spread: Madura United (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6352 | abiertas: 2692 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1941 | 98.88c | 99.12% | +0.25 pts | -0.17 a +0.66 | 17 |
| clima_cierre | tocadas | 1786 | 98.90c | 99.05% | +0.15 pts | -0.30 a +0.60 | 17 |
| cripto_cierre | todas | 984 | 98.76c | 98.58% | -0.18 pts | -0.92 a +0.55 | 14 |
| cripto_cierre | tocadas | 903 | 98.80c | 98.45% | -0.35 pts | -1.15 a +0.45 | 14 |
| deportes_previo | todas | 2653 | 98.08c | 97.15% | -0.93 pts | -1.55 a -0.31 | 78 |
| deportes_previo | tocadas | 2593 | 98.11c | 97.09% | -1.03 pts | -1.66 a -0.39 | 78 |
| otros_cierre | todas | 707 | 99.15c | 98.44% | -0.71 pts | -1.61 a +0.20 | 11 |
| otros_cierre | tocadas | 649 | 99.11c | 98.31% | -0.81 pts | -1.79 a +0.18 | 11 |
| post_fin_90_97 | todas | 67 | 94.19c | 97.01% | +2.83 pts | -1.29 a +6.94 | 2 |
| post_fin_90_97 | tocadas | 51 | 94.25c | 96.08% | +1.83 pts | -3.56 a +7.21 | 2 |
| TOTAL | todas | 6352 | 98.51c | 98.12% | -0.39 pts | -0.72 a -0.06 | 122 |
| TOTAL | tocadas | 5982 | 98.53c | 98.00% | -0.52 pts | -0.87 a -0.17 | 122 |

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

Aun no hay veredicto: van 116 operaciones cerradas en 6.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
