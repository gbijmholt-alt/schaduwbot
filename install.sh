#!/bin/bash
# Installeert of werkt de bot bij vanuit /opt/schaduwbot en (her)start de service. Idempotent.
set -e
cd /opt/schaduwbot
[ -x .venv/bin/python ] || python3 -m venv .venv
.venv/bin/pip install -q --upgrade pip
.venv/bin/pip install -q -r requirements.txt
mkdir -p data reports
cp schaduwbot.service /etc/systemd/system/schaduwbot.service
systemctl daemon-reload
systemctl enable schaduwbot
systemctl restart schaduwbot
echo "install klaar"
