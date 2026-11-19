# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.3 de 28 | corridas: 120
- Capital inicial: $1,000.00 | valor actual: $898.32 | P&L: $-101.68 (-10.17%)
- Efectivo libre: $0.00 | en ordenes abiertas: $158.15 (3) | en posiciones: $748.02 (10)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 246 colocadas, 112 llenadas, 103 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 4 | 97.87c | 100.00% | 51.0-100.0% | +2.13 pts | $+7.75 | 1.02 |
| cripto_cierre | 34 | 98.78c | 100.00% | 89.8-100.0% | +1.22 pts | $+27.63 | 0.17 |
| deportes_previo | 41 | 98.17c | 94.08% | 83.9-98.7% | -4.09 pts | $-137.85 | 0.38 |
| otros_cierre | 22 | 99.66c | 100.00% | 85.1-100.0% | +0.34 pts | $+4.80 | 0.40 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 102 | 98.60c | 97.38% | 93.1-99.5% | -1.22 pts | $-93.83 | 0.34 |

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
| $87.27 | 99.8c | 98.4c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $89.46 | 99.8c | 99.0c | deportes_previo |  | Spread: CA Progreso (-2.5) |
| $51.73 | 99.8c | 99.8c | deportes_previo |  | Spread: Cerro Largo FC (-3.5) |
| $90.13 | 99.7c | 98.0c | otros_cierre |  | Will Apple (AAPL) close above $355 on November 19? |
| $55.98 | 99.7c | 99.6c | otros_cierre |  | Will Microsoft (MSFT) close above $520 on November 19? |
| $71.88 | 98.7c | 97.9c | cripto_cierre |  | Airbnb (ABNB) Up or Down on November 19? |
| $85.33 | 97.7c | 98.1c | cripto_cierre |  | Tesla (TSLA) Up or Down on November 19? |
| $89.12 | 99.8c | 99.8c | cripto_cierre |  | Amazon (AMZN) Up or Down on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 5837 | abiertas: 2473 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1694 | 98.90c | 99.06% | +0.16 pts | -0.30 a +0.62 | 16 |
| clima_cierre | tocadas | 1555 | 98.90c | 98.97% | +0.07 pts | -0.43 a +0.56 | 16 |
| cripto_cierre | todas | 951 | 98.78c | 98.53% | -0.25 pts | -1.01 a +0.51 | 14 |
| cripto_cierre | tocadas | 874 | 98.82c | 98.40% | -0.42 pts | -1.25 a +0.40 | 14 |
| deportes_previo | todas | 2445 | 98.08c | 97.10% | -0.98 pts | -1.65 a -0.32 | 71 |
| deportes_previo | tocadas | 2388 | 98.11c | 97.03% | -1.08 pts | -1.76 a -0.40 | 71 |
| otros_cierre | todas | 686 | 99.17c | 98.54% | -0.63 pts | -1.52 a +0.26 | 10 |
| otros_cierre | tocadas | 628 | 99.13c | 98.41% | -0.73 pts | -1.70 a +0.25 | 10 |
| post_fin_90_97 | todas | 61 | 94.11c | 96.72% | +2.61 pts | -1.91 a +7.13 | 2 |
| post_fin_90_97 | tocadas | 47 | 94.13c | 95.74% | +1.61 pts | -4.23 a +7.45 | 2 |
| TOTAL | todas | 5837 | 98.52c | 98.06% | -0.45 pts | -0.80 a -0.10 | 113 |
| TOTAL | tocadas | 5492 | 98.53c | 97.94% | -0.59 pts | -0.96 a -0.22 | 113 |

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

Aun no hay veredicto: van 102 operaciones cerradas en 6.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
