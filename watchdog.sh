#!/bin/bash
# CONFIGURATION
MINER_CMD="python3 -u ~/miner.py"
LIMITER_CMD="cpulimit -l 85"
WALLET_FILE="$HOME/blockchain.enc"
LOG_FILE="$HOME/watchdog.log"

echo "[$(date)] Sentry Active. Monitoring Shadow Velocity..." >> $LOG_FILE

while true; do
    # A. Check if Miner is running
    if ! pgrep -f "$MINER_CMD" > /dev/null; then
        echo "[!] Miner down. Restarting..." >> $LOG_FILE
        nohup $LIMITER_CMD -- $MINER_CMD > ~/miner.log 2>&1 &
    fi

    # B. Check if CPULimit is active (if miner is running)
    if pgrep -f "$MINER_CMD" > /dev/null && ! pgrep -f "cpulimit -l 85" > /dev/null; then
        echo "[!] CPU Limit missing. Re-applying..." >> $LOG_FILE
        # Find miner PID and limit it
        MPID=$(pgrep -f "$MINER_CMD")
        nohup cpulimit -p $MPID -l 85 > /dev/null 2>&1 &
    fi

    # C. Stall Protection (Is the file actually growing?)
    SIZE1=$(stat -c%s "$WALLET_FILE" 2>/dev/null || echo 0)
    sleep 60
    SIZE2=$(stat -c%s "$WALLET_FILE" 2>/dev/null || echo 0)

    if [ "$SIZE1" -eq "$SIZE2" ] && [ "$SIZE1" -gt 0 ]; then
        echo "[!] Stale File detected. Force Restarting..." >> $LOG_FILE
        pkill -f miner.py
    fi
done
