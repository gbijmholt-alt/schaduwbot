#!/bin/bash
# Installeert of update de bot vanuit /opt/schaduwbot. Idempotent.
set -e
cd /opt/schaduwbot
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install -q -r requirements.txt
mkdir -p data reports status
git config user.email "bot@schaduwbot"
git config user.name "schaduwbot"
cp schaduwbot.service /etc/systemd/system/
cp schaduwbot-update.service schaduwbot-update.timer /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now schaduwbot schaduwbot-update.timer
echo "install klaar"
