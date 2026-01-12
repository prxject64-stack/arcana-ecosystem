#!/bin/bash
# Phase 2, Day 23: Data-Validator (Cross-Reference Protocol)

# 1. Fetch from Primary (Current Frequency)
PRIMARY_URL=$(cat /dev/shm/active_frequency)
PRIMARY_DATA=$(curl -s "https://$PRIMARY_URL/v3/simple/price?ids=bitcoin&vs_currencies=usd" | grep -oP '\d+\.\d+')

# 2. Fetch from Secondary (Shadow Frequency)
SECONDARY_URL="api.binance.com" # Hardcoded secondary for verification
SECONDARY_DATA=$(curl -s "https://$SECONDARY_URL/api/v3/ticker/price?symbol=BTCUSDT" | grep -oP '\d+\.\d+' | head -n 1)

echo "--- CROSS-REFERENCING SIGNALS ---"
echo "Primary ($PRIMARY_URL): $PRIMARY_DATA"
echo "Secondary ($SECONDARY_URL): $SECONDARY_DATA"

# 3. Calculate Variance (Threshold 1%)
# Logic: If |P - S| / P > 0.01, reject.
# Simplified for Bash: check if difference is within a safe margin.
DIFF=$(echo "$PRIMARY_DATA - $SECONDARY_DATA" | bc -l | sed 's/-//')
THRESHOLD=$(echo "$PRIMARY_DATA * 0.01" | bc -l)

if (( $(echo "$DIFF < $THRESHOLD" | bc -l) )); then
    echo "VALIDATION SUCCESS: Signals aligned."
    echo "1" > /dev/shm/validation_state
else
    echo "VALIDATION FAILED: High variance detected. Signal discarded."
    echo "0" > /dev/shm/validation_state
fi
