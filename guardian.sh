#!/bin/bash
# TRUSTSTACK SOVEREIGN GUARDIAN + INTEGRITY CHECKER
PROJECT_DIR="/home/prxject64"
MANIFEST="$(ls -t $PROJECT_DIR/SECURITY_MANIFEST_*.txt | head -1)"
LOG_FILE="$PROJECT_DIR/logs/guardian.log"

# 1. Check Process Status
if ! pgrep -f "miner.py" > /dev/null; then
    echo "$(date): [CRITICAL] Miner OFFLINE. Restarting..." >> "$LOG_FILE"
    nohup python3 $PROJECT_DIR/miner.py >> $PROJECT_DIR/logs/miner_output.log 2>&1 &
fi

# 2. Check Integrity (SHA-256)
# Get the expected hash from the manifest and the current hash
EXPECTED_HASH=$(grep "miner.py" "$MANIFEST" | awk '{print $1}')
CURRENT_HASH=$(sha256sum $PROJECT_DIR/miner.py | awk '{print $1}')

if [ "$EXPECTED_HASH" != "$CURRENT_HASH" ]; then
    echo "$(date): [SECURITY ALERT] miner.py HASH MISMATCH! Expected: $EXPECTED_HASH Got: $CURRENT_HASH" >> "$LOG_FILE"
    # Optional: Kill the miner if it's been tampered with
    pkill -f "miner.py"
fi
