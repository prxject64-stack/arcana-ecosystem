#!/bin/bash

# Path to the miner
MINER_PATH="/home/ubuntu/arcana-ecosystem/mining-core/aws_miner_v2.py"
LOG_FILE="/home/ubuntu/arcana-ecosystem/mining-core/miner.log"

while true; do
    # Check if the python process is running
    if ! pgrep -f "python3 $MINER_PATH" > /dev/null; then
        echo "$(date): Miner down. Restarting..." >> watchdog.log
        nohup python3 $MINER_PATH > /dev/null 2>&1 &
    fi
    sleep 30
done
