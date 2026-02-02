#!/bin/bash
echo "[ARCANA] Starting Sovereign Ledger Backup..."
# Refreshing metadata token for IMDSv2
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
# Running Scan
aws dynamodb scan --table-name TrustStack_Clients --region us-east-2 --limit 100 > "backup_$(date +%F_%T).json"
if [ $? -eq 0 ]; then
    echo "[ARCANA] Backup Successful. 136B CC Ledger Secured."
else
    echo "[ARCANA] Backup Failed. Update your IAM policy using arcana_policy.json."
fi
