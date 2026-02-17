#!/bin/bash
# Arcana Sovereign State Pruner
echo "Starting 24-hour maintenance cycle..."

# 1. Graceful Shutdown
geth --exec "miner.stop()" attach http://127.0.0.1:8545
sleep 10

# 2. Run Pruning
# This removes old trie nodes while keeping the 136B CC ledger intact
geth --datadir ~/arcana-ecosystem/data snapshot prune-state

# 3. Restart Miner on R7i.xlarge (8 threads optimized)
geth --datadir ~/arcana-ecosystem/data --networkid 136 --miner.threads 8 --api "eth,net,web3,miner,admin" --http &
echo "Maintenance complete. 136B CC Ecosystem online."
