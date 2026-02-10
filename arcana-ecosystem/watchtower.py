import asyncio
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION ---
RPC_URL = "http://localhost:8547"
EXECUTOR_ADDR = "0xc6639De27d334Ca9E87EE00219CAE5B848BE7246"
GOD_KEY_ADDR = "0x0Ed60278e8A7C9520611EBDcB214C374b91BF05e"

w3 = AsyncWeb3(AsyncHTTPProvider(RPC_URL))

async def monitor():
    print(f"🛡️ Watchtower Active: Monitoring Executor {EXECUTOR_ADDR}")
    last_block = await w3.eth.block_number
    
    while True:
        try:
            curr_block = await w3.eth.block_number
            if curr_block > last_block:
                for bn in range(last_block + 1, curr_block + 1):
                    block = await w3.eth.get_block(bn, full_transactions=True)
                    for tx in block.transactions:
                        if tx['to'] == EXECUTOR_ADDR:
                            sender = tx['from']
                            status = "✅ AUTHORIZED" if sender == GOD_KEY_ADDR else "🚨 UNAUTHORIZED"
                            print(f"[{status}] Block: {bn} | From: {sender} | Value: {tx['value']}")
                last_block = curr_block
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Watchtower Error: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(monitor())
