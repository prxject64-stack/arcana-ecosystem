import asyncio
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

# --- CONFIGURATION: HIGH VOLUME TARGETS ---
BASE_RPC = "https://mainnet.base.org"
AERODROME_ROUTER = "0xcF77a3Ba9A5CA399B7c97c74d54e5b1Beb874E43"
UNISWAP_V3_BASE = "0x33782761817367f0f6717a6a7c3697976e536965"

w3 = AsyncWeb3(AsyncHTTPProvider(BASE_RPC))

async def sniff_volume():
    print(f"📡 High-Volume Radar Live: Monitoring Aerodrome & Uniswap...")
    while True:
        try:
            block = await w3.eth.get_block('latest', full_transactions=True)
            count = 0
            for tx in block.transactions:
                if tx['to'] and tx['to'].lower() in [AERODROME_ROUTER.lower(), UNISWAP_V3_BASE.lower()]:
                    count += 1
            if count > 0:
                print(f"💰 MONEY DETECTED: {count} swaps in block {block['number']}")
            await asyncio.sleep(1)
        except Exception as e:
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(sniff_volume())
