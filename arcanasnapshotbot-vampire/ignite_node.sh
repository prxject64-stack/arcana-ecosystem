#!/bin/bash
# Arcana Sovereign Master Deployment & Auto-Sync - 2026 Feb 20

REPO_DIR="/root/arcana-ecosystem/arcanasnapshotbot-vampire"
SYSTEMD_DIR="/etc/systemd/system"

echo "[1/5] Synchronizing with Global Sovereign Repository..."
cd $REPO_DIR
# Stash local changes to prevent merge conflicts during auto-sync
git stash
git pull origin main
git stash pop || echo "No local stashes to apply."

echo "[2/5] Establishing Symbolic Links..."
ln -sf $REPO_DIR/arcana-bot.service $SYSTEMD_DIR/arcana-bot.service

echo "[3/5] Hardening Venv and Dependencies..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

echo "[4/5] Initializing Sovereign Firewall..."
ufw allow 22/tcp
ufw allow 11434/tcp
ufw --force enable

echo "[5/5] Starting Services..."
systemctl daemon-reload
systemctl restart arcana-bot

echo "=== LINODE G8 SOVEREIGN NODE ONLINE & SYNCED ==="
systemctl status arcana-bot --no-pager
