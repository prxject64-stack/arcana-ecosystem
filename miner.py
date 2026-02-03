import time
import os

def mine():
    print("ARCANA-ECOSYSTEM: Miner Starting...")
    while True:
        entry = {"ts": time.time(), "id": os.urandom(8).hex()}
        print(f"Block Mined: {entry['id']}")
        time.sleep(10)

if __name__ == "__main__":
    mine()
