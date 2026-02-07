import asyncio
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION ---
RPC_URL = "http://localhost:8547"
GOD_KEY = "0x93fdaa6afd2c665f9dedf7dd3e2ad0f1949719008740d3c03cf86233b9b68cb4"
EXECUTOR_ADDR = "0xc6639De27d334Ca9E87EE00219CAE5B848BE7246"
TOKEN_ADDR = "0x16f6CDA8205854473f617311d2672991B2a388b1"
RECIPIENT = "0x7BfBFCAcEda78A54Fa0C6CAD236AB5a6c11B7a29"
TOTAL_SWAPS = 4500
SWAP_AMOUNT = 1000 

# v7 uses AsyncWeb3 directly
w3 = AsyncWeb3(AsyncHTTPProvider(RPC_URL))
account = w3.eth.account.from_key(GOD_KEY)

ABI = [
    {
        "inputs": [
            {"name": "token", "type": "address"},
            {"name": "to", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "name": "executeSwap",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

async def send_swap(nonce):
    try:
        contract = w3.eth.contract(address=EXECUTOR_ADDR, abi=ABI)
        tx = await contract.functions.executeSwap(
            TOKEN_ADDR, RECIPIENT, SWAP_AMOUNT
        ).build_transaction({
            'from': account.address,
            'nonce': nonce,
            'gas': 120000,
            'gasPrice': w3.to_wei('0.1', 'gwei'),
            'chainId': 412346
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = await w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        return tx_hash.hex()
    except Exception as e:
        return f"Error at nonce {nonce}: {e}"

async def main():
    print(f"🚀 Launching Swarm Strike (v7 Engine): {TOTAL_SWAPS} P2P Swaps...")
    start_nonce = await w3.eth.get_transaction_count(account.address)
    
    batch_size = 500 
    for i in range(0, TOTAL_SWAPS, batch_size):
        end_idx = min(i + batch_size, TOTAL_SWAPS)
        current_batch = range(start_nonce + i, start_nonce + end_idx)
        tasks = [send_swap(n) for n in current_batch]
        results = await asyncio.gather(*tasks)
        
        successes = [r for r in results if not r.startswith("Error")]
        print(f"📡 Batch {i//batch_size + 1} complete: {len(successes)}/{len(tasks)} successful.")

    print("🏁 Swarm Engine strike finalized.")

if __name__ == "__main__":
    asyncio.run(main())
