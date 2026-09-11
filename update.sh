#!/bin/bash
# Aangeroepen door tick.sh (elke 5 minuten): nieuwe code van GitHub ophalen en de bot zo nodig herstellen.
cd /opt/schaduwbot || exit 1
echo "--- update $(date -u +%FT%TZ)"
git fetch -q origin main || { echo "git fetch mislukt"; exit 0; }
if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
  echo "nieuwe code: $(git rev-parse --short origin/main)"
  # Alleen herstarten als er iets verandert dat de bot zelf gebruikt. Wijzigingen in analyses, documentatie of
  # volg_wallets.txt vragen geen herstart (elke herstart geeft een gat in de data van lopende tokens).
  CHANGED=$(git diff --name-only HEAD origin/main)
  git reset -q --hard origin/main
  cp /opt/schaduwbot.env /opt/schaduwbot/.env 2>/dev/null || echo "waarschuwing: /opt/schaduwbot.env ontbreekt"
  if echo "$CHANGED" | grep -qvE '^(ledger\.py|video_replay\.py|wallet_analysis\.py|status_push\.py|update\.sh|test_all\.py|README\.md|volg_wallets\.txt|Fase1_.*|.*\.md)$'; then
    echo "botcode gewijzigd: herstart"; bash install.sh
  else
    echo "alleen analyses/documentatie gewijzigd: geen herstart"
  fi
elif ! systemctl is-active --quiet schaduwbot; then
  echo "bot draait niet: herstel"
  bash install.sh
fi

# Analyses (wallet-analyse, geldstroom, videostrategie): als eigen systemd-taak met lage prioriteit, elke 2 uur,
# en direct opnieuw zodra een van de scripts verandert. Ze lezen de bot-database alleen; de geldstroom en de
# videotoets schrijven naar een eigen database (data/ledger.sqlite) en rekenen alleen nieuwe trades en tokens door.
STAMP=/opt/schaduwbot/reports/.wallets_stamp
SUM=$(cat /opt/schaduwbot/wallet_analysis.py /opt/schaduwbot/ledger.py /opt/schaduwbot/video_replay.py 2>/dev/null | sha1sum | cut -c1-12)
mkdir -p /opt/schaduwbot/reports
if [ -f /opt/schaduwbot/wallet_analysis.py ] && ! systemctl is-active --quiet schaduwbot-wallets; then
  LAST_SUM=$(cat "$STAMP" 2>/dev/null)
  AGE=$(( $(date +%s) - $(stat -c %Y "$STAMP" 2>/dev/null || echo 0) ))
  if [ "$LAST_SUM" != "$SUM" ] || [ "$AGE" -gt 7200 ]; then
    systemctl reset-failed schaduwbot-wallets 2>/dev/null
    if systemd-run --unit=schaduwbot-wallets --collect -p RuntimeMaxSec=5400 /bin/bash -c \
         'cd /opt/schaduwbot && set -a && . ./.env && set +a && for s in ledger.py video_replay.py wallet_analysis.py; do [ -f "$s" ] && nice -n 19 ionice -c3 .venv/bin/python "$s" >> reports/wallets.log 2>&1; done'; then
      echo "$SUM" > "$STAMP"; echo "analyses gestart ($SUM)"
    else
      echo "analyses starten mislukt"
    fi
  fi
fi
