#!/bin/bash
# 12D Sentry v2: Visual Notification Protocol

# 1. Search for 'Success' in the latest IDrive logs
LOG_RESULT=$(/opt/IDriveForLinux/bin/idrive --view-log | grep -i "Success" | tail -n 1)

if [[ -z "$LOG_RESULT" ]]; then
    # Visual Alert for Failure
    notify-send "12D ALERT" "Heartbeat not detected. Check alignment." --icon=error
    echo "$(date): ALERT - Backup failed or did not run." >> ~/arcana-ecosystem/idrive_scripts/infrastructure.md
else
    # Visual Confirmation for Success
    notify-send "12D SUCCESS" "Heartbeat confirmed: $LOG_RESULT" --icon=emblem-success
    echo "$(date): SUCCESS - 12D Heartbeat confirmed." >> ~/arcana-ecosystem/idrive_scripts/infrastructure.md
fi
