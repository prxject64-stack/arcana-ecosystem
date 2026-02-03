#!/bin/bash
echo "--- ARCANA ECOSYSTEM: PRIME DAY STRESS TEST ---"
echo "Target Load: 4,500 TPS | Duration: 60 Minutes"
echo "Vault Principal: 136B CC | Status: MONITORING"
echo "-----------------------------------------------"

# Start the simulation engine in 'Aggressive' mode
# Redirecting to log for the Fee Collector to scrape later
sim-engine --iterations 5T --tps 4500 --duration 3600 --mode hyper-growth >> /var/log/miner_gate.log 2>&1 &

echo "Hyper-Growth simulation started in background."
echo "PID: $!"
echo "Check /var/log/miner_gate.log for real-time throughput."
