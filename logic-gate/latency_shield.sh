#!/bin/bash
# Phase 2, Day 26: Neural-Latency Shield (Adaptive Obfuscation Protocol)

TARGET=$(cat /dev/shm/active_frequency 2>/dev/null || echo "api.coingecko.com")

echo "--- MEASURING NEURAL LATENCY ---"

# 1. Measure RTT (Round Trip Time) to the active 3D node
RTT=$(ping -c 1 "$TARGET" | grep 'time=' | sed 's/.*time=\([0-9.]*\).*/\1/')

if [ -z "$RTT" ]; then RTT=100; fi # Default if ping is blocked

echo "3D Latency: ${RTT}ms"

# 2. Calculate "Neural Jitter" (Randomized sleep between 0.5x and 1.5x of Latency)
# This prevents the 3D server from seeing a fixed pattern.
JITTER=$(echo "scale=3; ($RTT * ((500 + $RANDOM % 1000) / 1000)) / 1000" | bc -l)

echo "Injecting ${JITTER}s Neural Jitter into the stream..."
sleep "$JITTER"

# 3. Defensive Shift: If RTT > 250ms, the node is "Heavy". Slow down further.
if (( $(echo "$RTT > 250" | bc -l) )); then
    echo "HEAVY SCANNING DETECTED. Expanding Shield."
    sleep 2
fi
