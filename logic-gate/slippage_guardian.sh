#!/bin/bash
# Phase 3, Day 6: Slippage-Guardian (Flash-Crash Protection)

THRESHOLD="0.001" # 0.1% tolerance

echo "--- ENGAGING SLIPPAGE GUARDIAN ---"

# 1. Get the Signed Price (from the Anti-Arbitrage Engine/Signer)
TARGET_PRICE=$(cat /dev/shm/execution_price 2>/dev/null)

if [ -z "$TARGET_PRICE" ]; then
    echo "ERROR: No target price found. Aborting for safety."
    echo "0" > /dev/shm/execution_gate
    exit 1
fi

# 2. Fetch the "Now" Price (The Reality Check)
# We pull the freshest data possible from the 12D redundant sensors
REALITY_PRICE=$(cat /dev/shm/current_price 2>/dev/null || echo "$TARGET_PRICE")

# 3. Calculate Variance
# Logic: (Target - Reality) / Target
VARIANCE=$(echo "scale=5; ($TARGET_PRICE - $REALITY_PRICE) / $TARGET_PRICE" | bc -l)

echo "Target: $TARGET_PRICE | Reality: $REALITY_PRICE | Variance: $VARIANCE"

# 4. The Decision Gate
if (( $(echo "$VARIANCE > $THRESHOLD" | bc -l) )); then
    echo "CRITICAL: Slippage detected ($VARIANCE). ABORTING TRANSACTION."
    echo "0" > /dev/shm/execution_gate
else
    echo "STABLE: Slippage within limits. Proceeding to 12D-3D bridge."
    echo "1" > /dev/shm/execution_gate
fi
