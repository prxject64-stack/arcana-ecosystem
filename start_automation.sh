#!/bin/bash
echo "--- ARCANA AUTOMATION ACTIVE ---"
echo "Target: http://127.0.0.1:5000/mine"
echo "Interval: 30 Seconds"
echo "Press [CTRL+C] to stop the heartbeat."
echo "--------------------------------"

while true
do
    # Perform the pulse and hide the extra text
    curl -s http://127.0.0.1:5000/mine > /dev/null
    
    # Log the time to the terminal so you know it's working
    echo "Pulse sent at $(date +'%H:%M:%S') - +50 CC Secured"
    
    # Wait for the next cycle
    sleep 30
done
