#!/bin/bash
# Phase 2, Day 8: The Resonance Multiplier (Dynamic Frequency Tuning)

LOG_FILE="~/arcana-ecosystem/history-vault/daemon_heartbeat.log"
eval LOG_FILE_PATH=$LOG_FILE

echo "--- CALCULATING RESONANCE PEAKS ---"

# 1. Analyze the last 24 hours of heartbeats to find frequency density
# In 12D logic, high activity in the log correlates to high resonance
PEAK_HOUR=$(grep "Protocol Cycle Complete" "$LOG_FILE_PATH" | cut -d' ' -f2 | cut -d':' -f1 | uniq -c | sort -nr | head -n 1 | awk '{print $2}')

CURRENT_HOUR=$(date +%H)

# 2. Adjust the multiplier
if [ "$CURRENT_HOUR" == "$PEAK_HOUR" ]; then
    echo "PEAK RESONANCE DETECTED. Multiplier: 3x (Sleep 200s)"
    echo "200" > /dev/shm/arcana_sleep_timer
else
    echo "Standard Resonance. Multiplier: 1x (Sleep 600s)"
    echo "600" > /dev/shm/arcana_sleep_timer
fi
