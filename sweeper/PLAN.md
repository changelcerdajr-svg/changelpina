# Proyecto: bot "sweeper" de Polymarket, SOLO PAPEL (sin dinero real)

Instrucciones para Claude Code: ejecuta este plan de principio a fin en un repo nuevo. Trabaja por fases, commitea al terminar cada una y no pidas confirmación entre fases, salvo en las que se marcan.

## Reglas duras
- Solo papel. No crear cuentas, no wallets, no llaves privadas, no ordenes reales. Ninguna fase de este documento requiere credenciales.
- Solo leer las APIs publicas de Polymarket: Gamma (`https://gamma-api.polymarket.com`) y CLOB (`https://clob.polymarket.com`, p. ej. `/prices-history`). No usar VPN ni evadir bloqueos geograficos.
- Limites de riesgo en la simulacion: max 5% del capital por mercado, 20% por categoria, excluir mercados con disputa UMA o resolucion ambigua, solo mercados que cierran en <=45 dias, solo ordenes limite tipo maker, parar la simulacion si la perdida acumulada llega a 15%.
- Supuesto de ejecucion realista: solo 30% de las ordenes limite se llenan.

## Idea
El "sweeper" compra resultados casi seguros (94-99 centavos) y espera cobrar $1. La pregunta que decide todo: ¿los resultados que cotizan ~96c pagan $1 mas del 96% de las veces? Si no, no hay ventaja y el plan termina.

## Fase 1. Repo y entorno
Crear repo (privado), estructura `src/`, `data/`, README. SQLite en `data/`. Python 3, sin dependencias raras.

## Fase 2. Backtest de calibracion (criterio de paso/fallo)
1. Correr `src/fetch_backtest.py` (abajo): baja ~10,000 mercados binarios resueltos de las ultimas 36 semanas (volumen >= $5,000) y el historial horario de precios de los 10 dias previos al cierre, a `data/backtest.db`. Tarda un buen rato; correrlo en segundo plano y esperar con un bucle until, no con sleeps encadenados.
2. Correr `src/analyze_backtest.py` (abajo). Compara, por categoria, banda de precio (90-95, 95-97, 97-99c) y horizonte (1h, 6h, 24h, 72h antes del cierre), el % de veces que el favorito pago $1 contra su precio medio. Ya incluye intervalo de confianza Wilson.
3. PASA si alguna categoria paga >= 1 punto por encima del precio (limite inferior del IC razonable) con >= 300 casos, ya descontando el supuesto de 30% de llenado. Si ninguna pasa, reportar y DETENERSE: el plan termina ahi.
4. Cuidado con sesgo de supervivencia: mercados que siguen abiertos pasada su fecha de fin (p. ej. 0.99 y no resuelven) cuentan como riesgo de capital inmovilizado; reportar aparte.

## Fase 3. Escaner en vivo + simulador de papel (solo si pasa Fase 2)
- Escaner cada hora: lista mercados activos con resultados en la banda ganadora, liquidez >= $1,000, cierre <= 45 dias, sin disputa UMA.
- Simulador: coloca ordenes limite virtuales con las reglas de riesgo, llenado 30%, registra todo en SQLite del repo y commitea cada corrida.
- Duracion: 4 semanas de papel antes de sacar conclusiones.
- Programarlo como tarea programada (cada hora) en Claude Code en la nube; el estado vive en el repo, cada corrida arranca en un contenedor limpio.

## Fase 4. Reporte
Panel/reporte con: operaciones simuladas, % de pago real vs. precio, P&L simulado, capital inmovilizado, peores casos. Veredicto honesto: ¿hay ventaja despues de todo?

## Fase 5. Piloto real (NO la hace Claude)
Solo si las fases anteriores salen positivas, y solo si el usuario decide, desde Mexico (en Espana Polymarket esta bloqueado desde el 26 may 2026). Lo ejecuta el usuario a mano; Claude no coloca ordenes reales.

## Estado al momento de pasar este documento
- Fase 1 hecha. Fase 2: `fetch_backtest.py` ya bajo los ~10,772 mercados y estaba descargando historiales (iba ~1,200 de 10,772). Si `data/backtest.db` no existe, ejecutar el script desde cero.
- Pendiente: analisis de Fase 2, luego Fases 3 y 4.
