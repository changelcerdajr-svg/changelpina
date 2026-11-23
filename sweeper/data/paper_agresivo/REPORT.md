# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 9.4 de 28 | corridas: 207
- Capital inicial: $1,000.00 | valor actual: $895.29 | P&L: $-104.71 (-10.47%)
- Efectivo libre: $0.00 | en ordenes abiertas: $224.15 (4) | en posiciones: $680.61 (9)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 416 colocadas, 188 llenadas, 178 tocadas sin llenarse (sorteo 30%), 46 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 5 | 98.28c | 100.00% | 56.6-100.0% | +1.72 pts | $+7.94 | 0.97 |
| cripto_cierre | 53 | 98.76c | 100.00% | 93.2-100.0% | +1.24 pts | $+43.07 | 0.17 |
| deportes_previo | 86 | 97.98c | 95.70% | 90.2-98.8% | -2.28 pts | $-158.03 | 0.28 |
| otros_cierre | 33 | 99.67c | 100.00% | 89.6-100.0% | +0.33 pts | $+7.49 | 0.37 |
| post_fin_90_97 | 2 | 95.85c | 100.00% | 34.2-100.0% | +4.15 pts | $+4.28 | 0.69 |
| TOTAL | 179 | 98.48c | 97.77% | 95.2-99.4% | -0.71 pts | $-95.24 | 0.29 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-95.89 | 97.4c | 0.0 | deportes_previo | FC Schalke 04 vs. VfB Stuttgart: Neither team to score first? |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 89.8c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $35.36 | 99.8c | 98.9c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $4.5m and $5.5m at auction? |
| $87.27 | 99.8c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $26.13 | 95.0c | 100.0c | post_fin_90_97 |  | Will the highest temperature in Chicago be between 58-59°F on November 22? |
| $88.88 | 99.8c | 99.8c | deportes_previo |  | David Njoku: 2+ Touchdowns |
| $88.97 | 97.3c | 97.2c | deportes_previo |  | Spread: Antigua GFC (-1.5) |
| $89.52 | 99.9c | 99.9c | cripto_cierre |  | Bitcoin Up or Down - November 22, 6:35PM-6:40PM ET |
| $89.52 | 99.9c | 99.9c | cripto_cierre |  | BNB Up or Down - November 22, 6:35PM-6:40PM ET |
| $83.18 | 99.8c | 99.8c | cripto_cierre |  | Will Bitcoin reach $72,000 November 16-22? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 10627 | abiertas: 2686 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 2915 | 98.83c | 99.07% | +0.25 pts | -0.10 a +0.59 | 27 |
| clima_cierre | tocadas | 2702 | 98.85c | 99.00% | +0.15 pts | -0.22 a +0.52 | 27 |
| cripto_cierre | todas | 1401 | 98.71c | 98.07% | -0.64 pts | -1.35 a +0.07 | 27 |
| cripto_cierre | tocadas | 1275 | 98.75c | 97.88% | -0.87 pts | -1.65 a -0.09 | 27 |
| deportes_previo | todas | 4946 | 98.00c | 97.38% | -0.62 pts | -1.06 a -0.18 | 132 |
| deportes_previo | tocadas | 4822 | 98.04c | 97.36% | -0.68 pts | -1.13 a -0.23 | 130 |
| otros_cierre | todas | 1210 | 99.01c | 97.27% | -1.73 pts | -2.64 a -0.82 | 33 |
| otros_cierre | tocadas | 1130 | 98.97c | 97.08% | -1.89 pts | -2.87 a -0.92 | 33 |
| post_fin_90_97 | todas | 155 | 94.12c | 93.55% | -0.57 pts | -4.40 a +3.26 | 10 |
| post_fin_90_97 | tocadas | 132 | 94.14c | 92.42% | -1.71 pts | -6.18 a +2.76 | 10 |
| TOTAL | todas | 10627 | 98.38c | 97.87% | -0.51 pts | -0.78 a -0.24 | 229 |
| TOTAL | tocadas | 10061 | 98.40c | 97.77% | -0.63 pts | -0.92 a -0.35 | 227 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will "Heartland" be the top global Netflix movie this week?
- 99.8c -> pago 0.0 | clima_cierre | tocada | Will the highest temperature in Kuala Lumpur be 27°C on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) finish week of November 16 above $270?
- 99.8c -> pago 0.0 | otros_cierre | tocada | Will Amazon (AMZN) close at $245-$250 on the final day of trading of the week of Nov 16 – 

## Veredicto

Aun no hay veredicto: van 179 operaciones cerradas en 9.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
