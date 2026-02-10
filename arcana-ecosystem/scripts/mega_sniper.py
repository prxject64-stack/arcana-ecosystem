import asyncio
import time
from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

# FEB 9, 2026 LIVE CONFIG
MAINNET_RPC = "https://mainnet.infura.io/v3/3842a81a77b74adb984f313801fa3d57"
MEGAETH_RPC = "https://mainnet.megaeth.com/rpc" 

# ASSETS (MegaETH Native)
WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
USDM = "0x5fdf0a645228892404f21570d519b33a55856711" # USDm Ethena/MegaETH
USDC_MAIN = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

# KUMBAYA DEX (Primary MegaETH Liquidity Hub)
KUMBAYA_ROUTER = "0x582522718E23192B452D37207869687103831822" # Official Feb 9 Deployment

ABI = '[{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"}]'

async def get_price(w3, router, path):
    try:
        contract = w3.eth.contract(address=w3.to_checksum_address(router), abi=ABI)
        res = await contract.functions.getAmountsOut(10**18, path).call()
        return res[-1] / 10**6 # USDm uses 6 decimals
    except: return None

async def run():
    w3_m = AsyncWeb3(AsyncHTTPProvider(MAINNET_RPC))
    w3_mega = AsyncWeb3(AsyncHTTPProvider(MEGAETH_RPC))
    print(f"--- r7iz SAUNA: KUMBAYA LIQUIDITY SCAN ---")
    
    while True:
        # Mainnet Reference (WETH/USDC)
        p_main = await get_price(w3_m, "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", [WETH, USDC_MAIN])
        # MegaETH Local (WETH/USDm)
        p_mega = await get_price(w3_mega, KUMBAYA_ROUTER, [WETH, USDM])
        
        if p_main and p_mega:
            spread = abs(p_main - p_mega) / ((p_main + p_mega)/2) * 100
            status = "!! HIT !!" if spread > 0.8 else "low"
            print(f"[{time.strftime('%H:%M:%S')}] WETH/USDm Spread: {spread:.4f}% | Main: ${p_main:.2f} | Mega: ${p_mega:.2f}", end="\r")
        else:
            # If the router is silent, we poll the Block Height to verify connectivity
            bh = await w3_mega.eth.block_number
            print(f"[{time.strftime('%H:%M:%S')}] Polling Kumbaya... (Mega Block #{bh})", end="\r")
        
        await asyncio.sleep(0.1) # 100ms polling

if __name__ == "__main__":
    asyncio.run(run())
