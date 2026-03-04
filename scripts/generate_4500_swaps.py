import os
import requests
import json

# Sovereign Configuration
RPC_URL = 'http://127.0.0.1:8545'
VAULT_ADDR = '0x5FbDB2315678afecb367f032d93F642f64180aa3'
FROM_ADDR = '0x14A3256052c02f9d87FE1Cc3b712D4530061b25c'
# Selector for deposit(uint256,address)
SELECTOR = '0x6e553570'

def dispatch_swaps(count):
    # assets = 100 * 10^18
    assets = '0000000000000000000000000000000000000000000000056bc75e2d63100000'
    # receiver = FROM_ADDR padded
    receiver = '00000000000000000000000014a3256052c02f9d87fe1cc3b712d4530061b25c'
    data = SELECTOR + assets + receiver
    
    for i in range(count):
        payload = {
            'jsonrpc': '2.0',
            'method': 'eth_sendTransaction',
            'params': [{
                'from': FROM_ADDR,
                'to': VAULT_ADDR,
                'data': data,
                'gas': '0x186A0'
            }],
            'id': i
        }
        requests.post(RPC_URL, json=payload)
        if i % 500 == 0:
            print(f'Dispatched {i} / {count} swaps...')

dispatch_swaps(4500)
print('Success: 4,500 ERC-4626 Transactions dispatched.')
