# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 4.7 de 28 | corridas: 77
- Capital inicial: $1,000.00 | valor actual: $871.61 | P&L: $-128.39 (-12.84%)
- Efectivo libre: $0.58 | en ordenes abiertas: $259.81 (3) | en posiciones: $616.54 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 179 colocadas, 82 llenadas, 72 tocadas sin llenarse (sorteo 30%), 22 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 26 | 99.03c | 100.00% | 87.1-100.0% | +0.97 pts | $+16.20 | 0.09 |
| deportes_previo | 28 | 97.90c | 91.19% | 77.4-98.0% | -6.71 pts | $-151.71 | 0.44 |
| otros_cierre | 17 | 99.62c | 100.00% | 81.6-100.0% | +0.38 pts | $+3.98 | 0.45 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 74 | 98.57c | 96.28% | 90.7-99.3% | -2.29 pts | $-123.07 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.2c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $59.11 | 99.9c | 98.9c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $86.34 | 98.4c | 98.4c | deportes_previo |  | Spread: Jamaica (-1.5) |
| $35.36 | 99.8c | 99.6c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $87.28 | 99.8c | 99.8c | deportes_previo |  | Will UK annual inflation be between 4.0% and 4.2% in October? |
| $87.28 | 97.9c | 97.9c | clima_cierre |  | Will the highest temperature in London be 11°C on November 18? |
| $82.12 | 98.5c | 98.5c | clima_cierre |  | Will the highest temperature in Paris be 13°C on November 18? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 4225 | abiertas: 1712 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1091 | 98.98c | 99.36% | +0.38 pts | -0.09 a +0.85 | 7 |
| clima_cierre | tocadas | 997 | 98.97c | 99.30% | +0.33 pts | -0.18 a +0.85 | 7 |
| cripto_cierre | todas | 625 | 98.92c | 98.08% | -0.84 pts | -1.90 a +0.23 | 12 |
| cripto_cierre | tocadas | 576 | 98.95c | 97.92% | -1.03 pts | -2.19 a +0.13 | 12 |
| deportes_previo | todas | 1898 | 98.08c | 97.31% | -0.77 pts | -1.49 a -0.04 | 51 |
| deportes_previo | tocadas | 1858 | 98.12c | 97.26% | -0.86 pts | -1.60 a -0.13 | 51 |
| otros_cierre | todas | 571 | 99.30c | 98.77% | -0.53 pts | -1.43 a +0.37 | 7 |
| otros_cierre | tocadas | 515 | 99.27c | 98.64% | -0.62 pts | -1.62 a +0.37 | 7 |
| post_fin_90_97 | todas | 40 | 94.19c | 97.50% | +3.31 pts | -1.61 a +8.22 | 1 |
| post_fin_90_97 | tocadas | 33 | 94.30c | 96.97% | +2.67 pts | -3.28 a +8.61 | 1 |
| TOTAL | todas | 4225 | 98.56c | 98.15% | -0.41 pts | -0.81 a -0.01 | 78 |
| TOTAL | tocadas | 3979 | 98.57c | 98.04% | -0.53 pts | -0.96 a -0.10 | 78 |

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

Aun no hay veredicto: van 74 operaciones cerradas en 4.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
