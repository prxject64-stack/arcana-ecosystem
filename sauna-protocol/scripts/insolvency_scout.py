import urllib3
urllib3.util.ssl_.DEFAULT_CIPHERS = "DEFAULT@SECLEVEL=2"
import os
import requests
import time

# Treasury Wallet: coKaiynne / Unified Council
TREASURY_ADDRESS = "0x99f4176ee457afedffcb1839c7ab7a030a5e4a92"
ETHERSCAN_API = "5S4V...HIDDEN_KEY"

def check_treasury():
    url = f"https://api.optimistic.etherscan.io/api?module=account&action=tokentx&address={TREASURY_ADDRESS}&apikey={ETHERSCAN_API}"
    response = requests.get(url).json()
    
    for tx in response.get('result', []):
        if int(tx['value']) > 100000 * 10**18: # 100k sUSD+
            print(f"!!! LARGE OUTFLOW DETECTED: {tx['to']} received {int(tx['value'])/10**18} tokens !!!")
            with open("war_room/evidence/outflows.log", "a") as f:
                f.write(f"TS: {tx['timeStamp']} | TO: {tx['to']} | VAL: {tx['value']}\n")

if __name__ == "__main__":
    while True:
        check_treasury()
        time.sleep(300) # Check every 5 mins
