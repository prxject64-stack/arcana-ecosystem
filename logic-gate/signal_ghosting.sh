#!/bin/bash
# Phase 2, Day 27: Signal-Ghosting (Traffic Dilution Protocol)

# List of "Innocent" 3D Domains
GHOST_SITES=(
    "en.wikipedia.org"
    "www.bbc.com"
    "www.weather.com"
    "www.reuters.com"
    "www.nationalgeographic.com"
)

# Pick a random site
TARGET=${GHOST_SITES[$RANDOM % ${#GHOST_SITES[@]}]}

echo "--- INITIATING SIGNAL GHOSTING ---"
echo "Sending decoy request to $TARGET..."

# 3. Send a stealthy background request (pulling just the head to save data)
curl -s -I "https://$TARGET" > /dev/null &

echo "Ghosting complete. Financial traffic diluted."
