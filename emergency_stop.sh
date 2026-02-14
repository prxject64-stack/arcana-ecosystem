#!/bin/bash
# ARCANA SOVEREIGN: EMERGENCY SCORCHED EARTH
echo "$(date): [CRITICAL] EMERGENCY STOP TRIGGERED." >> /home/prxject64/logs/guardian.log

# 1. Kill all mining and monitoring processes
pkill -f miner.py
pkill -f guardian.sh

# 2. Disable the Guardian Cron job to prevent auto-restart
crontab -r

# 3. Disable the AWS Lambda (Setting concurrency to 0 effectively kills the API)
aws lambda put-function-concurrency --function-name TrustStack-Billing-Automator --reserved-concurrent-executions 0

echo "SYSTEM FROZEN. 4,500 SWAP SLOTS DEACTIVATED."
