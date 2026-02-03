#!/bin/bash
# Arcana Sovereign Ledger Backup v3.0 [Automated Git Sync - 2026-02-02]
TABLE_NAME="TrustStack_Clients"
REGION="us-east-1"
USER_HOME="/home/prxject64"
BACKUP_FILE="${USER_HOME}/cc_private_ledger_$(date +%F_%H-%M).json"

echo "[ARCANA] Starting Sovereign Audit..."

# 1. Verify Cloud Permissions
aws dynamodb scan --table-name "$TABLE_NAME" --region "$REGION" --limit 1 --select "COUNT" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "[SUCCESS] Permissions Verified. Scanning Ledger..."
    aws dynamodb scan --table-name "$TABLE_NAME" --region "$REGION" > "$BACKUP_FILE"
    
    # 2. Synchronize with GitHub
    cd "$USER_HOME"
    git add "$BACKUP_FILE"
    git commit -m "Auto-Snapshot: CC Private Ledger $(date +%F_%H-%M)"
    git push origin main --force
    
    echo "[ARCANA] Ledger Secured and Pushed to Remote."
else
    echo "[CRITICAL] AccessDenied. Scan Failed. Check IAM Browser Console."
    exit 1
fi
