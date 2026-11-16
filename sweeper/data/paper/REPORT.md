# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 4.4 de 28 | corridas: 64
- Capital inicial: $1,000.00 | valor actual: $1,020.17 | P&L: $+20.17 (+2.02%)
- Efectivo libre: $408.30 | en ordenes abiertas: $509.40 (10) | en posiciones: $101.78 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 116 colocadas, 30 llenadas, 48 tocadas sin llenarse (sorteo 30%), 28 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 6 | 98.86c | 100.00% | 61.0-100.0% | +1.14 pts | $+3.48 | 0.24 |
| deportes_previo | 13 | 98.72c | 100.00% | 77.2-100.0% | +1.28 pts | $+8.49 | 0.35 |
| otros_cierre | 7 | 98.87c | 100.00% | 64.6-100.0% | +1.13 pts | $+4.03 | 0.67 |
| post_fin_95_97 | 2 | 96.65c | 100.00% | 34.2-100.0% | +3.35 pts | $+3.50 | 0.85 |
| TOTAL | 28 | 98.64c | 100.00% | 87.9-100.0% | +1.36 pts | $+19.49 | 0.44 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.87 | 98.0c | 99.0c | otros_cierre |  | Next Astra Model (6.1+) released by November 15, 2026? |
| $50.92 | 99.2c | 99.5c | otros_cierre |  | Will the USS Theodore Roosevelt arrive in CENTCOM by November 15, 2026? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 1093 | abiertas: 370 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 361 | 98.78c | 98.06% | -0.72 pts | -2.14 a +0.69 | 7 |
| cripto_cierre | tocadas | 254 | 98.68c | 97.24% | -1.44 pts | -3.45 a +0.57 | 7 |
| deportes_previo | todas | 548 | 98.44c | 98.54% | +0.10 pts | -0.91 a +1.10 | 8 |
| deportes_previo | tocadas | 461 | 98.39c | 98.70% | +0.31 pts | -0.72 a +1.34 | 6 |
| otros_cierre | todas | 177 | 98.59c | 100.00% | +1.41 pts | +1.30 a +1.51 | 0 |
| otros_cierre | tocadas | 125 | 98.49c | 100.00% | +1.51 pts | +1.38 a +1.64 | 0 |
| post_fin_95_97 | todas | 7 | 95.91c | 71.43% | -24.49 pts | -60.55 a +11.58 | 2 |
| post_fin_95_97 | tocadas | 7 | 95.91c | 71.43% | -24.49 pts | -60.55 a +11.58 | 2 |
| TOTAL | todas | 1093 | 98.56c | 98.44% | -0.12 pts | -0.85 a +0.61 | 17 |
| TOTAL | tocadas | 847 | 98.47c | 98.23% | -0.24 pts | -1.13 a +0.64 | 15 |

Peores casos del registro sombra:

- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5
- 98.4c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 98.4c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 14?
- 98.3c -> pago 0.0 | deportes_previo | no tocada | Spread: Denmark (-2.5)
- 98.2c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?
- 97.7c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be above $66,000 on November 14?

## Veredicto

Aun no hay veredicto: van 28 operaciones cerradas en 4.4 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
