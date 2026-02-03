#!/bin/bash
# Arcana Ecosystem: Yield Projection v1.0
LOG_FILE="revenue_ledger.log"
INITIAL_LIQUIDITY=136000000000

if [ ! -f "$LOG_FILE" ]; then
    echo "[ERROR]: No revenue data found. Run ./collect_fees.sh first to generate logs."
    exit 1
fi

# Extract the last 60 minutes of profit data from the log
RECENT_FEES=$(tail -n 60 "$LOG_FILE" | grep "PROFIT" | awk '{print $3}' | paste -sd+ - | bc)

if [ -z "$RECENT_FEES" ]; then RECENT_FEES=0; fi

# Forecast Calculations
HOURLY_EST=$(echo "scale=2; $RECENT_FEES" | bc)
DAILY_EST=$(echo "scale=2; $HOURLY_EST * 24" | bc)
WEEKLY_EST=$(echo "scale=2; $DAILY_EST * 7" | bc)
MONTHLY_EST=$(echo "scale=2; $DAILY_EST * 30" | bc)

echo "-------------------------------------"
echo "   ARCANA SOVEREIGN YIELD REPORT     "
echo "-------------------------------------"
echo "Hourly Projection:  $HOURLY_EST CC"
echo "Daily Projection:   $DAILY_EST CC"
echo "Weekly Projection:  $WEEKLY_EST CC"
echo "Monthly Projection: $MONTHLY_EST CC"
echo "-------------------------------------"
echo "Projected Annual ROI: $(echo "scale=4; ($MONTHLY_EST * 12 / $INITIAL_LIQUIDITY) * 100" | bc)%"
echo "-------------------------------------"
