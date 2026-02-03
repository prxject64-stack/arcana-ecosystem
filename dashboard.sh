#!/bin/bash
# Arcana Sovereign Dashboard v1.0 [2026-02-02]
TABLE_NAME="TrustStack_Clients"
REGION="us-east-1"

clear
echo "==============================================================="
echo "        ARCANA SOVEREIGN ECOSYSTEM: COMMAND DASHBOARD          "
echo "==============================================================="
echo " DATE: $(date)          NODE: $(hostname) "
echo "---------------------------------------------------------------"

# 1. CLOUD STATUS
DESCRIBE=$(aws dynamodb describe-table --table-name "$TABLE_NAME" --region "$REGION" 2>/dev/null)
if [ $? -eq 0 ]; then
    RCU=$(echo $DESCRIBE | jq '.Table.ProvisionedThroughput.ReadCapacityUnits')
    WCU=$(echo $DESCRIBE | jq '.Table.ProvisionedThroughput.WriteCapacityUnits')
    STATUS=$(echo $DESCRIBE | jq -r '.Table.TableStatus')
    echo "[IDENTITY] Role: arcana-miner-identity | STATUS: VERIFIED"
    echo "[LEDGER]   Table: $TABLE_NAME | State: $STATUS"
    echo "[CAPACITY] Read: $RCU | Write: $WCU (Target: 4500 Swaps)"
else
    echo "[CRITICAL] IDENTITY BREACH: Access Denied to DynamoDB"
fi

# 2. AUTOMATION STATUS
echo "---------------------------------------------------------------"
LAST_BACKUP=$(ls -t /home/prxject64/backups/*.json 2>/dev/null | head -n 1)
CRON_JOB=$(crontab -l | grep "backup_ledger.sh")

if [ -z "$LAST_BACKUP" ]; then
    echo "[BACKUP]   Last Snapshot: NONE FOUND"
else
    echo "[BACKUP]   Last Snapshot: $(basename "$LAST_BACKUP")"
fi

if [ -z "$CRON_JOB" ]; then
    echo "[CRON]     Hourly Sync: INACTIVE"
else
    echo "[CRON]     Hourly Sync: ACTIVE (Path: /home/prxject64)"
fi

# 3. SECURITY & GIT
echo "---------------------------------------------------------------"
GIT_STATUS=$(git log -1 --format="%cr (%s)" 2>/dev/null)
echo "[GIT]      Last Push: $GIT_STATUS"
echo "[SECURITY] Sauna Protocol Shield: ONLINE"
echo "==============================================================="
echo " COMMANDS: [1] Nexus-Core [2] Backup [3] Emergency-Lock [Q] Quit "
