import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

MASTER_CSV = "master_ledger.csv"
TARGET_GOAL = 1000000000  # 1 Billion ARC

def project_wealth():
    if not os.path.exists(MASTER_CSV) or os.stat(MASTER_CSV).st_size < 100:
        print("[!] Error: Master Ledger is empty or missing. Run consolidation with valid worker IPs.")
        return

    df = pd.read_csv(MASTER_CSV)
    if df.empty:
        print("[!] Error: No mining data found in ledger.")
        return

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values('Timestamp')

    current_wealth = df['Net_ARC'].sum() + 500000000
    
    # Calculate velocity only if we have at least 2 data points
    if len(df) < 2:
        print("[i] Waiting for more data points to calculate velocity...")
        print(f"Current Wealth: {current_wealth:,.2f} ARC")
        return

    time_delta = (df['Timestamp'].max() - df['Timestamp'].min()).total_seconds() / 3600
    
    if time_delta == 0:
        arc_per_hour = 0
    else:
        arc_per_hour = df['Net_ARC'].sum() / time_delta

    if arc_per_hour <= 0:
        print("[!] Warning: Mining velocity is 0. Check worker nodes.")
        return

    remaining_arc = TARGET_GOAL - current_wealth
    hours_to_goal = remaining_arc / arc_per_hour
    target_date = datetime.now() + timedelta(hours=float(hours_to_goal))

    print("="*45)
    print("      ARCANA LIQUIDITY PROJECTION       ")
    print("="*45)
    print(f"Current Wealth:   {current_wealth:,.2f} ARC")
    print(f"Mining Velocity:  {arc_per_hour:,.2f} ARC/Hour")
    print("-" * 45)
    print(f"Estimated Time:   {hours_to_goal/24:,.2f} Days")
    print(f"Target 1B Date:   {target_date.strftime('%Y-%m-%d %H:%M')}")
    print("="*45)

if __name__ == "__main__":
    project_wealth()
