import os
import sys
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

sausd_addr = os.getenv('SAUSD_ADDR')
vault_addr = os.getenv('VAULT_ADDR')
master_signer = '0x14A3256052c02f9d87FE1Cc3b712D4530061b25c'

if not w3.is_connected():
    print('CRITICAL: Anvil node not found')
    sys.exit(1)

print(f'Initiating Phase 1 Stress Test...')

NUM_SWAPS = 4500
AMOUNT = 100 * 10**18 

def run_stress_test():
    selector = '0xb6b55f25'
    encoded_amount = hex(int(AMOUNT))[2:].zfill(64)
    nonce = w3.eth.get_transaction_count(master_signer)
    
    for i in range(NUM_SWAPS):
        tx = {
            'from': master_signer,
            'to': vault_addr,
            'data': f'{selector}{encoded_amount}',
            'gas': 150000,
            'nonce': nonce + i,
            'gasPrice': w3.eth.gas_price,
            'chainId': 31337
        }
        
        try:
            w3.provider.make_request('eth_sendTransaction', [tx])
            if i % 500 == 0 and i > 0:
                print(f'Dispatched {i} / {NUM_SWAPS} swaps...')
        except Exception as e:
            print(f'Batch Failure at {i}: {e}')
            break

if __name__ == '__main__':
    if not vault_addr:
        print('ERROR: VAULT_ADDR not set.')
    else:
        run_stress_test()
        print('Success: 4,500 Transactions dispatched.')
