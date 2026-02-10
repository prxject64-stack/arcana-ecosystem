import time
import sys
from web3 import Web3
from concurrent.futures import ThreadPoolExecutor

RPC_URL = "https://mainnet.infura.io/v3/3842a81a77b74adb984f313801fa3d57"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

PAIRS = [
    {"name": "WETH/USDC", "path": ["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"]},
    {"name": "LINK/WETH", "path": ["0x514910771AF9Ca656af840dff83E8264EcF986CA", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"]},
    {"name": "WBTC/WETH", "path": ["0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"]}
]

ROUTERS = {
    "UNI": w3.to_checksum_address("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"),
    "SUSHI": w3.to_checksum_address("0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F")
}

ABI = '[{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"}]'

def get_gas_cost():
    try:
        # Average gas for 2 swaps = 300,000 gas
        gas_price = w3.eth.gas_price
        eth_price_in_usdc = 2700 # Static estimate for faster loop
        cost_in_eth = (300000 * gas_price) / 10**18
        return cost_in_eth * eth_price_in_usdc
    except: return 50.0

def check_pair(pair):
    try:
        uni = w3.eth.contract(address=ROUTERS["UNI"], abi=ABI)
        sushi = w3.eth.contract(address=ROUTERS["SUSHI"], abi=ABI)
        input_amt = 10**8 if "WBTC" in pair["name"] else 10**18
        
        p_uni = uni.functions.getAmountsOut(input_amt, pair["path"]).call()[-1]
        p_sushi = sushi.functions.getAmountsOut(input_amt, pair["path"]).call()[-1]
        
        avg = (p_uni + p_sushi) / 2
        spread_pct = (abs(p_uni - p_sushi) / avg) * 100
        
        # Arbitrage is only "GO" if spread > 0.6% (DEX fees) + Gas impact
        status = "HIT" if spread_pct > 0.8 else "low"
        return f"{pair['name']}: {spread_pct:.3f}% ({status})"
    except: return None

print(f"--- r7iz ARCANA SECURITY SCANNER ---")
print(f"ESTIMATED GAS COST PER TRADE: ${get_gas_cost():.2f}")
while True:
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(check_pair, PAIRS))
        print(f"[{time.strftime('%H:%M:%S')}] {' | '.join([r for r in results if r])}      ", end="\r")
    time.sleep(1)
