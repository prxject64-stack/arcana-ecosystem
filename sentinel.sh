#!/bin/bash
SERVER_IP="3.16.37.77"
echo "Starting Arcana Sentinel for node $SERVER_IP..."

while true; do
    RESPONSE=$(curl -s -X POST http://$SERVER_IP/join)
    if [[ $RESPONSE == *"ARC-"* ]]; then
        echo "$(date): [SUCCESS] Node is active. Response: $RESPONSE"
    else
        echo "$(date): [ALERT] NODE DOWN OR UNSTABLE!"
        echo "Check server: sudo python3 -m uvicorn onboard:app"
    fi
    sleep 60
done
