import time
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

COINBASE = "0xc6757EFa426A3fC4EA842DC36c6658032dE25d07"

def run_test(num_swaps):
    print(f"🚀 Injecting {num_swaps} swaps for 136B CC ecosystem.")
    try:
        nonce = w3.eth.get_transaction_count(COINBASE)
        base_gas_price = w3.eth.gas_price
        
        for i in range(num_swaps):
            tx = {
                'from': COINBASE,
                'nonce': nonce + i,
                'to': COINBASE,
                'value': 0,
                'gas': 21000,
                'gasPrice': base_gas_price,
                'chainId': 1337
            }
            w3.eth.send_transaction(tx)
            if i % 100 == 0:
                print(f"✅ Injected {i} swaps...")
        print("🏁 All 4,500 swaps injected.")
    except Exception as e:
        print(f"🛑 Critical Error: {e}")

if __name__ == "__main__":
    run_test(4500)
