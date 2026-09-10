#!/bin/bash
# Eerste installatie van de schaduwbot op een verse Ubuntu-server. Draait als root.
# Wordt gestart door de user-data van Hetzner, en opnieuw door tick.sh zolang de installatie niet gelukt is.
# Vereist omgevingsvariabelen: GITHUB_REPO, GITHUB_TOKEN, HELIUS_API_KEY (bij de eerste run).

exec 9>/run/schaduwbot-bootstrap.lock
flock -n 9 || { echo "bootstrap draait al"; exit 0; }
LOG=/var/log/schaduwbot-bootstrap.log
exec >>"$LOG" 2>&1
echo "===== bootstrap start $(date -u +%FT%TZ) ====="

# --- 1. geheimen vastleggen (alleen bij eerste run; daarna uit het bestand) ---
if [ -n "${GITHUB_TOKEN:-}" ]; then
  GITHUB_REPO=${GITHUB_REPO//$'\r'/}; GITHUB_TOKEN=${GITHUB_TOKEN//$'\r'/}; HELIUS_API_KEY=${HELIUS_API_KEY//$'\r'/}
  GITHUB_REPO=${GITHUB_REPO// /}; GITHUB_TOKEN=${GITHUB_TOKEN// /}; HELIUS_API_KEY=${HELIUS_API_KEY// /}
  umask 077
  cat > /opt/schaduwbot.env <<EOF
GITHUB_REPO=${GITHUB_REPO}
GITHUB_TOKEN=${GITHUB_TOKEN}
HELIUS_API_KEY=${HELIUS_API_KEY}
HEALTH_PORT=8080
DB_PATH=/opt/schaduwbot/data/schaduwbot.sqlite
REPORT_DIR=/opt/schaduwbot/reports
EOF
  umask 022
fi
set -a; . /opt/schaduwbot.env; set +a
RAW="https://raw.githubusercontent.com/${GITHUB_REPO}/main"

# --- 2. hartslag installeren vóór alles, zodat fouten altijd gemeld en opnieuw geprobeerd worden ---
curl -fsSL "$RAW/status_push.py" -o /root/status_push.py || echo "status_push.py ophalen mislukt"
cat > /root/tick.sh <<'EOF'
#!/bin/bash
set -a; . /opt/schaduwbot.env; set +a
RAW="https://raw.githubusercontent.com/${GITHUB_REPO}/main"
curl -fsSL "$RAW/status_push.py" -o /root/status_push.py.new && mv /root/status_push.py.new /root/status_push.py
if [ -d /opt/schaduwbot/.git ] && [ -f /opt/schaduwbot/.venv/bin/python ]; then
  bash /opt/schaduwbot/update.sh >> /var/log/schaduwbot-update.log 2>&1
else
  curl -fsSL "$RAW/bootstrap.sh" -o /root/bootstrap.sh && bash /root/bootstrap.sh
fi
python3 /root/status_push.py "tick" || true
EOF
cat > /etc/systemd/system/schaduwbot-tick.service <<'EOF'
[Unit]
Description=Schaduwbot: status melden, updaten, zelfherstel
[Service]
Type=oneshot
ExecStart=/bin/bash /root/tick.sh
TimeoutStartSec=1800
EOF
cat > /etc/systemd/system/schaduwbot-tick.timer <<'EOF'
[Unit]
Description=Schaduwbot tick elke 5 minuten
[Timer]
OnBootSec=2min
OnUnitActiveSec=5min
[Install]
WantedBy=timers.target
EOF
systemctl daemon-reload
systemctl enable schaduwbot-tick.timer
systemctl start schaduwbot-tick.timer
python3 /root/status_push.py "bootstrap gestart" || true

fail() { echo "FOUT: $1"; python3 /root/status_push.py "bootstrap-fout: $1" || true; exit 1; }

# --- 3. pakketten (wacht op apt-lock van automatische updates bij eerste boot) ---
export DEBIAN_FRONTEND=noninteractive
apt-get -o DPkg::Lock::Timeout=900 update -q || fail "apt-get update"
apt-get -o DPkg::Lock::Timeout=900 install -y -q git python3-venv python3-pip curl || fail "apt-get install"

# --- 4. code ophalen ---
if [ ! -d /opt/schaduwbot/.git ]; then
  rm -rf /opt/schaduwbot
  git clone -q "https://github.com/${GITHUB_REPO}.git" /opt/schaduwbot || fail "git clone"
fi
cp /opt/schaduwbot.env /opt/schaduwbot/.env

# --- 5. installeren en starten ---
bash /opt/schaduwbot/install.sh || fail "install.sh"
sleep 30
python3 /root/status_push.py "bootstrap klaar" || true
echo "===== bootstrap klaar $(date -u +%FT%TZ) ====="
