#!/bin/bash
# Phase 2, Day 10: The Multi-Node Relay (Origin Obfuscation)

# List of simulated Relay Nodes (Representing 12D Exit Points)
NODES=("192.168.1.101" "45.77.10.12" "104.248.5.99" "138.197.2.20" "82.196.3.14")

echo "--- ROTATING RELAY NODES ---"

# Pick a random node for this cycle
SELECTED_NODE=${NODES[$RANDOM % ${#NODES[@]}]}

# Store the selected node in RAM for the API Hook to use
echo "$SELECTED_NODE" > /dev/shm/current_node

echo "Current Exit Node: $SELECTED_NODE"
echo "Relay active. Signal origin shifted."
