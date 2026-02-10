import time
def monitor():
    print("--- Obsidian Layer: Amazon HQ Gate Monitoring ---")
    print("Node ID: AMAZON_HQ_01 | Status: ACTIVE")
    print("Throughput: 4,500/s | Liquidity: 136B CC")
    print("-------------------------------------------------")
    # This simulates a live hook into the miner --status stream
    while True:
        print(f"[{time.strftime('%H:%M:%S')}] Payout Processed: 1,240 CC | Latency: 312ms | Proof: VERIFIED")
        time.sleep(2)
