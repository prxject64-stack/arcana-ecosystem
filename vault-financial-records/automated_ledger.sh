#!/bin/bash
# Phase 2, Day 7: The Automated Ledger (The Golden Record)

# 1. Sync with the Daemon's current temporal secret
ROTATING_KEY=$(date +%Y%m%d%H$(($(date +%M)/10)))
SECRET="12D_ARCANA_${ROTATING_KEY}"
DATE_STAMP=$(date "+%Y-%m-%d")

echo "--- COMPILING GOLDEN RECORD FOR $DATE_STAMP ---"

# 2. Gather all ephemeral data from the last 24 hours
GOLDEN_TEMP="/dev/shm/golden_record_$DATE_STAMP"
mkdir -p $GOLDEN_TEMP

# Capture growth engine projections and current signal counts
~/arcana-ecosystem/vault-financial-records/growth_engine.sh > $GOLDEN_TEMP/summary.txt 2>/dev/null
echo "Signals_Captured: $(ls ~/arcana-ecosystem/vault-financial-records/signal_*.gpg | wc -l)" >> $GOLDEN_TEMP/summary.txt

# 3. Create the Encrypted Archive
tar -cf - $GOLDEN_TEMP | gpg --batch --yes --passphrase "$SECRET" --symmetric --cipher-algo AES256 -o "~/arcana-ecosystem/history-vault/GOLDEN_RECORD_$DATE_STAMP.gpg"

# 4. Clean up the source signals to prevent bloat (optional, keeps only last 7 days)
find ~/arcana-ecosystem/vault-financial-records/ -name "signal_*.gpg" -mtime +7 -delete

rm -rf $GOLDEN_TEMP
echo "SUCCESS: Golden Record for $DATE_STAMP sealed in History Vault."
