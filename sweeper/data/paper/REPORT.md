# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 9.9 de 28 | corridas: 210
- Capital inicial: $1,000.00 | valor actual: $1,062.65 | P&L: $+62.65 (+6.26%)
- Efectivo libre: $428.44 | en ordenes abiertas: $318.01 (6) | en posiciones: $316.93 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 353 colocadas, 88 llenadas, 176 tocadas sin llenarse (sorteo 30%), 83 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 23 | 98.91c | 100.00% | 85.7-100.0% | +1.09 pts | $+13.16 | 0.22 |
| deportes_previo | 32 | 98.22c | 100.00% | 89.3-100.0% | +1.78 pts | $+29.80 | 0.34 |
| otros_cierre | 22 | 99.06c | 100.00% | 85.1-100.0% | +0.94 pts | $+10.74 | 0.44 |
| post_fin_95_97 | 5 | 96.36c | 100.00% | 56.6-100.0% | +3.64 pts | $+9.68 | 0.65 |
| TOTAL | 82 | 98.52c | 100.00% | 95.5-100.0% | +1.48 pts | $+63.38 | 0.36 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.3c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $53.03 | 99.6c | 99.5c | deportes_previo |  | Chattanooga vs. Alabama |
| $53.03 | 99.2c | 99.2c | otros_cierre |  | Will the next Claude Opus model (5.6+) be released on November 21, 2026? |
| $53.03 | 99.2c | 99.2c | cripto_cierre |  | Will Bitcoin reach $64,000 on November 21? |
| $52.99 | 97.9c | 96.9c | cripto_cierre |  | Will Bitcoin reach $63,000 on November 21? |
| $53.01 | 99.4c | 99.5c | cripto_cierre |  | Will Ethereum reach $1,900 on November 21? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 3156 | abiertas: 445 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 968 | 98.74c | 98.97% | +0.22 pts | -0.41 a +0.86 | 10 |
| cripto_cierre | tocadas | 652 | 98.57c | 98.47% | -0.10 pts | -1.04 a +0.84 | 10 |
| deportes_previo | todas | 1629 | 98.33c | 99.20% | +0.87 pts | +0.45 a +1.30 | 14 |
| deportes_previo | tocadas | 1365 | 98.29c | 99.19% | +0.91 pts | +0.44 a +1.37 | 12 |
| otros_cierre | todas | 530 | 98.80c | 99.25% | +0.44 pts | -0.30 a +1.18 | 4 |
| otros_cierre | tocadas | 358 | 98.70c | 98.88% | +0.19 pts | -0.91 a +1.28 | 4 |
| post_fin_95_97 | todas | 29 | 96.10c | 93.10% | -3.00 pts | -12.35 a +6.35 | 2 |
| post_fin_95_97 | tocadas | 24 | 96.12c | 91.67% | -4.45 pts | -15.70 a +6.80 | 2 |
| TOTAL | todas | 3156 | 98.52c | 99.08% | +0.57 pts | +0.24 a +0.90 | 30 |
| TOTAL | tocadas | 2399 | 98.40c | 98.87% | +0.47 pts | +0.05 a +0.89 | 28 |

Peores casos del registro sombra:

- 99.4c -> pago 0.0 | otros_cierre | tocada | Will Paul Cézanne's “Arlequin” sell for between $110m and $120m at auction?
- 99.1c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $69,000 on November 12?
- 99.1c -> pago 0.0 | otros_cierre | tocada | Will Microsoft (MSFT) close above $500 on November 19?
- 98.9c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $275 on November 19?
- 98.8c -> pago 0.0 | deportes_previo | no tocada | Milton Keynes Dons FC vs. Burton Albion FC: O/U 7.5
- 98.8c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $57,000 on November 20?
- 98.7c -> pago 0.0 | otros_cierre | tocada | Will Google (GOOGL) close above $280 on November 19?
- 98.6c -> pago 0.0 | cripto_cierre | tocada | Will Bitcoin dip to $56,000 on November 20?
- 98.5c -> pago 0.0 | cripto_cierre | tocada | Will the price of Solana be above $75 on November 14?
- 98.4c -> pago 0.0 | deportes_previo | tocada | Netherlands vs. Greece: Netherlands O/U 5.5

## Veredicto

Aun no hay veredicto: van 82 operaciones cerradas en 9.9 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
