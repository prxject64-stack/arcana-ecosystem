from web3 import Web3
import json

# Connect to your local Arcana Node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# PRO MODE: Hardcoded CC Address (The 136B CC token contract)
# Replace this with your actual CC token address
cc_token_address = "0xBdae565eff11d46dfD2154442f0a565B4011F3b8" 

# Load ABI and BIN
with open('build/ArcanaBridgeL1.abi', 'r') as f:
    abi = json.load(f)
with open('build/ArcanaBridgeL1.bin', 'r') as f:
    bytecode = f.read()

# Setup Contract
Bridge = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get Account (God Wallet)
account = w3.eth.accounts[0]

print(f"Deploying Bridge from: {account}")

# Build Transaction
tx_hash = Bridge.constructor(cc_token_address).transact({'from': account, 'gas': 2000000, 'gasPrice': w3.to_wei('1', 'gwei')})

# Wait for Receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Bridge Deployed at: {tx_receipt.contractAddress}")
