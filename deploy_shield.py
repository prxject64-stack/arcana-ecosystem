from web3 import Web3
from eth_account import Account

# Connection to your node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Deployment Data
priv_key = "fdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2"
account = Account.from_key(priv_key)

# Fetching the real-time state from your Geth node
current_chain_id = w3.eth.chain_id
current_nonce = w3.eth.get_transaction_count(account.address)

print(f"Detected Chain ID: {current_chain_id}")
print(f"Current Nonce: {current_nonce}")
print(f"Deploying from: {account.address}")

# FULL SAUNASHIELD BYTECODE
bytecode = "0x050919050565b61079e81610789565b82525050565b60006080820190506107b9600083018761076b565b6107c6602083018661077a565b6107d3604083018561077a565b6107e06060830184610795565b95945050505050565b60008060408385031215610800576107ff6106d1565b5b600061080e858286016106f7565b925050602061081f858286016106f7565b9150509250929050565b600060208201905061083e600083018461077a565b92915050565b6000819050919050565b600061086961086461085f84610739565b610844565b610739565b9050919050565b600061087b8261084e565b9050919050565b600061088d82610870565b9050919050565b61089d81610882565b82525050565b60006020820190506108b86000830184610894565b92915050565b60006060820190506108d3600083018661076b565b6108e060208"

# Build Transaction
tx = {
    'nonce': current_nonce,
    'gas': 5000000,
    'gasPrice': w3.eth.gas_price if w3.eth.gas_price > 0 else 2000000000,
    'data': bytecode,
    'chainId': current_chain_id
}

# Sign and Send
signed_tx = Account.sign_transaction(tx, priv_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print(f"\n--- SAUNASHIELD BROADCASTED ---")
print(f"Transaction Hash: {tx_hash.hex()}")
print(f"-------------------------------\n")
