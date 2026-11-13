# Sweeper de Polymarket — SOLO PAPEL

Investigación sin dinero real: ¿los resultados casi seguros de Polymarket pagan $1 más seguido de lo
que dice su precio? Ver `PLAN.md` para el plan original y las reglas duras.

- Sin cuentas, sin wallets, sin llaves, sin órdenes reales.
- Solo lectura de las APIs públicas (Gamma y CLOB).

## Estado (11 nov 2026)

1. **El primer backtest estaba sesgado.** Tomaba los mercados de mayor volumen final, y las sorpresas
   generan volumen, así que sobre-representaba favoritos que perdieron. Daba un edge de -2 a -5 puntos
   que no es real.
2. **Sin ese sesgo, la banda del plan (90-97c) está bien calibrada**: edge entre -0.7 y +0.4 puntos.
   Ahí no hay ventaja en ningún sentido.
3. **Sí hay una ventaja pequeña y consistente en favoritos de 97-99.95c cerca del cierre**, en cripto,
   deportes y "otros", y en mercados de 95-97c cuya fecha de fin ya pasó. Pasa en datos de
   entrenamiento, se confirma en datos recientes no usados para buscarla, sobrevive a la selección
   adversa y al peor caso de los mercados sin resolver.
4. **El simulador de papel corre cada hora** con esas reglas. El veredicto final sale tras 4 semanas:
   ver `data/paper/REPORT.md`.

## Backtest sin sesgo (`src/explore_universe.py`)

Muestra: 176 ventanas de 2 horas elegidas al azar en 90 días, con **todos** los mercados binarios cuya
fecha de fin cae en la ventana: resueltos de cualquier volumen (unos 330,000), anulados o pagados
50/50 (6,355) y los que siguen sin resolver (7,541). 376,265 observaciones con el favorito a 80c o más.

- Decisión con datos conocidos de antemano: horas antes o después de la fecha de fin publicada.
- Edge = pagó − precio medio visto. Error estándar agrupado por evento.
- Entrena = 2/3 de ventanas más antiguas; prueba = 1/3 más reciente.
- "Tocada": solo órdenes cuyo precio fue alcanzado después (selección adversa del maker).
- "Peor caso": todos los mercados que siguen sin resolver se cuentan como pérdida total.

Calibración general, 24h antes de la fecha de fin:

| Banda | n | Precio | Pagó | Edge | IC95 |
|---|---|---|---|---|---|
| 90-95c | 14,882 | 92.53c | 92.49% | -0.04 | -0.46 a +0.39 |
| 95-97c | 6,964 | 95.85c | 96.08% | +0.23 | -0.23 a +0.69 |
| 97-99c | 8,409 | 98.04c | 98.28% | +0.24 | -0.03 a +0.51 |
| 99-99.5c | 4,337 | 99.27c | 99.77% | +0.50 | +0.35 a +0.64 |
| 99.5-99.95c | 5,098 | 99.71c | 99.98% | +0.27 | +0.24 a +0.31 |

Reglas que usa el simulador (54 de 175 reglas evaluadas pasan todo; estas son las elegidas):

| Regla | Momento | Banda | n | Pérdidas | Edge | Edge en prueba | Edge tocada | Peor caso |
|---|---|---|---|---|---|---|---|---|
| cripto | 24h antes del fin | 97-99.95c | 1,634 | 3 | +0.67 | +0.54 | +0.46 | +0.67 |
| cripto | 6h antes del fin | 97-99.95c | 2,399 | 4 | +0.58 | +0.42 | +0.45 | +0.58 |
| deportes | 24h antes del fin | 97-99.95c | 2,336 | 12 | +0.99 | +1.21 | +0.99 | +0.52 |
| deportes | 6h antes del fin | 97-99.95c | 4,225 | 37 | +0.54 | +0.22 | +0.30 | +0.14 |
| otros | 24h antes del fin | 97-99.95c | 542 | 0 | +1.10 | +1.20 | +1.37 | +0.92 |
| otros | 6h antes del fin | 97-99.95c | 551 | 0 | +1.01 | +1.20 | +1.17 | +0.82 |
| fin ya pasó (6h) | todas | 95-97c | 563 | 4 | +3.53 | +4.17 | +2.75 | +1.96 |

"Deportes" excluye clima, tuits y marcadores exactos, que el clasificador original mezclaba y donde
la selección adversa se come el edge. Detalle completo en `data/universe_rules.csv` y
`data/universe_calibration.csv`.

### Lo que el backtest no prueba

- El precio histórico es el punto medio horario, no una orden ejecutada. Con un diferencial de
  99.5/99.9, comprar al medio exige que alguien te venda ahí; si hay que pagar 99.9 la ventaja desaparece.
