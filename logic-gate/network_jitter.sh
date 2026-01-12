#!/bin/bash
# Phase 3, Day 18: Network-Jitter-Generator (Traffic Masking Protocol)

# List of innocuous 3D endpoints to ping
NODES=("8.8.8.8" "1.1.1.1" "api.github.com" "www.wikipedia.org")

echo "--- INITIATING NETWORK CLOAKING ---"

while true; do
    # 1. Choose a random node
    TARGET=${NODES[$RANDOM % ${#NODES[@]}]}
    
    # 2. Generate a random "Pulse" size (encrypted noise)
    PULSE_SIZE=$((RANDOM % 1024 + 512)) # 512 - 1536 bytes
    
    # 3. Randomized interval to prevent "Rhythmic Pattern" detection
    SLEEP_TIME=$(echo "scale=2; ($RANDOM % 500) / 100" | bc -l)
    
    # 4. Send the Jitter Signal
    ping -c 1 -s $PULSE_SIZE $TARGET > /dev/null 2>&1
    
    # 5. Check if the Arcana Daemon is still alive; if not, terminate jitter
    if ! pgrep -f "arcana_daemon" > /dev/null; then
        echo "DAEMON OFFLINE. CLOAKING DISENGAGED."
        exit 0
    fi
    
    sleep $SLEEP_TIME
done
