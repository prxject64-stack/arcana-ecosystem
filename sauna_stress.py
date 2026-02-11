import time
from web3 import Web3
from eth_account import Account
from web3.middleware import ExtraDataToPOAMiddleware 
from concurrent.futures import ThreadPoolExecutor

# 1. Connect to Arcana L1
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

if not w3.is_connected():
    print("CRITICAL: Arcana Node offline.")
    exit()

SENDER_ADDR = "0xBdae565eff11d46dfD2154442f0a565B4011F3b8"
TARGET_TPS = 4500
CHAIN_ID = 12345

def send_batch():
    nonce = w3.eth.get_transaction_count(SENDER_ADDR)
    print(f"--- ARCANA SOVEREIGN (ARC) STRESS TEST ---")
    print(f"Starting Stress Test at Nonce: {nonce}")
    
    # London Fork Fix: Set a minimum gas price (1 Gwei)
    min_gas_price = w3.to_wei(1, 'gwei')
    
    tx_list = []
    print(f"Generating {TARGET_TPS} Random Recipient Swaps...")
    
    for i in range(TARGET_TPS):
        receiver = Account.create().address
        tx = {
            'from': SENDER_ADDR,
            'to': receiver,
            'value': w3.to_wei(1, 'ether'),
            'gas': 21000,
            'gasPrice': min_gas_price, # Set to non-zero for London Fork
            'nonce': nonce + i,
            'chainId': CHAIN_ID
        }
        tx_list.append(tx)

    print("Broadcasting to Arcana Mempool...")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Transactions are sent to the node for signing/broadcasting
        results = list(executor.map(lambda t: w3.eth.send_transaction(t), tx_list))
        
    duration = time.time() - start_time
    print(f"Finished in {duration:.2f}s | Effective TPS: {len(results)/duration:.2f}")

if __name__ == "__main__":
    send_batch()
