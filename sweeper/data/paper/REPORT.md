# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 8.2 de 28 | corridas: 164
- Capital inicial: $1,000.00 | valor actual: $1,047.30 | P&L: $+47.30 (+4.73%)
- Efectivo libre: $419.47 | en ordenes abiertas: $418.70 (8) | en posiciones: $208.82 (4)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 287 colocadas, 68 llenadas, 142 tocadas sin llenarse (sorteo 30%), 69 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 18 | 98.82c | 100.00% | 82.4-100.0% | +1.18 pts | $+11.04 | 0.20 |
| deportes_previo | 23 | 98.36c | 100.00% | 85.7-100.0% | +1.64 pts | $+19.51 | 0.36 |
| otros_cierre | 19 | 99.12c | 100.00% | 83.2-100.0% | +0.88 pts | $+8.66 | 0.49 |
| post_fin_95_97 | 4 | 96.32c | 100.00% | 51.0-100.0% | +3.68 pts | $+7.77 | 0.68 |
| TOTAL | 64 | 98.59c | 100.00% | 94.3-100.0% | +1.41 pts | $+46.98 | 0.37 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.5c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.37 | 99.3c | 99.3c | otros_cierre |  | Will the next Meta Muse Spark model be released on November 19, 2026? |
| $52.31 | 99.5c | 99.8c | cripto_cierre |  | Will Bitcoin reach $68,000 on November 19? |
| $52.32 | 99.2c | 99.6c | cripto_cierre |  | Will Ethereum reach $1,950 on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2328 | abiertas: 341 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 795 | 98.74c | 99.12% | +0.38 pts | -0.27 a +1.03 | 7 |
| cripto_cierre | tocadas | 536 | 98.56c | 98.69% | +0.14 pts | -0.82 a +1.09 | 7 |
| deportes_previo | todas | 1129 | 98.36c | 99.11% | +0.75 pts | +0.20 a +1.30 | 10 |
| deportes_previo | tocadas | 947 | 98.32c | 99.16% | +0.83 pts | +0.25 a +1.42 | 8 |
| otros_cierre | todas | 377 | 98.75c | 99.73% | +0.98 pts | +0.45 a +1.51 | 1 |
| otros_cierre | tocadas | 247 | 98.65c | 99.60% | +0.94 pts | +0.14 a +1.75 | 1 |
| post_fin_95_97 | todas | 27 | 96.10c | 92.59% | -3.51 pts | -13.54 a +6.52 | 2 |
| post_fin_95_97 | tocadas | 22 | 96.12c | 90.91% | -5.21 pts | -17.46 a +7.04 | 2 |
| TOTAL | todas | 2328 | 98.53c | 99.14% | +0.61 pts | +0.24 a +0.99 | 20 |
| TOTAL | tocadas | 1752 | 98.41c | 98.97% | +0.56 pts | +0.09 a +1.03 | 18 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5
- 98.4c -> pago 0.0 | deportes_previo | tocada | Spread: Latina Calcio (-3.5)
- 98.4c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be less than $66,000 on November 14?
- 98.3c -> pago 0.0 | deportes_previo | no tocada | Spread: Denmark (-2.5)
- 98.2c -> pago 0.0 | deportes_previo | tocada | Spread: Libya (-1.5)
- 97.8c -> pago 0.0 | cripto_cierre | tocada | Will the price of Bitcoin be between $70,000 and $72,000 on November 12?

## Veredicto

Aun no hay veredicto: van 64 operaciones cerradas en 8.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
