#!/bin/bash
# Constants based on $727.7M Annual Savings / 31,536,000 seconds
SAVINGS_PER_SEC=23.076
YIELD_PER_SEC=0.441 # Based on 13.9M CC annual fee yield

echo "--- ARCANA LIVE SAVINGS & YIELD DASHBOARD ---"
echo "Metrics: 4,500 TPS | 136B CC Principal"
echo "---------------------------------------------"

TOTAL_SAVED=0
TOTAL_YIELD=0

# Loop for live visualization during the meeting
for i in {1..3600}
do
    TOTAL_SAVED=$(echo "$TOTAL_SAVED + $SAVINGS_PER_SEC" | bc -l)
    TOTAL_YIELD=$(echo "$TOTAL_YIELD + $YIELD_PER_SEC" | bc -l)
    
    # Format for clean display
    PRINT_SAVED=$(printf "%.2f" $TOTAL_SAVED)
    PRINT_YIELD=$(printf "%.2f" $TOTAL_YIELD)
    
    echo -ne "RECOVERED CAPITAL: \$$PRINT_SAVED | PROTOCOL YIELD: $PRINT_YIELD CC\r"
    sleep 1
done
