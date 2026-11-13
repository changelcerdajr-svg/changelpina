# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 0.1 de 28 | corridas: 4
- Capital inicial: $1,000.00 | valor actual: $995.82 | P&L: $-4.18 (-0.42%)
- Efectivo libre: $4.21 | en ordenes abiertas: $298.33 (3) | en posiciones: $697.86 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 20 colocadas, 9 llenadas, 8 tocadas sin llenarse (sorteo 30%), 0 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 2 | 99.80c | 100.00% | 34.2-100.0% | +0.20 pts | $+0.40 | 0.08 |
| TOTAL | 2 | 99.80c | 100.00% | 34.2-100.0% | +0.20 pts | $+0.40 | 0.08 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $100.00 | 98.9c | 96.0c | deportes_previo |  | Spread: Saudi Arabia (-2.5) |
| $100.00 | 98.4c | 97.8c | deportes_previo |  | Spread: Qatar (-2.5) |
| $98.93 | 97.6c | 97.6c | deportes_previo |  | Spread: Australia (-3.5) |
| $100.00 | 99.9c | 100.0c | otros_cierre |  | Will the US national average gas price be less than $3.8900 on November 13? |
| $98.93 | 97.3c | 97.3c | deportes_previo |  | Spread: Kuwait (-2.5) |
| $100.00 | 98.7c | 99.7c | cripto_cierre |  | Will the price of Bitcoin be between $72,000 and $74,000 on November 13? |
| $100.00 | 99.7c | 97.6c | clima_cierre |  | Exact Score: Coleraine FC 0 - 0 Portadown FC? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 0 | abiertas: 1605 | abiertas mas de 7 dias despues de su fecha de fin: 0

## Veredicto

Aun no hay veredicto: van 2 operaciones cerradas en 0.1 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
