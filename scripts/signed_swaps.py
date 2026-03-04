import time
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# Master Signer info
FROM_ADDR = '0x14A3256052c02f9d87FE1Cc3b712D4530061b25c'
PRIV_KEY = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
VAULT_ADDR = '0x5FbDB2315678afecb367f032d93F642f64180aa3'

# deposit(uint256,address)
SELECTOR = '0x6e553570'
assets = '0000000000000000000000000000000000000000000000056bc75e2d63100000' # 100
receiver = '00000000000000000000000014a3256052c02f9d87fe1cc3b712d4530061b25c'
data = SELECTOR + assets + receiver

nonce = w3.eth.get_transaction_count(FROM_ADDR)

for i in range(4500):
    tx = {
        'nonce': nonce + i,
        'to': VAULT_ADDR,
        'data': data,
        'gas': 100000,
        'gasPrice': w3.to_wei('1', 'gwei'),
        'chainId': 31337
    }
    signed_tx = w3.eth.account.sign_transaction(tx, PRIV_KEY)
    w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    if i % 500 == 0:
        print(f'Sent {i} signed swaps...')

print('4500 Signed Swaps Dispatched.')
