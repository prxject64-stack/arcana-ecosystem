#!/bin/bash
# Arcana Sovereign Auditor v1.0 [2026-02-02]
TABLE_NAME="TrustStack_Clients"
REGION="us-east-1"
USER_HOME="/home/prxject64"
LATEST_BACKUP=$(ls -t ${USER_HOME}/backups/*.json 2>/dev/null | head -n 1)

echo "==============================================="
echo "      ARCANA AUDITOR: LEDGER VERIFICATION      "
echo "==============================================="

if [ -z "$LATEST_BACKUP" ]; then
    echo "[ERROR] No local snapshots found. Run backup_ledger.sh first."
    exit 1
fi

echo "[AUDIT] Local Snapshot: $(basename "$LATEST_BACKUP")"

# 1. Fetch Live Count
LIVE_COUNT=$(aws dynamodb describe-table --table-name "$TABLE_NAME" --region "$REGION" | jq '.Table.ItemCount')
# 2. Fetch Snapshot Count
SNAP_COUNT=$(jq '.Items | length' "$LATEST_BACKUP")

echo "[STATS] Live Entries: $LIVE_COUNT | Snapshot Entries: $SNAP_COUNT"

# 3. Drift Analysis
if [ "$LIVE_COUNT" -eq "$SNAP_COUNT" ]; then
    echo "[RESULT] PASS: Ledger Integrity 100%. No Drift Detected."
else
    DIFF=$((LIVE_COUNT - SNAP_COUNT))
    echo "[RESULT] FAIL: Drift Detected! Difference: $DIFF entries."
    echo "[ACTION] Run backup_ledger.sh to sync the Sovereign State."
fi
echo "==============================================="
