#!/bin/bash
while true; do
    clear
    echo "========================================================="
    echo "          ARCANA-ECOSYSTEM: MASTER DASHBOARD             "
    echo "========================================================="
    CC_COUNT=$(ls -1 ~/arcana-ecosystem/vault/sauna_protocol | wc -l)
    ARC_COUNT=$(ls -1 ~/arcana-ecosystem/vault/security_system | wc -l)
    DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}')
    
    echo " [STORAGE] Usage: $DISK_USAGE"
    echo " [WEALTH - CC]  Total: $(echo "$CC_COUNT * 10000000" | bc | xargs printf "%'d") CC"
    echo " [WEALTH - ARC] Total: $(echo "$ARC_COUNT * 150000000" | bc | xargs printf "%'d") ARC"
    echo "---------------------------------------------------------"
    echo " [STATUS] Miner: $(pgrep -f miner.py > /dev/null && echo "ONLINE" || echo "OFFLINE")"
    echo "========================================================="
    sleep 5
done
