import asyncio
from web3 import AsyncWeb3, Web3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION ---
LOCAL_RPC = "http://localhost:8545"
TARGET_CONTRACT = Web3.to_checksum_address("0x418E22722F5A6C11B7A2916F6Cda8205854473F6")
w3 = AsyncWeb3(AsyncHTTPProvider(LOCAL_RPC))

async def hammer_state():
    print(f"🌀 [TEMPORAL STRIKE] Testing AlphaSec across block transitions...")
    
    pre_balance = await w3.eth.get_balance(TARGET_CONTRACT)
    accounts = await w3.eth.accounts
    
    async def heavy_hit(account, count=5):
        success = 0
        for _ in range(count):
            try:
                # Force a block mine manually every few hits to simulate network progression
                if _ % 2 == 0:
                    await w3.provider.make_request("evm_mine", [])
                
                nonce = await w3.eth.get_transaction_count(account)
                tx = {
                    'from': account, 'to': TARGET_CONTRACT, 'value': w3.to_wei(0.001, 'ether'),
                    'gas': 120000, 'maxFeePerGas': w3.to_wei(200, 'gwei'), 
                    'maxPriorityFeePerGas': w3.to_wei(50, 'gwei'), 
                    'nonce': nonce, 'chainId': 8453
                }
                await w3.eth.send_transaction(tx)
                success += 1
            except:
                pass
        return success

    # Increase the load: 10 accounts firing in a dirty state
    tasks = [heavy_hit(acc, 15) for acc in accounts[:10]]
    print(f"🔥 Launching 150-hit Temporal Swarm...")
    results = await asyncio.gather(*tasks)
    
    total_hits = sum(results)
    post_balance = await w3.eth.get_balance(TARGET_CONTRACT)
    
    expected_gain = w3.to_wei(total_hits * 0.001, 'ether')
    actual_gain = post_balance - pre_balance
    
    print(f"🏁 Strike Finalized. Total Hits: {total_hits}")
    print(f"📊 Actual Delta: {w3.from_wei(actual_gain, 'ether')} ETH")
    
    if actual_gain == expected_gain:
        print("🛡️ VERDICT: AlphaSec is mathematically consistent across block transitions.")
    else:
        print(f"🚨 CRITICAL: STATE DRIFT DETECTED. Gap: {w3.from_wei(expected_gain - actual_gain, 'ether')} ETH")

if __name__ == "__main__":
    asyncio.run(hammer_state())
