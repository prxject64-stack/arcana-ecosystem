import asyncio
import time
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

MEGAETH_RPC = "https://mainnet.megaeth.com/rpc"
w3 = AsyncWeb3(AsyncHTTPProvider(MEGAETH_RPC))

# LOMBARD ASSETROUTER - The Bridge Gatekeeper
LOMBARD_ROUTER = w3.to_checksum_address("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599")

async def watch_bridge():
    print(f"--- r7iz SAUNA: INFINEX/LOMBARD BRIDGE WATCH ---")
    print(f"TARGET: 09:00 AM EST RETAIL FLOOD")
    
    while True:
        try:
            # We poll the transaction count. If it increases, the bridge is active.
            tx_count = await w3.eth.get_transaction_count(LOMBARD_ROUTER)
            bh = await w3.eth.block_number
            
            if tx_count > 0:
                print(f"\n[!!!] BRIDGE ACTIVITY DETECTED: {tx_count} Transactions")
                print(f"ACTION: LIQUIDITY IS FLOWING. STARTING ARCANA SNIPER.")
                break
            else:
                # Polling at 100ms to stay ahead of the Infinex launch
                print(f"[{time.strftime('%H:%M:%S')}] Polling Lombard Bridge... Block #{bh} (Inactive)", end="\r")
        except:
            print(f"[{time.strftime('%H:%M:%S')}] RPC Congestion. Retrying...", end="\r")
        
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(watch_bridge())
