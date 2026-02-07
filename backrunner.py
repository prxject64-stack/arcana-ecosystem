import asyncio
import json
import sys
from web3 import AsyncWeb3, Web3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION ---
LOCAL_RPC = "http://localhost:8545"
AERODROME_ROUTER = Web3.to_checksum_address("0xcF77a3Ba9A5CA399B7c97c74d54e5b1Beb874E43")
AERODROME_FACTORY = Web3.to_checksum_address("0x420DD381b31aEf6683db6B902084cB0FFECe40Da")
WETH = Web3.to_checksum_address("0x4200000000000000000000000000000000000006")
USDC = Web3.to_checksum_address("0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913")

w3 = AsyncWeb3(AsyncHTTPProvider(LOCAL_RPC))

async def simulate_backrun():
    print("🛰️ [SAT-LINK ACTIVE] Monitoring Base Tip...", flush=True)
    
    router_abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"components":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bool","name":"stable","type":"bool"},{"internalType":"address","name":"factory","type":"address"}],"internalType":"struct IRouter.route[]","name":"routes","type":"tuple[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"}]')
    contract = w3.eth.contract(address=AERODROME_ROUTER, abi=router_abi)
    route = [{"from": WETH, "to": USDC, "stable": False, "factory": AERODROME_FACTORY}]
    
    last_block = 0
    last_price = 0

    while True:
        try:
            # ONLY get the block number (Lightest request possible)
            curr_block = await w3.eth.block_number
            
            if curr_block > last_block:
                # New block found! Now fetch price
                amounts = await contract.functions.getAmountsOut(10**18, route).call()
                current_price = amounts[-1] / 10**6
                
                if last_price > 0:
                    impact = ((current_price - last_price) / last_price) * 100
                    print(f"📦 Block: {curr_block} | Price: {current_price:.2f} | Impact: {impact:.4f}%", flush=True)
                else:
                    print(f"📦 Block: {curr_block} | Initial Price: {current_price:.2f}", flush=True)
                
                last_price = current_price
                last_block = curr_block
            
            # Slow down slightly to avoid Alchemy RPS kickback
            await asyncio.sleep(1.0) 
            
        except Exception as e:
            # If we get a 429 error (Rate limit), sleep longer
            if "429" in str(e):
                print("⚠️ Rate Limited! Cooling down...", flush=True)
                await asyncio.sleep(5)
            else:
                print(f"⚠️ Error: {e}", flush=True)
                await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(simulate_backrun())
