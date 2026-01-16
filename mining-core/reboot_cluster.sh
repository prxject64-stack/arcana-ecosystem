#!/bin/bash

WORKERS_FILE="workers.txt"
MINER_PATH="/home/ubuntu/arcana-ecosystem/mining-core/aws_miner_v2.py"

echo "----------------------------------------------------"
echo "   ARCANA ECOSYSTEM: CLUSTER REFRESH INITIATED      "
echo "----------------------------------------------------"

while IFS= read -r worker_ip; do
    echo "Refreshing Node [$worker_ip]..."
    
    # Remote Command Sequence:
    # 1. Kill the current miner and watchdog
    # 2. Pull the latest code from GitHub
    # 3. Restart the watchdog (which will restart the miner)
    ssh -o StrictHostKeyChecking=no ubuntu@$worker_ip "
        pkill -f watchdog.sh; 
        pkill -f aws_miner_v2.py; 
        cd ~/arcana-ecosystem && git pull origin main;
        nohup ~/arcana-ecosystem/mining-core/watchdog.sh > /dev/null 2>&1 &
    "
    
    echo "Node [$worker_ip] is now UPDATED and ONLINE."
done < "$WORKERS_FILE"

echo "----------------------------------------------------"
echo "   GLOBAL CLUSTER REFRESH COMPLETE                  "
echo "----------------------------------------------------"
