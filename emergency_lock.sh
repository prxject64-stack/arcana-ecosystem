#!/bin/bash
# Arcana Emergency Kill-Switch v1.0 [Sovereign Lockdown - 2026-02-02]
TABLE_NAME="TrustStack_Clients"
REGION="us-east-1"

echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "   CRITICAL: INITIATING EMERGENCY LOCKDOWN     "
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

# 1. Force Capacity to Minimum (1 RCU / 1 WCU)
# This effectively throttles all 4500 swaps to 0, stopping the drain.
aws dynamodb update-table \
    --table-name "$TABLE_NAME" \
    --region "$REGION" \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "[LOCKED] Throughput throttled to 1. Transaction flow halted."
else
    echo "[FAILED] Lockdown signal rejected. Check IAM Master Key."
    exit 1
fi

# 2. Final Snapshot (Capture the scene of the breach)
echo "[ARCANA] Capturing Forensic Snapshot..."
aws dynamodb scan --table-name "$TABLE_NAME" --region "$REGION" > "FORENSIC_SNAPSHOT_$(date +%s).json"

# 3. Security Broadcast
echo "[SECURITY] Sauna Protocol: VAULT SEALED."
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
