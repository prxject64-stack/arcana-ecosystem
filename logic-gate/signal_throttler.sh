#!/bin/bash
# Phase 2, Day 24: Signal-Throttler (Volatility Control Protocol)

LAST_WRITE_FILE="/dev/shm/last_signal_write"
MIN_GAP=10 # Minimum seconds between writes

echo "--- CHECKING SIGNAL DENSITY ---"

# 1. Initialize if first run
if [ ! -f "$LAST_WRITE_FILE" ]; then
    echo "$(date +%s)" > "$LAST_WRITE_FILE"
    echo "1" > /dev/shm/throttle_state
    exit 0
fi

LAST_TIME=$(cat "$LAST_WRITE_FILE")
CURRENT_TIME=$(date +%s)
ELAPSED=$((CURRENT_TIME - LAST_TIME))

# 2. Evaluate Density
if [ "$ELAPSED" -lt "$MIN_GAP" ]; then
    echo "THROTTLE ACTIVE: Signal density too high ($ELAPSED s). Skipping write."
    echo "0" > /dev/shm/throttle_state
else
    echo "THROTTLE PASS: Signal density optimal. Updating last write time."
    echo "$CURRENT_TIME" > "$LAST_WRITE_FILE"
    echo "1" > /dev/shm/throttle_state
fi
