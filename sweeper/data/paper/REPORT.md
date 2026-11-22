# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 10.3 de 28 | corridas: 223
- Capital inicial: $1,000.00 | valor actual: $1,074.27 | P&L: $+74.27 (+7.43%)
- Efectivo libre: $432.90 | en ordenes abiertas: $482.91 (9) | en posiciones: $158.52 (3)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 377 colocadas, 93 llenadas, 189 tocadas sin llenarse (sorteo 30%), 86 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 26 | 98.90c | 100.00% | 87.1-100.0% | +1.10 pts | $+15.05 | 0.28 |
| deportes_previo | 34 | 98.26c | 100.00% | 89.8-100.0% | +1.74 pts | $+31.04 | 0.34 |
| otros_cierre | 22 | 99.06c | 100.00% | 85.1-100.0% | +0.94 pts | $+10.74 | 0.44 |
| post_fin_95_97 | 8 | 95.97c | 100.00% | 67.6-100.0% | +4.03 pts | $+17.50 | 0.42 |
| TOTAL | 90 | 98.43c | 100.00% | 95.9-100.0% | +1.57 pts | $+74.33 | 0.36 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $53.03 | 99.2c | 99.3c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $53.66 | 98.1c | 98.1c | otros_cierre |  | Will xQc finish GTA VI by November 22, 3:59 AM ET? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3377 | abiertas: 652 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 994 | 98.73c | 98.99% | +0.26 pts | -0.36 a +0.88 | 10 |
| cripto_cierre | tocadas | 676 | 98.56c | 98.52% | -0.04 pts | -0.95 a +0.87 | 10 |
| deportes_previo | todas | 1823 | 98.31c | 99.01% | +0.70 pts | +0.25 a +1.15 | 19 |
| deportes_previo | tocadas | 1537 | 98.27c | 98.96% | +0.68 pts | +0.19 a +1.18 | 17 |
| otros_cierre | todas | 531 | 98.80c | 99.25% | +0.44 pts | -0.30 a +1.18 | 4 |
| otros_cierre | tocadas | 358 | 98.70c | 98.88% | +0.19 pts | -0.91 a +1.28 | 4 |
| post_fin_95_97 | todas | 29 | 96.10c | 93.10% | -3.00 pts | -12.35 a +6.35 | 2 |
| post_fin_95_97 | tocadas | 24 | 96.12c | 91.67% | -4.45 pts | -15.70 a +6.80 | 2 |
| TOTAL | todas | 3377 | 98.49c | 98.99% | +0.50 pts | +0.17 a +0.83 | 35 |
| TOTAL | tocadas | 2595 | 98.39c | 98.77% | +0.38 pts | -0.04 a +0.80 | 33 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.9c -> pago 0.0 | deportes_previo | tocada | Dundee FC vs. Heart of Midlothian FC: O/U 7.5
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $56,000 on November 20?
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?

## Veredicto

Aun no hay veredicto: van 90 operaciones cerradas en 10.3 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
