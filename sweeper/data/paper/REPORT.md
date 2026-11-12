# Sweeper de Polymarket: reporte del simulador de papel

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-11T22:05:26Z | dias corridos: 0.5 de 28 | corridas: 11
- Capital inicial: $1,000.00 | valor actual: $1,000.30 | P&L: $+0.30 (+0.03%)
- Efectivo libre: $400.24 | en ordenes abiertas: $499.95 (10) | en posiciones: $100.01 (2)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 20 colocadas, 3 llenadas, 7 tocadas sin llenarse (sorteo 30%), 0 expiradas

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
| $50.00 | 97.7c | 97.9c | deportes_previo |  | Will Somalia win on 2026-11-12? |
| $50.01 | 99.4c | 99.4c | deportes_previo |  | Spread: Somalia (-1.5) |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 0 | abiertas: 281 | abiertas mas de 7 dias despues de su fecha de fin: 0

## Veredicto

Aun no hay veredicto: van 1 operaciones cerradas en 0.5 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
