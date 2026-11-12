# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 0.8 de 28 | corridas: 18
- Capital inicial: $1,000.00 | valor actual: $1,001.43 | P&L: $+1.43 (+0.14%)
- Efectivo libre: $400.70 | en ordenes abiertas: $299.88 (6) | en posiciones: $299.62 (6)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 35 colocadas, 7 llenadas, 17 tocadas sin llenarse (sorteo 30%), 5 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| otros_cierre | 1 | 99.60c | 100.00% | 20.7-100.0% | +0.40 pts | $+0.20 | 0.17 |
| TOTAL | 1 | 99.60c | 100.00% | 20.7-100.0% | +0.40 pts | $+0.20 | 0.17 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $50.00 | 97.7c | 99.6c | deportes_previo |  | Will Somalia win on 2026-11-12? |
| $50.01 | 99.4c | 99.5c | deportes_previo |  | Spread: Somalia (-1.5) |
| $50.02 | 98.5c | 99.7c | cripto_cierre |  | Will the price of Ethereum be above $1,900 on November 12? |
| $50.02 | 99.8c | 99.8c | cripto_cierre |  | Will the price of Ethereum be above $1,800 on November 12? |
| $49.85 | 99.6c | 99.6c | cripto_cierre |  | Will the price of Bitcoin be between $74,000 and $76,000 on November 12? |
| $49.73 | 97.7c | 97.0c | deportes_previo |  | Spread: CSD Mixco (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 42 | abiertas: 333 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 37 | 99.05c | 100.00% | +0.95 pts | +0.75 a +1.15 | 0 |
| cripto_cierre | tocadas | 19 | 98.97c | 100.00% | +1.03 pts | +0.72 a +1.34 | 0 |
| deportes_previo | todas | 2 | 98.05c | 100.00% | +1.95 pts | +1.26 a +2.64 | 0 |
| deportes_previo | tocadas | 2 | 98.05c | 100.00% | +1.95 pts | +1.26 a +2.64 | 0 |
| otros_cierre | todas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| otros_cierre | tocadas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| TOTAL | todas | 42 | 99.00c | 100.00% | +1.00 pts | +0.81 a +1.19 | 0 |
| TOTAL | tocadas | 24 | 98.89c | 100.00% | +1.11 pts | +0.83 a +1.38 | 0 |

## Veredicto

Aun no hay veredicto: van 1 operaciones cerradas en 0.8 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
