# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.2 de 28 | corridas: 116
- Capital inicial: $1,000.00 | valor actual: $894.57 | P&L: $-105.43 (-10.54%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $402.26 (6) | en posiciones: $496.52 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 230 colocadas, 105 llenadas, 91 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 30 | 98.97c | 100.00% | 88.6-100.0% | +1.03 pts | $+20.65 | 0.18 |
| deportes_previo | 40 | 98.16c | 94.01% | 83.5-98.6% | -4.15 pts | $-138.24 | 0.38 |
| otros_cierre | 22 | 99.66c | 100.00% | 85.1-100.0% | +0.34 pts | $+4.80 | 0.40 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 97 | 98.65c | 97.28% | 92.8-99.4% | -1.37 pts | $-101.21 | 0.35 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.7c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $39.06 | 99.0c | 98.5c | deportes_previo |  | Spread: Al Dhafra SSC (-1.5) |
| $36.90 | 95.6c | 96.3c | cripto_cierre |  | Will the price of Bitcoin be less than $62,000 on November 19? |
| $87.72 | 99.8c | 100.0c | cripto_cierre |  | Will the price of Ethereum be above $1,600 on November 19? |
| $89.05 | 95.3c | 95.3c | cripto_cierre |  | Will the price of Bitcoin be between $62,000 and $64,000 on November 19? |
| $29.38 | 97.6c | 97.6c | cripto_cierre |  | Will the price of Bitcoin be between $64,000 and $66,000 on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5673 | abiertas: 2337 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1676 | 98.90c | 99.11% | +0.21 pts | -0.24 a +0.66 | 15 |
| clima_cierre | tocadas | 1537 | 98.91c | 99.02% | +0.12 pts | -0.37 a +0.61 | 15 |
| cripto_cierre | todas | 871 | 98.79c | 98.39% | -0.40 pts | -1.23 a +0.43 | 14 |
| cripto_cierre | tocadas | 800 | 98.83c | 98.25% | -0.58 pts | -1.48 a +0.32 | 14 |
| deportes_previo | todas | 2396 | 98.09c | 97.12% | -0.97 pts | -1.63 a -0.30 | 69 |
| deportes_previo | tocadas | 2340 | 98.11c | 97.05% | -1.06 pts | -1.74 a -0.38 | 69 |
| otros_cierre | todas | 673 | 99.17c | 98.51% | -0.66 pts | -1.57 a +0.25 | 10 |
| otros_cierre | tocadas | 615 | 99.13c | 98.37% | -0.76 pts | -1.75 a +0.24 | 10 |
| post_fin_90_97 | todas | 57 | 94.08c | 96.49% | +2.41 pts | -2.42 a +7.24 | 2 |
| post_fin_90_97 | tocadas | 45 | 94.14c | 95.56% | +1.41 pts | -4.68 a +7.51 | 2 |
| TOTAL | todas | 5673 | 98.52c | 98.06% | -0.46 pts | -0.82 a -0.11 | 110 |
| TOTAL | tocadas | 5337 | 98.53c | 97.94% | -0.59 pts | -0.97 a -0.22 | 110 |

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

Aun no hay veredicto: van 97 operaciones cerradas en 6.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
