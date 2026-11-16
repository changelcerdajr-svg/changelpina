# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.2 de 28 | corridas: 39
- Capital inicial: $1,000.00 | valor actual: $832.64 | P&L: $-167.36 (-16.74%)
- Efectivo libre: $0.00 | en ordenes abiertas: $296.16 (7) | en posiciones: $537.77 (8)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 89 colocadas, 37 llenadas, 32 tocadas sin llenarse (sorteo 30%), 13 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 1 | 99.70c | 100.00% | 20.7-100.0% | +0.30 pts | $+0.30 | 1.87 |
| cripto_cierre | 10 | 99.07c | 100.00% | 72.2-100.0% | +0.93 pts | $+7.24 | 0.07 |
| deportes_previo | 12 | 97.93c | 83.09% | 55.2-95.3% | -14.83 pts | $-174.43 | 0.74 |
| otros_cierre | 6 | 99.66c | 100.00% | 61.0-100.0% | +0.34 pts | $+0.82 | 0.79 |
| TOTAL | 29 | 98.58c | 91.44% | 78.0-98.1% | -7.14 pts | $-166.07 | 0.56 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $90.86 | 99.7c | 96.7c | otros_cierre |  | Will "Ghost Soldier" Opening Weekend Box Office be between 3m and 4m? |
| $91.86 | 96.0c | 97.0c | post_fin_90_97 |  | Florida A&M Rattlers vs. UTEP Miners |
| $91.77 | 99.8c | 96.4c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $82.24 | 95.0c | 99.7c | clima_cierre |  | Will the highest temperature in Paris be 14°C on November 16? |
| $83.25 | 99.8c | 99.8c | cripto_cierre |  | Bitcoin above 66,400 on November 16, 2PM ET? |
| $52.37 | 98.0c | 98.0c | cripto_cierre |  | Ethereum above 1,830 on November 16, 2PM ET? |
| $22.72 | 96.1c | 96.1c | deportes_previo |  | Greece vs. Serbia: Neither team to score first? |
| $22.70 | 99.8c | 98.4c | cripto_cierre |  | Amazon (AMZN) Up or Down on November 16? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2407 | abiertas: 1998 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 562 | 99.10c | 99.47% | +0.36 pts | -0.23 a +0.96 | 3 |
| clima_cierre | tocadas | 517 | 99.06c | 99.42% | +0.36 pts | -0.29 a +1.00 | 3 |
| cripto_cierre | todas | 423 | 99.10c | 97.16% | -1.94 pts | -3.50 a -0.37 | 12 |
| cripto_cierre | tocadas | 388 | 99.11c | 96.91% | -2.20 pts | -3.90 a -0.50 | 12 |
| deportes_previo | todas | 1081 | 97.94c | 96.58% | -1.37 pts | -2.45 a -0.29 | 37 |
| deportes_previo | tocadas | 1063 | 97.98c | 96.52% | -1.46 pts | -2.56 a -0.36 | 37 |
| otros_cierre | todas | 325 | 99.35c | 99.69% | +0.35 pts | -0.26 a +0.95 | 1 |
| otros_cierre | tocadas | 312 | 99.34c | 99.68% | +0.34 pts | -0.30 a +0.97 | 1 |
| post_fin_90_97 | todas | 16 | 95.11c | 100.00% | +4.89 pts | +4.36 a +5.42 | 0 |
| post_fin_90_97 | tocadas | 15 | 95.11c | 100.00% | +4.89 pts | +4.32 a +5.45 | 0 |
| TOTAL | todas | 2407 | 98.59c | 97.80% | -0.79 pts | -1.37 a -0.21 | 53 |
| TOTAL | tocadas | 2295 | 98.58c | 97.69% | -0.89 pts | -1.50 a -0.28 | 53 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?
- 98.9c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 15?

## Veredicto

Aun no hay veredicto: van 29 operaciones cerradas en 3.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
