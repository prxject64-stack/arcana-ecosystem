#!/bin/bash
# Phase 3, Day 10: Multi-Network-Relay (Omnipresence Protocol)

# Define the 3D Network Array
NETWORKS=("ETH_MAINNET" "SOLANA_MAIN" "POLYGON_L2" "BITCOIN_CORE")
RPC_ENDPOINTS=(
    "https://mainnet.infura.io/v3/PROJECT_ID"
    "https://api.mainnet-beta.solana.com"
    "https://polygon-rpc.com"
    "https://blockstream.info/api"
)

echo "--- SCANNING NETWORK RELAYS ---"

# 1. Find the path of least resistance (Lowest Latency)
BEST_LATENCY=9999
SELECTED_NET=""

for i in "${!NETWORKS[@]}"; do
    NET=${NETWORKS[$i]}
    URL=${RPC_ENDPOINTS[$i]}
    
    # Measure 3D resonance (Latency)
    START=$(date +%s%N)
    curl -s --max-time 2 "$URL" > /dev/null
    END=$(date +%s%N)
    
    LATENCY=$(( (END - START) / 1000000 )) # ms
    echo "Network $NET: ${LATENCY}ms"
    
    if [ "$LATENCY" -lt "$BEST_LATENCY" ] && [ "$LATENCY" -gt 0 ]; then
        BEST_LATENCY=$LATENCY
        SELECTED_NET=$NET
    fi
done

echo "12D CHOICE: $SELECTED_NET (Latency: ${BEST_LATENCY}ms)"
echo "$SELECTED_NET" > /dev/shm/active_network
echo "$BEST_LATENCY" > /dev/shm/network_latency
