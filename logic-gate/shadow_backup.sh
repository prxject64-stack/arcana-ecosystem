#!/bin/bash
# Day 14: The Shadow Backup Logic
# Fail-safe for IDrive 5TB Sync

TIMESTAMP=$(date +%Y-%m-%d_%H-%M)
SHADOW_VAULT=~/arcana-ecosystem/shadow-vault
mkdir -p $SHADOW_VAULT

echo "Initiating Primary IDrive Heartbeat..."
# Attempting the primary cloud sync
idriveit --upload ~/arcana-ecosystem/core-assets/

if [ $? -eq 0 ]; then
    echo "SUCCESS: Primary Sync achieved. The 12D signal is stable."
else
    echo "CRITICAL: Primary Sync failed. Activating Day 14 Shadow Protocol..."
    
    # Create a local compressed & encrypted shadow clone
    tar -czf - ~/arcana-ecosystem/core-assets/ | gpg --batch --yes --symmetric --cipher-algo AES256 --passphrase "12thDimensionSuccess" --output $SHADOW_VAULT/shadow_backup_$TIMESTAMP.tar.gz.gpg
    
    echo "SHADOW ALERT: Local backup anchored at $SHADOW_VAULT/shadow_backup_$TIMESTAMP.tar.gz.gpg"
    echo "$(date): SHADOW BACKUP TRIGGERED" >> ~/arcana-ecosystem/history-vault/transmission_log.md
fi
