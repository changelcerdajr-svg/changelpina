# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 0.7 de 28 | corridas: 17
- Capital inicial: $1,000.00 | valor actual: $999.24 | P&L: $-0.76 (-0.08%)
- Efectivo libre: $400.81 | en ordenes abiertas: $349.62 (7) | en posiciones: $249.78 (5)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 34 colocadas, 6 llenadas, 16 tocadas sin llenarse (sorteo 30%), 5 expiradas

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
| $50.00 | 97.7c | 97.5c | deportes_previo |  | Will Somalia win on 2026-11-12? |
| $50.01 | 99.4c | 99.5c | deportes_previo |  | Spread: Somalia (-1.5) |
| $50.02 | 98.5c | 97.2c | cripto_cierre |  | Will the price of Ethereum be above $1,900 on November 12? |
| $50.02 | 99.8c | 99.4c | cripto_cierre |  | Will the price of Ethereum be above $1,800 on November 12? |
| $49.73 | 97.7c | 97.7c | deportes_previo |  | Spread: CSD Mixco (-2.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 39 | abiertas: 326 | abiertas mas de 7 dias despues de su fecha de fin: 0

| Regla | Grupo | n | Precio medio | Pago real | Edge | IC95 del edge | Perdidas |
|---|---|---|---|---|---|---|---|
| cripto_cierre | todas | 34 | 99.05c | 100.00% | +0.95 pts | +0.74 a +1.16 | 0 |
| cripto_cierre | tocadas | 18 | 98.96c | 100.00% | +1.04 pts | +0.72 a +1.37 | 0 |
| deportes_previo | todas | 2 | 98.05c | 100.00% | +1.95 pts | +1.26 a +2.64 | 0 |
| deportes_previo | tocadas | 2 | 98.05c | 100.00% | +1.95 pts | +1.26 a +2.64 | 0 |
| otros_cierre | todas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| otros_cierre | tocadas | 3 | 98.97c | 100.00% | +1.03 pts | +0.41 a +1.66 | 0 |
| TOTAL | todas | 39 | 98.99c | 100.00% | +1.01 pts | +0.81 a +1.21 | 0 |
| TOTAL | tocadas | 23 | 98.88c | 100.00% | +1.12 pts | +0.84 a +1.41 | 0 |

## Veredicto

Aun no hay veredicto: van 1 operaciones cerradas en 0.7 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
