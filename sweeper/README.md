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
python3 src/fetch_backtest.py 36
```

```bash
python3 src/analyze_backtest.py
```

Python 3 estándar, sin dependencias externas.
