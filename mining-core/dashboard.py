import os
import re

LOG_FILE = "miner.log"

def calculate_stats():
    total_mined = 0
    total_fees = 0
    blocks_count = 0

    if not os.path.exists(LOG_FILE):
        print("Waiting for miner to generate logs...")
        return

    # Regex to extract numeric values from the logs
    # Format: Mined X ARC | Fee: Y ARC
    with open(LOG_FILE, "r") as f:
        for line in f:
            match = re.search(r"Mined ([\d.]+) ARC \| Fee: ([\d.]+) ARC", line)
            if match:
                total_mined += float(match.group(1))
                total_fees += float(match.group(2))
                blocks_count += 1

    print("="*40)
    print("      ARCANA ECOSYSTEM DASHBOARD      ")
    print("="*40)
    print(f"Total Blocks Found:  {blocks_count}")
    print(f"Gross ARC Mined:     {total_mined + total_fees:,.2f}")
    print(f"Infinite Fees (0.5%): {total_fees:,.2f}")
    print(f"Net Wealth (CC):     {total_mined:,.2f}")
    print("-" * 40)
    print(f"Current Profitability: SUCCESS")
    print("="*40)

if __name__ == "__main__":
    calculate_stats()
