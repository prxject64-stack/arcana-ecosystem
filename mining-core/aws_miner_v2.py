import time
import os

LEDGER_PATH = "../blockchain.enc"
LOG_PATH = "miner.log"
FEE_PERCENT = 0.005 # 0.5% Infinite Fee

def mine_delta():
    while True:
        # Simulate Proof of Heat / ZKD-Hyperion Hashing
        time.sleep(60) 
        
        # Calculate Rewards
        reward = 1000000 # 1M ARC
        fee = reward * FEE_PERCENT
        net_yield = reward - fee
        
        # APPEND only (Delta) to the log instead of rewriting the 160MB enc file
        with open(LOG_PATH, "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] - SUCCESS - Mined {net_yield} ARC | Fee: {fee} ARC (ZKD-Hyperion)\n")
        
        print(f"Block Found: {net_yield} ARC secured.")

if __name__ == "__main__":
    mine_delta()
