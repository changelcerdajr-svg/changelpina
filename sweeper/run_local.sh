#!/usr/bin/env bash
# Corrida local del simulador de papel, SIN Claude: no gasta creditos ni manda mensajes.
# Corre los dos perfiles (base y agresivo) y regenera dashboard.html. Solo necesita python3.
#
# Para correrlo cada hora (Linux/macOS), agrega esta linea con `crontab -e`:
#   0 * * * * /ruta/a/changelpina/sweeper/run_local.sh >> /ruta/a/changelpina/sweeper/data/local.log 2>&1
set -euo pipefail
export PYTHONUTF8=1   # evita errores de codificacion en Windows (cp1252)
cd "$(dirname "$0")"
# Si el repo esta limpio, trae el ultimo estado; si tienes cambios locales, sigue sin tocarlos.
if git diff --quiet 2>/dev/null && git diff --cached --quiet 2>/dev/null; then
  git pull -q --ff-only 2>/dev/null || true
fi
echo "== $(date -u +%FT%TZ) =="
python3 src/paper.py
PROFILE=agresivo python3 src/paper.py
python3 src/dashboard.py
echo "Listo. Abre sweeper/dashboard.html"
