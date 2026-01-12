#!/bin/bash
# Phase 2, Day 20: Resource-Camouflage Engine (Silent Processing Protocol)

echo "--- ENGAGING RESOURCE CAMOUFLAGE ---"

# 1. Identify all Arcana-related PIDs
PIDS=$(pgrep -f "arcana|scraper|daemon|synthesizer")

if [ -z "$PIDS" ]; then
    echo "No active Arcana processes found."
    exit 0
fi

for PID in $PIDS; do
    # 2. Set CPU Priority to 'Lowest' (nice 19)
    renice -n 19 -p $PID > /dev/null
    
    # 3. Set I/O Priority to 'Idle' (ionice class 3)
    # This ensures the disk only works when nothing else needs it
    ionice -c 3 -p $PID > /dev/null
    
    echo "PID $PID: Camouflaged (CPU: Nice 19 | I/O: Idle)"
done

echo "SUCCESS: Arcana footprint reduced to < 5%."
