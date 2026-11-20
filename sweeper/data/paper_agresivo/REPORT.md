# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 6.9 de 28 | corridas: 136
- Capital inicial: $1,000.00 | valor actual: $881.68 | P&L: $-118.32 (-11.83%)
- Efectivo libre: $0.00 | en ordenes abiertas: $423.50 (7) | en posiciones: $496.66 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 279 colocadas, 125 llenadas, 117 tocadas sin llenarse (sorteo 30%), 30 expiradas

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
| $91.37 | 98.5c | 97.5c | deportes_previo |  | Spread: Arema FC (-3.5) |
| $31.33 | 95.0c | 95.0c | deportes_previo |  | Spread: Madura United (-2.5) |
| $91.47 | 97.3c | 63.5c | deportes_previo |  | Kashiwa Reysol vs. JEF United Ichihara Chiba: Neither team to score first? |
| $26.00 | 97.8c | 96.5c | deportes_previo |  | Spread: Shimizu S-Pulse (-1.5) |
| $33.43 | 98.4c | 98.0c | deportes_previo |  | Spread: Imisli FK (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 6421 | abiertas: 2755 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 1965 | 98.88c | 99.13% | +0.26 pts | -0.15 a +0.66 | 17 |
| clima_cierre | tocadas | 1808 | 98.90c | 99.06% | +0.16 pts | -0.28 a +0.60 | 17 |
| cripto_cierre | todas | 1000 | 98.77c | 98.60% | -0.17 pts | -0.89 a +0.56 | 14 |
| cripto_cierre | tocadas | 919 | 98.81c | 98.48% | -0.33 pts | -1.12 a +0.45 | 14 |
| deportes_previo | todas | 2678 | 98.08c | 97.18% | -0.90 pts | -1.52 a -0.28 | 78 |
| deportes_previo | tocadas | 2618 | 98.11c | 97.12% | -0.99 pts | -1.63 a -0.36 | 78 |
| otros_cierre | todas | 711 | 99.15c | 98.45% | -0.70 pts | -1.60 a +0.20 | 11 |
| otros_cierre | tocadas | 653 | 99.11c | 98.32% | -0.80 pts | -1.78 a +0.18 | 11 |
| post_fin_90_97 | todas | 67 | 94.19c | 97.01% | +2.83 pts | -1.29 a +6.94 | 2 |
| post_fin_90_97 | tocadas | 51 | 94.25c | 96.08% | +1.83 pts | -3.56 a +7.21 | 2 |
| TOTAL | todas | 6421 | 98.51c | 98.14% | -0.37 pts | -0.70 a -0.04 | 122 |
| TOTAL | tocadas | 6049 | 98.53c | 98.02% | -0.50 pts | -0.85 a -0.16 | 122 |

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

Aun no hay veredicto: van 116 operaciones cerradas en 6.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
