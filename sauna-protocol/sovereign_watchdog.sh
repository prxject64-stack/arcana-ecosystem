#!/bin/bash
# Sovereign Watchdog for Arcana/Sauna Protocol

while true; do
    echo "[!] STARTING HARDHAT NODE..."
    # Start node in background and save PID
    npx hardhat node --hostname 127.0.0.1 > node.log 2>&1 &
    NODE_PID=$!
    
    # Wait for node to warm up (RPC ready)
    sleep 5
    
    echo "[!] NODE DETECTED. INJECTING SOVEREIGN STATE (146B ARC/CC)..."
    npx hardhat run scripts/direct_resurrect.js --network localhost
    
    echo "[!] STATE ANCHORED. MONITORING..."
    
    # Wait for the node process to end (crash or kill)
    wait $NODE_PID
    
    echo "[X] NODE CRASHED OR STOPPED. RESTARTING IN 3 SECONDS..."
    sleep 3
done
