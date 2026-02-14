import asyncio
import json
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION ---
BASE_RPC = "https://mainnet.base.org" # Public RPC or your Alchemy URL
TARGET_ENGINE = "0x418e22722f5a6c11b7a2916f6cdA8205854473f6"

w3 = AsyncWeb3(AsyncHTTPProvider(BASE_RPC))

async def sniff():
    print(f"📡 Interceptor Live: Listening for AlphaSec orders on Base...")
    seen_txs = set()
    
    while True:
        try:
            # In 2026, most L2s allow polling the 'pending' block
            block = await w3.eth.get_block('pending', full_transactions=True)
            for tx in block.transactions:
                if tx['to'] == TARGET_ENGINE and tx['hash'] not in seen_txs:
                    print(f"🕵️ ORDER DETECTED: {tx['hash'].hex()}")
                    print(f"📊 Input Data: {tx['input'][:64]}...")
                    # Save for our local stress-test
                    with open("captured_orders.log", "a") as f:
                        f.write(f"{tx['hash'].hex()}:{tx['input']}\n")
                    seen_txs.add(tx['hash'])
            await asyncio.sleep(0.5) # High-speed polling
        except Exception as e:
            print(f"⚠️ Connection lag: {e}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(sniff())
