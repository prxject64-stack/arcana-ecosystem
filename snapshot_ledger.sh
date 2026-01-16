#!/bin/bash
# Arcana Sovereign Snapshot Logic
DATE=$(date +%Y-%m-%d_%H%M%S)
SOURCE="/home/ubuntu/arcana-ecosystem/ledger.json"
DEST="/home/ubuntu/arcana-ecosystem/snapshots/ledger_snapshot_$DATE.json"

# Create Snapshot
cp -p "$SOURCE" "$DEST"

# Retention: Delete snapshots older than 14 days
find /home/ubuntu/arcana-ecosystem/snapshots/ -name "ledger_snapshot_*.json" -mtime +14 -exec rm {} \;

echo "[$(date)] Sovereign Snapshot Created: $DEST" >> /home/ubuntu/arcana-ecosystem/snapshots/snapshot_log.txt
