#!/bin/bash
# Phase 2, Day 9: The Decoy-Traffic Generator (Network Camouflage)

# List of highly common 3D targets to blend in with
TARGETS=("google.com" "wikipedia.org" "github.com" "ubuntu.com" "nasa.gov" "kernel.org")

echo "--- DEPLOYING DIGITAL CHAFF ---"

# Generate 3-5 random pings to create noise
NUM_DECOYS=$((3 + RANDOM % 3))

for ((i=1; i<=NUM_DECOYS; i++)); do
    TARGET=${TARGETS[$RANDOM % ${#TARGETS[@]}]}
    # Perform a light 'head' request to mimic browsing
    curl -I -s --max-time 2 "https://$TARGET" > /dev/null
    echo "Decoy signal sent to $TARGET"
    # Random short delay between decoys
    sleep $((1 + RANDOM % 3))
done

echo "SUCCESS: Network camouflage established."
