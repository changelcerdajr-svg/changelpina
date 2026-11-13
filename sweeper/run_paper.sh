#!/usr/bin/env bash
# Una corrida del simulador de papel: actualiza la rama, corre, commitea y sube el estado.
# Uso: bash sweeper/run_paper.sh   (desde la raiz del repo o desde sweeper/)
set -euo pipefail
BRANCH="claude/new-session-4d5sbn"
cd "$(dirname "$0")"
git fetch -q origin "$BRANCH"
git checkout -q -B "$BRANCH" "origin/$BRANCH"
python3 src/paper.py | tee /tmp/paper_run.txt
python3 src/dashboard.py >/dev/null
git add data/paper dashboard.html
if git diff --cached --quiet; then echo "sin cambios"; exit 0; fi
git -c user.name="sweeper-paper" -c user.email="noreply@anthropic.com" commit -qm "papel: $(tail -1 /tmp/paper_run.txt | cut -c1-120)"
for i in 1 2 3 4; do
  if git push -q -u origin "$BRANCH"; then echo "estado subido"; exit 0; fi
  sleep $((2**i)); git pull -q --rebase origin "$BRANCH" || true
done
echo "ERROR: no se pudo subir el estado"; exit 1
