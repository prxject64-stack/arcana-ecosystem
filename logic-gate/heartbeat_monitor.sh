#!/bin/bash
# Phase 2, Day 19: 12D Heartbeat Monitor (Dead Man's Switch)

PULSE_FILE="~/arcana-ecosystem/.pulse_12d"
eval PULSE_PATH=$PULSE_FILE
THRESHOLD=172800 # 48 hours in seconds

echo "--- CHECKING 12D HEARTBEAT ---"

if [ ! -f "$PULSE_PATH" ]; then
    echo "First run: Generating initial pulse."
    touch "$PULSE_PATH"
    exit 0
fi

LAST_PULSE=$(stat -c %Y "$PULSE_PATH")
CURRENT_TIME=$(date +%s)
DIFF=$((CURRENT_TIME - LAST_PULSE))

if [ "$DIFF" -gt "$THRESHOLD" ]; then
    echo "CRITICAL: HEARTBEAT LOST FOR $DIFF SECONDS."
    echo "INITIATING EMERGENCY PURGE OF RAM BUFFERS..."
    rm -rf /dev/shm/*
    # Trigger the Day 12 De-Resonator for total system lockdown
    ~/arcana-ecosystem/logic-gate/emergency_deresonator.sh --panic
else
    echo "Heartbeat verified. Syncing with 12th Dimension..."
    # Update the pulse to prove presence
    touch "$PULSE_PATH"
fi