- Son 90 días (ago-nov 2026). Las reglas de cripto equivalen a vender seguros contra movimientos
  bruscos: un desplome en un día puede voltear muchos mercados a la vez, y el periodo no tuvo uno grande.
- Las pérdidas son raras y grandes: una sola a 99c borra unas 100-200 ganancias.
- Riesgos de cola vistos en los datos: partidos pospuestos (todos sus mercados atascados a ~55c) y
  mercados anulados que pagan 50/50.
- Se evaluaron 175 reglas; exigir confirmación en datos de prueba reduce el riesgo de sobreajuste,
  no lo elimina. Para eso es la fase de papel.

## Simulador de papel (`src/paper.py`)

Cada hora: liquida posiciones cerradas, revisa órdenes, escanea mercados activos y coloca órdenes
límite virtuales al punto medio (nunca al ask). Estado en `data/paper/state.json`, bitácora en
`data/paper/log.jsonl`, reporte en `data/paper/REPORT.md`.

- Capital virtual $1,000. Máximo 5% por mercado, 10% por evento, 20% por categoría.
- Liquidez mínima $1,000, diferencial máximo 3c, sin disputa UMA, cierre en 45 días o menos.
- Una orden se llena solo si el precio bajó al menos 1 tick por debajo del límite después de ponerla
  **y** gana un sorteo del 30% (supuesto del plan). Vive 12 horas como máximo.
- Se detiene si la pérdida acumulada llega al 15%, y deja de abrir órdenes a las 4 semanas.
- **Registro sombra**: con $1,000 solo caben unas 11 órdenes a la vez, muy pocas para medir una
  ventaja de medio punto. Por eso además se anota cada oportunidad detectada (una vez por mercado,
  sin límite de capital) con su precio límite, si el precio llegó a tocarla y cómo pagó
  (`data/paper/shadow_closed.csv`). El edge de las "tocadas" es el número que decide el veredicto.
- Programado como tarea de Claude Code en la nube cada hora. Una sesión nueva no puede subir
  cambios a este repo, así que la tarea despierta la sesión que construyó el proyecto.

Corrida manual:

```bash
bash sweeper/run_paper.sh
```

## Reproducir el backtest

Desde `sweeper/` (las bases de datos no se versionan; bajarlas tarda unas 2 horas):

```bash
python3 src/fetch_universe.py 252
```

```bash
UDB=data/universe_low.db VMIN=0 VMAX=1000 python3 src/fetch_universe.py 90
```

```bash
python3 src/fetch_unresolved.py
```

```bash
python3 src/fetch_voided.py
```

```bash
python3 src/explore_universe.py
```

`src/bias_check.py` muestra el sesgo de volumen. `src/fetch_backtest.py`, `src/analyze_backtest.py`,
`src/verdict_backtest.py` y los CSV `backtest_*` son el primer backtest (sesgado), que se conserva
como referencia. `src/stuck_markets.py` lista mercados abiertos pasada su fecha de fin.

## Perfil agresivo (experimento de comparación)

`PROFILE=agresivo python3 src/paper.py` corre un segundo simulador con su propio capital virtual
($1,000) y sus propios registros en `data/paper_agresivo/`. El perfil base no cambia.

| | Base | Agresivo |
|---|---|---|
| Por mercado / evento / categoría | 5% / 10% / 20% | 10% / 20% / 40% |
| Banda de precio | 97-99.95c | 95-99.95c |
| Ventana antes del fin | hasta 24-30h | hasta 72h |
| Fecha de fin ya pasada | 95-97c, hasta 12h | 90-97c, hasta 24h |
| Categorías | cripto, deportes, otros | las mismas más clima |
| Precio de la orden | punto medio | 1 tick por debajo del ask |
| Llenado supuesto | 30% | 50% |
| Liquidez mínima / diferencial máximo | $1,000 / 3c | $500 / 5c |
| Paro por pérdida | 15% | 30% |

Varias reglas del agresivo no pasaron todas las pruebas del backtest (la banda 95-97c antes del fin
está bien calibrada, sin ventaja; clima sufre selección adversa) y pagar casi el ask se come el
margen. Está para comparar desempeño, no porque se espere que gane. `run_paper.sh` corre los dos y
`dashboard.html` los muestra lado a lado.

## Correr sin Claude (sin créditos)

`run_local.sh` corre los dos perfiles y regenera `dashboard.html` con solo Python 3, sin mensajes.
Para que corra cada hora, agrega con `crontab -e` (Linux/macOS):

```
0 * * * * /ruta/a/changelpina/sweeper/run_local.sh >> /ruta/a/changelpina/sweeper/data/local.log 2>&1
```

En Windows, el Programador de tareas puede llamar al mismo script con Git Bash o WSL. El panel se
abre con doble clic en `dashboard.html`. La tarea horaria en la nube de Claude está apagada.
