#!/bin/bash
# ARCANA SOVEREIGN PANIC BUTTON - 2026 FEB 20

echo "!!! EMERGENCY LOCKDOWN INITIATED !!!"

# 1. Kill the Bot Service
systemctl stop arcana-bot
pkill -f vampire_scout.py

# 2. Lockdown Firewall (Deny All except SSH)
ufw reset
ufw default deny incoming
ufw allow 22/tcp
ufw --force enable

# 3. Archive Logs for Forensics
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
tail -n 1000 /var/log/arcana-bot.log > PANIC_AUDIT_$TIMESTAMP.log

echo "SYSTEM SECURED. Bot stopped. Firewall hardened. Logs archived."
