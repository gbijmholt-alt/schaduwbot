#!/bin/bash
# Elke 5 minuten: (1) rapporten + heartbeat naar GitHub-branch 'status', (2) nieuwe code ophalen, (3) herstart bij wijziging.
cd /opt/schaduwbot || exit 1
REMOTE_URL="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git"

# --- 1. status terugsturen via aparte checkout op branch 'status' ---
S=/opt/schaduwbot-status
if [ ! -d "$S/.git" ]; then
  git clone -q -b status "$REMOTE_URL" "$S" 2>/dev/null || { git init -q "$S"; (cd "$S" && git checkout -q --orphan status && git remote add origin "$REMOTE_URL"); }
  (cd "$S" && git config user.email "bot@schaduwbot" && git config user.name "schaduwbot")
fi
curl -s -m 5 http://127.0.0.1:8080/health > "$S/health.json" || echo '{"ok":false,"note":"health onbereikbaar"}' > "$S/health.json"
cp -f reports/latest.md "$S/latest.md" 2>/dev/null || true
cp -f reports/*.json "$S/" 2>/dev/null || true
journalctl -u schaduwbot -n 200 --no-pager > "$S/log-tail.txt" 2>/dev/null || true
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$S/heartbeat.txt"
(cd "$S" && git add -A && git commit -q -m "status $(cat heartbeat.txt)" >/dev/null 2>&1; git push -q origin status >/dev/null 2>&1) || true

# --- 2./3. code bijwerken ---
git fetch -q origin main || exit 0
if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
  git reset -q --hard origin/main
  bash install.sh
  systemctl restart schaduwbot
fi
