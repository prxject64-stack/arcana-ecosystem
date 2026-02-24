#!/bin/bash
echo "[!] Starting Arcana Node Maintenance..."
# 1. Clear dead logs
rm -rf ~/arcana-ecosystem/arcana_data/logs/*
rm -f ~/arcana-ecosystem/*.log

# 2. Prune State (Reclaims ~30-50% disk space)
# Target: 136B CC-P liquidity node state
geth snapshot prune-state --datadir ~/arcana-ecosystem/arcana_data

# 3. Secure Git Index
git rm -r --cached ~/arcana-ecosystem/arcana_data/geth/ 2>/dev/null
echo "arcana_data/" >> .gitignore

echo "[+] Maintenance Complete. ARC-S/CC-P state optimized."
