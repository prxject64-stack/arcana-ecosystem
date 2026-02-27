import time
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
VAULT = Web3.to_checksum_address("0xbdae565eff11d46dfd2154442f0a565b4011f3b8")

def log_revenue():
    while True:
        try:
            if w3.is_connected():
                bal = w3.eth.get_balance(VAULT)
                print(f"[{time.strftime('%H:%M:%S')}] Total Liquidity: {w3.from_wei(bal, 'ether'):,.2f} CC-P")
            else:
                print("Reconnecting to ARC-S...")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)

if __name__ == "__main__":
    log_revenue()
