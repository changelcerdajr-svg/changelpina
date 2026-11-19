# Sweeper de Polymarket: reporte del simulador de papel (perfil base)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 7.5 de 28 | corridas: 144
- Capital inicial: $1,000.00 | valor actual: $1,043.42 | P&L: $+43.42 (+4.34%)
- Efectivo libre: $364.92 | en ordenes abiertas: $417.14 (8) | en posiciones: $260.36 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 247 colocadas, 63 llenadas, 115 tocadas sin llenarse (sorteo 30%), 61 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 17 | 98.77c | 100.00% | 81.6-100.0% | +1.23 pts | $+10.88 | 0.19 |
| deportes_previo | 22 | 98.41c | 100.00% | 85.1-100.0% | +1.59 pts | $+18.06 | 0.35 |
| otros_cierre | 16 | 99.05c | 100.00% | 80.6-100.0% | +0.95 pts | $+7.82 | 0.56 |
| post_fin_95_97 | 3 | 96.40c | 100.00% | 43.8-100.0% | +3.60 pts | $+5.66 | 0.72 |
| TOTAL | 58 | 98.59c | 100.00% | 93.8-100.0% | +1.41 pts | $+42.42 | 0.38 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $51.82 | 98.5c | 98.8c | otros_cierre |  | Will Mark Rothko's “Untitled” sell for between $3.5m and $4.5m at auction? |
| $52.07 | 96.1c | 97.4c | post_fin_95_97 |  | Will the highest temperature in Seattle be between 54-55°F on November 18? |
| $52.15 | 97.3c | 97.6c | deportes_previo |  | Will Shan United win on 2026-11-19? |
| $52.16 | 99.5c | 99.5c | otros_cierre |  | Walmart (WMT) Q3 US comp sales (ex-fuel) growth <1%? |
| $52.16 | 99.7c | 99.7c | cripto_cierre |  | Will the price of Bitcoin be between $68,000 and $70,000 on November 19? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 2184 | abiertas: 227 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 730 | 98.72c | 99.04% | +0.32 pts | -0.39 a +1.02 | 7 |
| cripto_cierre | tocadas | 503 | 98.56c | 98.61% | +0.05 pts | -0.97 a +1.07 | 7 |
| deportes_previo | todas | 1076 | 98.37c | 99.07% | +0.70 pts | +0.12 a +1.27 | 10 |
| deportes_previo | tocadas | 900 | 98.33c | 99.11% | +0.78 pts | +0.17 a +1.40 | 8 |
| otros_cierre | todas | 353 | 98.75c | 99.72% | +0.97 pts | +0.40 a +1.53 | 1 |
| otros_cierre | tocadas | 231 | 98.65c | 99.57% | +0.92 pts | +0.06 a +1.78 | 1 |
| post_fin_95_97 | todas | 25 | 96.08c | 92.00% | -4.08 pts | -14.90 a +6.74 | 2 |
| post_fin_95_97 | tocadas | 20 | 96.09c | 90.00% | -6.09 pts | -19.53 a +7.35 | 2 |
| TOTAL | todas | 2184 | 98.53c | 99.08% | +0.56 pts | +0.16 a +0.96 | 20 |
| TOTAL | tocadas | 1654 | 98.41c | 98.91% | +0.50 pts | -0.00 a +1.00 | 18 |

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

Aun no hay veredicto: van 58 operaciones cerradas en 7.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
