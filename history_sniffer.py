import asyncio
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION ---
BASE_RPC = "https://mainnet.base.org"
TARGET_ENGINE = "0x418e22722f5a6c11b7a2916f6cdA8205854473f6"

w3 = AsyncWeb3(AsyncHTTPProvider(BASE_RPC))

async def scan_history():
    print(f"📡 Scanning last 100 blocks for AlphaSec activity...")
    latest = await w3.eth.block_number
    for i in range(latest - 100, latest + 1):
        block = await w3.eth.get_block(i, full_transactions=True)
        for tx in block.transactions:
            if tx['to'] and tx['to'].lower() == TARGET_ENGINE.lower():
                print(f"✅ FOUND ACTIVITY: Block {i} | Hash {tx['hash'].hex()}")
                print(f"📊 Method ID: {tx['input'][:10]}")
    print("🏁 Scan complete.")

if __name__ == "__main__":
    asyncio.run(scan_history())
