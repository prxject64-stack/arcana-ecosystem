#!/bin/bash
THRESHOLD=1000
ALERT_SENT=false

echo "--- MILESTONE WATCHER ACTIVE ---"
echo "Target: $THRESHOLD CC"
echo "--------------------------------"

while true
do
    # Calculate current balance from ledger.json
    # Sums all 'amount' values where recipient is your address
    CURRENT_BALANCE=$(jq '[.[] | .transactions[] | select(.recipient == "arcana_b8b59183c7cbd51eb577135fb48317888ee48282") | .amount] | add' ledger.json)
    
    # Handle null/empty cases
    if [ "$CURRENT_BALANCE" == "null" ]; then CURRENT_BALANCE=0; fi

    if [ "$CURRENT_BALANCE" -ge "$THRESHOLD" ] && [ "$ALERT_SENT" = false ]; then
        echo -e "\a" # Terminal Bell Sound
        echo "#########################################"
        echo "# MILESTONE REACHED: $CURRENT_BALANCE CC #"
        echo "#########################################"
        ALERT_SENT=true
    elif [ "$CURRENT_BALANCE" -lt "$THRESHOLD" ]; then
        # Reset if balance drops (e.g., if you spend money later)
        ALERT_SENT=false
    fi
    
    sleep 60
done
