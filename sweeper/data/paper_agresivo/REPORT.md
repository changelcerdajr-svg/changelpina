# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 3.6 de 28 | corridas: 49
- Capital inicial: $1,000.00 | valor actual: $818.12 | P&L: $-181.88 (-18.19%)
- Efectivo libre: $-0.00 | en ordenes abiertas: $387.96 (6) | en posiciones: $462.17 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 121 colocadas, 53 llenadas, 45 tocadas sin llenarse (sorteo 30%), 17 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| clima_cierre | 2 | 97.58c | 100.00% | 34.2-100.0% | +2.42 pts | $+4.63 | 1.27 |
| cripto_cierre | 18 | 99.04c | 100.00% | 82.4-100.0% | +0.96 pts | $+12.33 | 0.06 |
| deportes_previo | 16 | 97.96c | 84.92% | 64.0-96.5% | -13.04 pts | $-171.89 | 0.60 |
| otros_cierre | 9 | 99.74c | 100.00% | 70.1-100.0% | +0.26 pts | $+1.23 | 0.68 |
| post_fin_90_97 | 1 | 96.00c | 100.00% | 20.7-100.0% | +4.00 pts | $+3.83 | 0.71 |
| TOTAL | 46 | 98.55c | 94.15% | 85.5-98.8% | -4.40 pts | $-149.87 | 0.44 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|
| $-98.93 | 97.3c | 0.0 | deportes_previo | Spread: Kuwait (-2.5) |
| $-91.92 | 95.0c | 0.0 | deportes_previo | Sudan vs. Senegal: O/U 5.5 |

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $91.77 | 99.8c | 96.5c | otros_cierre |  | Pakistan military action against Afghanistan by November 15, 2026? |
| $54.57 | 98.8c | 50.0c | deportes_previo |  | Derius Davis: Anytime Touchdown |
| $84.54 | 99.9c | 100.0c | deportes_previo |  | Counter-Strike: BANGARANGA vs banda chuya (BO1) - ESEA Advanced Europe Regular S |
| $83.97 | 98.9c | 97.2c | otros_cierre |  | Will the next Grok model (4.8+) be released on November 16, 2026? |
| $59.11 | 99.9c | 98.7c | cripto_cierre |  | Will Microstrategy announce a Bitcoin purchase November 10-16? |
| $80.59 | 98.9c | 98.9c | deportes_previo |  | Tahiti vs. Cook Islands: O/U 0.5 |
| $7.62 | 99.7c | 99.7c | deportes_previo |  | Will Singapore win on 2026-11-17? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2788 | abiertas: 1933 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| clima_cierre | todas | 701 | 99.09c | 99.57% | +0.49 pts | +0.00 a +0.97 | 3 |
| clima_cierre | tocadas | 636 | 99.04c | 99.53% | +0.49 pts | -0.04 a +1.01 | 3 |
| cripto_cierre | todas | 454 | 99.01c | 97.36% | -1.65 pts | -3.11 a -0.19 | 12 |
| cripto_cierre | tocadas | 414 | 99.04c | 97.10% | -1.94 pts | -3.54 a -0.34 | 12 |
| deportes_previo | todas | 1240 | 97.99c | 96.69% | -1.29 pts | -2.29 a -0.30 | 41 |
| deportes_previo | tocadas | 1219 | 98.02c | 96.64% | -1.38 pts | -2.39 a -0.38 | 41 |
| otros_cierre | todas | 358 | 99.26c | 99.44% | +0.18 pts | -0.59 a +0.95 | 2 |
| otros_cierre | tocadas | 342 | 99.26c | 99.42% | +0.15 pts | -0.65 a +0.96 | 2 |
| post_fin_90_97 | todas | 35 | 94.17c | 100.00% | +5.83 pts | +5.27 a +6.38 | 0 |
| post_fin_90_97 | tocadas | 29 | 94.28c | 100.00% | +5.72 pts | +5.12 a +6.32 | 0 |
| TOTAL | todas | 2788 | 98.55c | 97.92% | -0.63 pts | -1.15 a -0.10 | 58 |
| TOTAL | tocadas | 2640 | 98.55c | 97.80% | -0.74 pts | -1.30 a -0.19 | 58 |

Peores casos del registro sombra:

- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Denmark (-2.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Spread: Grizzlies (-30.5)
- 99.8c -> pago 0.0 | deportes_previo | tocada | Union San Felipe vs. Union Espanola: O/U 6.5
- 99.8c -> pago 0.0 | deportes_previo | tocada | Will Drew Sample score the first touchdown?
- 99.7c -> pago 0.0 | deportes_previo | tocada | Will Fernando Mendoza score the first touchdown?
- 99.5c -> pago 0.0 | cripto_cierre | tocada | Will Solana dip to $75 on November 13?
- 99.4c -> pago 0.0 | deportes_previo | tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.9c -> pago 0.0 | deportes_previo | tocada | Spread: Netherlands (-4.5)
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Philippines be the Jury Winner in the Eurovision Asia 2026 Grand Final?

## Veredicto

Aun no hay veredicto: van 46 operaciones cerradas en 3.6 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
