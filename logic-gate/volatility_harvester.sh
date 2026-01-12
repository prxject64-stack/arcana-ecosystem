#!/bin/bash
# Phase 4, Day 9: Volatility-Harvester (Risk-Mitigation & Re-Entry)

echo "--- MONITORING VOLATILITY RESONANCE ---"

# 1. Calculate 3D Volatility Index
# Fetches standard deviation of price from the Execution Price log
VOLATILITY=$(cat /dev/shm/resonance_sentiment 2>/dev/null | awk '{print ($1 < 0 ? -$1 : $1)}')

# 2. Threshold Check (12D Safety Margin)
# If volatility is > 8, the environment is too unstable for passive yield
if [ "$VOLATILITY" -gt 8 ]; then
    echo "WARNING: High 3D Volatility Detected ($VOLATILITY)."
    echo "ACTION: Pulling assets from Yield-Bridge to Secure-Vault."
    
    # Update state for the Yield-Optimizer to pause
    echo "STABLE" > /dev/shm/active_yield_protocol
    echo "0" > /dev/shm/current_apr
    echo "STATUS: ASSETS PROTECTED."
else
    echo "STABLE RESONANCE ($VOLATILITY). Yield-Bridge is optimal."
    # If we were in Stable mode, trigger Re-Entry
    if [ "$(cat /dev/shm/active_yield_protocol)" == "STABLE" ]; then
        echo "RE-ENTRY: Market stabilized. Re-deploying for maximum frequency."
        ~/arcana-ecosystem/logic-gate/yield_optimizer.sh
    fi
fi
