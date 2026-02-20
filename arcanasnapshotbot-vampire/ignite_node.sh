#!/bin/bash
# Arcana Sovereign Master Deployment - 2026 Feb 20

REPO_DIR="/root/arcana-ecosystem/arcanasnapshotbot-vampire"
SYSTEMD_DIR="/etc/systemd/system"

echo "[1/4] Establishing Symbolic Links..."
# Force create symlink for the bot service
ln -sf $REPO_DIR/arcana-bot.service $SYSTEMD_DIR/arcana-bot.service

echo "[2/4] Hardening Venv and Dependencies..."
cd $REPO_DIR
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

echo "[3/4] Initializing Sovereign Firewall..."
ufw allow 22/tcp
ufw allow 11434/tcp
ufw --force enable

echo "[4/4] Starting Services..."
systemctl daemon-reload
systemctl restart arcana-bot

echo "=== LINODE G8 SOVEREIGN NODE ONLINE ==="
systemctl status arcana-bot --no-pager
