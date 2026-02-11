import boto3
from eth_signer.signer import AWSKMSKey
from web3 import Web3
import os

# Node & Vault Setup
RPC_URL = "http://18.221.3.50:8545"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Priority 2: Initialize the Vault
# Replace 'YOUR_KMS_KEY_ID_HERE' with the actual ID once you create it in Console
kms_client = boto3.client('kms', region_name='us-east-1') 
key_id = "YOUR_KMS_KEY_ID_HERE" 

try:
    vault_account = AWSKMSKey(kms_client, key_id)
    print(f"✅ Vault Active. Treasury Address: {vault_account.address}")
except Exception as e:
    print(f"❌ Vault Error: {e}")

def execute_vault_swap(to_address, amount_cc):
    """Signs via AWS HSM without ever touching a private key."""
    # Priority 1: Dynamic Gas Implementation
    latest_block = w3.eth.get_block('latest')
    base_fee = latest_block['baseFeePerGas']
    priority_fee = w3.to_wei(2, 'gwei')
    max_fee = (2 * base_fee) + priority_fee
    
    # Nonce Manager logic
    nonce = w3.eth.get_transaction_count(vault_account.address, 'pending')
    
    tx = {
        'chainId': 1,
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount_cc, 'ether'),
        'gas': 21000,
        'maxFeePerGas': max_fee,
        'maxPriorityFeePerGas': priority_fee,
        'from': vault_account.address
    }
    
    signed_tx = vault_account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

if __name__ == "__main__":
    # This will fail until you put a real Key ID in the variable above
    print("Sauna Vault Manager initialized.")
