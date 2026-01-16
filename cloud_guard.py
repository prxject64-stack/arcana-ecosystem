import os
import time

# For T3 instances, we watch CPU Load as a proxy for Credit Drain
MAX_LOAD = 0.90 # 90% CPU Load limit

def cloud_watchdog():
    print(f"☁️ Cloud Guard: ACTIVE (Limit: {MAX_LOAD*100}% CPU)")
    while True:
        # Get the 1-minute load average
        load1, load5, load15 = os.getloadavg()
        # On a t3.micro (2 vCPUs), a load of 2.0 is 100%
        cpu_usage = load1 / 2.0 
        
        if cpu_usage > MAX_LOAD:
            print(f"\n[!!!] HIGH LOAD: {cpu_usage*100:.1f}% - PAUSING MINER")
            os.system("pkill -f multi_core_miner.py")
            # Wait for credits to "recharge"
            time.sleep(300) 
        time.sleep(5)

if __name__ == "__main__":
    cloud_watchdog()
