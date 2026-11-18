# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.6 de 28 | corridas: 75
- Capital inicial: $1,000.00 | valor actual: $872.70 | P&L: $-127.30 (-12.73%)
- Efectivo libre: $0.00 | en ordenes abiertas: $514.37 (8) | en posiciones: $358.71 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 174 colocadas, 77 llenadas, 68 tocadas sin llenarse (sorteo 30%), 21 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 25 | 99.00c | 100.00% | 86.7-100.0% | +1.00 pts | $+15.85 | 0.10 |
| deportes_previo | 27 | 97.98c | 90.83% | 76.6-97.9% | -7.15 pts | $-155.21 | 0.45 |
| otros_cierre | 17 | 99.62c | 100.00% | 81.6-100.0% | +0.38 pts | $+3.98 | 0.45 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 72 | 98.60c | 96.15% | 90.4-99.2% | -2.44 pts | $-126.92 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.4c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $86.13 | 96.1c | 100.0c | deportes_previo |  | Tennessee Volunteers vs. Belmont Bruins (W) |
| $86.34 | 98.4c | 98.4c | deportes_previo |  | Spread: Jamaica (-1.5) |
| $35.36 | 99.8c | 99.6c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4111 | abiertas: 1733 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1071 | 98.98c | 99.35% | +0.36 pts | -0.12 a +0.85 | 7 |
| clima_cierre | tocadas | 980 | 98.97c | 99.29% | +0.32 pts | -0.21 a +0.84 | 7 |
| cripto_cierre | todas | 621 | 98.92c | 98.07% | -0.85 pts | -1.92 a +0.22 | 12 |
| cripto_cierre | tocadas | 573 | 98.95c | 97.91% | -1.04 pts | -2.21 a +0.12 | 12 |
| deportes_previo | todas | 1811 | 98.06c | 97.24% | -0.82 pts | -1.57 a -0.07 | 50 |
| deportes_previo | tocadas | 1771 | 98.10c | 97.18% | -0.92 pts | -1.69 a -0.15 | 50 |
| otros_cierre | todas | 568 | 99.30c | 98.77% | -0.53 pts | -1.44 a +0.37 | 7 |
| otros_cierre | tocadas | 512 | 99.26c | 98.63% | -0.63 pts | -1.63 a +0.37 | 7 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 4111 | 98.56c | 98.13% | -0.44 pts | -0.85 a -0.02 | 77 |
| TOTAL | tocadas | 3869 | 98.57c | 98.01% | -0.56 pts | -0.99 a -0.12 | 77 |

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
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5

## Veredicto

Aun no hay veredicto: van 72 operaciones cerradas en 4.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
