import time
from web3 import Web3
from eth_account import Account

# Node & Account Setup
# Using your public IP: 18.221.3.50
RPC_URL = "http://18.221.3.50:8545"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Replace this with your actual key for now (Priority 2 will move this to KMS)
private_key = "YOUR_PRIVATE_KEY_HERE" 
account = Account.from_key(private_key)

def get_sauna_gas():
    """Priority 1: Fetches dynamic EIP-1559 gas prices."""
    try:
        latest_block = w3.eth.get_block('latest')
        base_fee = latest_block['baseFeePerGas']
        # Set priority fee (tip) to 2 Gwei
        priority_fee = w3.to_wei(2, 'gwei') 
        # Max fee = (2 * BaseFee) + PriorityFee
        max_fee = (2 * base_fee) + priority_fee
        return max_fee, priority_fee
    except Exception as e:
        print(f"Gas Fetch Error: {e}")
        return w3.to_wei(50, 'gwei'), w3.to_wei(2, 'gwei')

def sync_sauna_nonce():
    """Nonce Manager: Grabs 'pending' count to prevent collisions."""
    return w3.eth.get_transaction_count(account.address, 'pending')

def execute_protected_swap(to_address, amount_cc):
    """Executes swap with Priority 1 & Nonce Guard."""
    max_fee, priority_fee = get_sauna_gas()
    nonce = sync_sauna_nonce()
    
    tx = {
        'chainId': 1, # Update to your specific CC Chain ID
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount_cc, 'ether'),
        'gas': 21000,
        'maxFeePerGas': max_fee,
        'maxPriorityFeePerGas': priority_fee,
    }
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

if __name__ == "__main__":
    print(f"🚀 Sauna Guard Active. Nonce: {sync_sauna_nonce()}")
    # Example: Push a test swap
    # print(f"Tx Hash: {execute_protected_swap('0x...', 0.1)}")
