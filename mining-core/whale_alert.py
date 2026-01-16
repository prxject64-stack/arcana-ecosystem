import time
import os

LOG_FILE = "miner.log"
WHALE_THRESHOLD = 1000000  # Alert if > 1M ARC

def watch_for_whales():
    print("Whale Alert System: [ONLINE]")
    # Move to the end of the file
    file_size = os.path.getsize(LOG_FILE)
    
    with open(LOG_FILE, "r") as f:
        f.seek(file_size)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            
            if "SUCCESS" in line:
                # Extract the mined amount
                try:
                    amount = float(line.split("Mined ")[1].split(" ARC")[0])
                    if amount >= WHALE_THRESHOLD:
                        print(f"\n[!!!] WHALE DETECTED [!!!]")
                        print(f"Details: {line.strip()}")
                except Exception:
                    continue

if __name__ == "__main__":
    watch_for_whales()
