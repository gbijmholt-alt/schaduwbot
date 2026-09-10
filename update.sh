#!/bin/bash
# Aangeroepen door tick.sh (elke 5 minuten): nieuwe code van GitHub ophalen en de bot zo nodig herstellen.
cd /opt/schaduwbot || exit 1
echo "--- update $(date -u +%FT%TZ)"
git fetch -q origin main || { echo "git fetch mislukt"; exit 0; }
if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
  echo "nieuwe code: $(git rev-parse --short origin/main)"
  git reset -q --hard origin/main
  cp /opt/schaduwbot.env /opt/schaduwbot/.env 2>/dev/null || echo "waarschuwing: /opt/schaduwbot.env ontbreekt"
  bash install.sh
elif ! systemctl is-active --quiet schaduwbot; then
  echo "bot draait niet: herstel"
  bash install.sh
fi
