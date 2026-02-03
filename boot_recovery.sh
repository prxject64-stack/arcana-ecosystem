#!/bin/bash
# Arcana Boot Recovery v1.0 [2026-02-02]
USER_HOME="/home/prxject64"
LOG_FILE="${USER_HOME}/boot_recovery.log"

echo "[$(date)] SYSTEM REBOOT DETECTED. INITIATING RECOVERY..." > "$LOG_FILE"

# 1. Wait for Network (AWS CLI needs internet)
sleep 30

# 2. Verify Identity
aws sts get-caller-identity >> "$LOG_FILE" 2>&1

# 3. Run Initial Health Check
${USER_HOME}/nexus_core.sh >> "$LOG_FILE" 2>&1

# 4. Trigger Immediate Backup
${USER_HOME}/backup_ledger.sh >> "$LOG_FILE" 2>&1

echo "[$(date)] RECOVERY COMPLETE. SYSTEMS ONLINE." >> "$LOG_FILE"
