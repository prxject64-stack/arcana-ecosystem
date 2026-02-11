import asyncio
import time
from web3 import AsyncWeb3

# --- CONFIG ---
RPC_URL = "http://127.0.0.1:8545"
VAULT_ADDR = "0xBf073f0aAA5Fe1C9612bc376158B572E4263cAf9"
MINER_ADDR = "0x19d37AEaA1FAE9a0942177CA6f047C3f4CFd0482"
NUM_SWAPS = 4500

async def main():
    w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(RPC_URL))
    
    if not await w3.is_connected():
        print("❌ Node not responding. Check geth_node.log")
        return

    nonce = await w3.eth.get_transaction_count(MINER_ADDR)
    gas_price = await w3.eth.gas_price
    chain_id = await w3.eth.chain_id

    print(f"🚀 Injecting 4,500 swaps for 136B CC ecosystem. Starting nonce: {nonce}")

    for i in range(NUM_SWAPS):
        tx = {
            'from': MINER_ADDR,
            'to': VAULT_ADDR,
            'value': w3.to_wei(0.01, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'nonce': nonce + i,
            'chainId': chain_id
        }
        
        try:
            await w3.eth.send_transaction(tx)
            if i % 500 == 0:
                print(f"✅ Status: {i}/4500 injected...")
            # Tiny sleep to prevent RPC flooding/crash
            await asyncio.sleep(0.01) 
        except Exception as e:
            print(f"🛑 Error at {i}: {e}")
            break

    print("🏁 Injection complete. 4,500 swaps are now in the Sauna Protocol pipeline.")

if __name__ == "__main__":
    asyncio.run(main())
