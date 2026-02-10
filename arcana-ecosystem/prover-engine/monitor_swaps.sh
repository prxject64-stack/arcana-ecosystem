#!/bin/bash
THRESHOLD=1.5
API_URL="http://localhost:8000/verify/WATCHDOG_PING"
API_KEY="arcana_pro_001"
echo "--- ARCANA PRO-SERIES MONITOR ACTIVE ---"
while true; do
    RESPONSE=$(curl -s -o /dev/null -w "%{http_code} %{time_total}" -H "X-API-Key: $API_KEY" "$API_URL")
    STATUS=$(echo $RESPONSE | awk '{print $1}')
    LATENCY=$(echo $RESPONSE | awk '{print $2}')
    if [ "$STATUS" != "200" ]; then
        echo "[$(date)] ALERT: Status $STATUS. Restarting..."
        fuser -k 8000/tcp
        sleep 5
        export PYTHONPATH=$PYTHONPATH:$(pwd)/prover-engine
        nohup python3 -u truststack_api.py >> api.log 2>&1 &
        sleep 10
    else
        echo "[$(date)] STATUS: HEALTHY | LATENCY: $LATENCY s"
    fi
    sleep 30
done
