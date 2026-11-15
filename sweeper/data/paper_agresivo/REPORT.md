# Sweeper de Polymarket: reporte del simulador de papel (perfil agresivo)

Dinero virtual. Ninguna orden real. Se regenera en cada corrida.

- Inicio: 2026-11-13T13:15:42Z | dias corridos: 0.2 de 28 | corridas: 7
- Capital inicial: $1,000.00 | valor actual: $914.37 | P&L: $-85.63 (-8.56%)
- Efectivo libre: $0.00 | en ordenes abiertas: $396.32 (5) | en posiciones: $605.50 (7)
- Capital inmovilizado (mercado abierto > 7 dias tras su fecha de fin): $0.00 en 0 posiciones
- Ordenes virtuales: 25 colocadas, 11 llenadas, 9 tocadas sin llenarse (sorteo 30%), 0 expiradas

## Operaciones cerradas: pago real contra precio pagado

| Regla | n | Precio medio | Pago real | IC95 del pago | Edge | P&L | Dias medios |
|---|---|---|---|---|---|---|---|
| cripto_cierre | 3 | 99.43c | 100.00% | 43.8-100.0% | +0.57 pts | $+1.72 | 0.11 |
| otros_cierre | 1 | 99.90c | 100.00% | 20.7-100.0% | +0.10 pts | $+0.10 | 0.15 |
| TOTAL | 4 | 99.55c | 100.00% | 51.0-100.0% | +0.45 pts | $+1.82 | 0.12 |

## Peores casos

| P&L | Precio | Pago | Regla | Mercado |
|---|---|---|---|---|

## Posiciones abiertas

| Costo | Precio | Marca | Regla | Inmovilizada | Mercado |
|---|---|---|---|---|---|
| $100.00 | 98.9c | 96.0c | deportes_previo |  | Spread: Saudi Arabia (-2.5) |
| $100.00 | 98.4c | 97.8c | deportes_previo |  | Spread: Qatar (-2.5) |
| $98.93 | 97.6c | 97.6c | deportes_previo |  | Spread: Australia (-3.5) |
| $98.93 | 97.3c | 17.0c | deportes_previo |  | Spread: Kuwait (-2.5) |
| $100.00 | 99.7c | 97.5c | clima_cierre |  | Exact Score: Coleraine FC 0 - 0 Portadown FC? |
| $97.99 | 99.8c | 99.8c | otros_cierre |  | Will Apple (AAPL) finish week of November 9 above $370? |
| $9.65 | 99.8c | 99.8c | otros_cierre |  | Will Apple (AAPL) finish week of November 9 above $375? |

## Registro sombra: todas las oportunidades detectadas, sin limite de capital

Cada mercado que cumple una regla se anota una vez al precio limite que se habria puesto. "Tocadas" son las que el precio alcanzo en las 12h siguientes (las unicas que un maker podria llenar).

- Resueltas: 0 | abiertas: 1909 | abiertas mas de 7 dias despues de su fecha de fin: 0

## Veredicto

Aun no hay veredicto: van 4 operaciones cerradas en 0.2 dias. El plan pide 4 semanas de papel y aqui se exigen al menos 100 operaciones cerradas antes de concluir.
