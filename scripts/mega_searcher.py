import asyncio
import time
from web3 import Web3, AsyncWeb3
from web3.providers import AsyncHTTPProvider

# FEB 9, 2026 LIVE ENDPOINTS
MAINNET_RPC = "https://mainnet.infura.io/v3/3842a81a77b74adb984f313801fa3d57"
MEGAETH_RPC = "https://mainnet.megaeth.com/rpc" 

# BTC.b (LOMBARD) & WETH ADDRESSES
WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
BTC_B = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599" # Canonical BTC.b on MegaETH

UNI_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
ABI = '[{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"}]'

async def fetch_price(w3, router_addr, path, decimals):
    try:
        contract = w3.eth.contract(address=router_addr, abi=ABI)
        amount = 10**8 if "0x226" in path[0] else 10**18
        res = await contract.functions.getAmountsOut(amount, path).call()
        return res[-1] / (10**decimals)
    except: return None

async def monitor():
    w3_main = AsyncWeb3(AsyncHTTPProvider(MAINNET_RPC))
    w3_mega = AsyncWeb3(AsyncHTTPProvider(MEGAETH_RPC))
    
    print(f"--- r7iz SAUNA PROTOCOL: MEGAETH LIVE ---")
    
    while True:
        # Concurrent fetching for 10ms parity
        p_main_task = fetch_price(w3_main, UNI_ROUTER, [WETH, USDC], 6)
        p_mega_task = fetch_price(w3_mega, UNI_ROUTER, [WETH, USDC], 6)
        
        p_main, p_mega = await asyncio.gather(p_main_task, p_mega_task)
        
        if p_main and p_mega:
            spread = abs(p_main - p_mega) / ((p_main + p_mega)/2) * 100
            status = "!! HIT !!" if spread > 0.6 else "wait"
            print(f"[{time.strftime('%H:%M:%S.%f')[:-3]}] Spread: {spread:.4f}% | Main: ${p_main:.2f} | Mega: ${p_mega:.2f} ({status})", end="\r")
        
        await asyncio.sleep(0.01) # 10ms heartbeat to match MegaETH blocks

if __name__ == "__main__":
    asyncio.run(monitor())
