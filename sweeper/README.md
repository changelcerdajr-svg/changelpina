# Sweeper de Polymarket — SOLO PAPEL

Investigación sin dinero real: ¿los resultados que cotizan a 94-99c en Polymarket pagan $1
más seguido de lo que dice su precio? Ver `PLAN.md` para el plan completo y las reglas duras.

- Sin cuentas, sin wallets, sin llaves, sin órdenes reales.
- Solo lectura de las APIs públicas (Gamma y CLOB).

## Estructura

- `src/fetch_backtest.py` — baja mercados binarios resueltos (36 semanas, volumen >= $5,000) y su
  historial horario de los 10 días previos al cierre a `data/backtest.db` (no se versiona; se regenera).
- `src/analyze_backtest.py` — calibración por horizonte, banda de precio y categoría, con IC de Wilson.
  Escribe `data/backtest_results.csv`.

## Uso

Desde esta carpeta (`sweeper/`):

```bash
python3 src/fetch_backtest.py 36 20000
```

```bash
python3 src/analyze_backtest.py
```

Python 3 estándar, sin dependencias externas.

## Resultado de la Fase 2 (11 nov 2026): NO PASA — el plan se detiene aquí

Muestra: 73,370 mercados binarios resueltos de 36 semanas (hasta ~2,100 por semana, el tope de
paginación de la API; volumen >= $5,000), 19,993 observaciones con el favorito entre 90 y 99c.

| Horizonte antes del cierre | n | Precio medio | Pagó $1 | Edge |
|---|---|---|---|---|
| 1h | 4,206 | 94.78c | 92.82% | -1.96 pts |
| 6h | 4,937 | 95.14c | 92.81% | -2.33 pts |
| 24h | 5,219 | 95.32c | 93.12% | -2.20 pts |
| 72h | 5,631 | 95.41c | 93.80% | -1.61 pts |

- Ninguno de los 88 grupos (categoría x banda x horizonte) cumple el criterio. Los favoritos pagan
  MENOS que su precio en todas las bandas (97-99c: -0.3 a -1.1 pts; 90-95c: -2.4 a -4.1 pts).
- Con selección adversa (la orden maker solo se llena si el precio baja hasta ella) empeora:
  -3 a -7 pts a 6-72h, porque las órdenes que se llenan son justo las de los mercados que se voltean.
- Única señal positiva: política (+1.0 pts a 24h, +1.7 a 6h), pero con n = 150-187 y el límite
  inferior del IC por debajo del precio. No alcanza los 300 casos, menos aún tras el 30% de llenado.
- Capital inmovilizado (`data/stuck_markets.csv`): 1,092 mercados siguen abiertos pasada su fecha de
  fin con el favorito >= 90c (mediana 7 días tarde, 109 con más de 30 días); 1,019 son de política,
  justo la única categoría con señal.

Detalle: `data/backtest_results.csv` y `data/backtest_verdict.csv` (`src/verdict_backtest.py`).
Los archivos `*_top300.csv` son la primera corrida, con solo los 300 mercados de mayor volumen por
semana; daba un edge aún peor (-2 a -4.7 pts) porque esa muestra sobre-representa sorpresas.

Limitaciones: el historial es horario (precio medio/último, no el bid real); la muestra sigue siendo
la de mayor volumen de cada semana; muchos mercados son del mismo partido/evento, así que los IC
reales son más anchos que los de Wilson.

Fases 3 y 4 no se ejecutan: según el plan, sin ventaja en el backtest no hay nada que simular.
