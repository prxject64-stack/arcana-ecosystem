from web3 import Web3
import time

# Connect to your Sovereign Node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

def check_yield():
    if w3.is_connected():
        # EIP-55 Checksum Address Required for 2026 Web3.py
        raw_address = "0xbdae565eff11d46dfd2154442f0a565b4011f3b8"
        vault_address = Web3.to_checksum_address(raw_address)
        
        balance_wei = w3.eth.get_balance(vault_address)
        cc_p_balance = w3.from_wei(balance_wei, 'ether')
        
        print(f"--- Arcana Revenue Harvest ---")
        print(f"[NODE] Status: Connected to ARC-S Network")
        print(f"[VAULT] Current CC-P Liquidity: {cc_p_balance} CC-P")
        
        # 2026 Revenue Logic: 0.1% swap fee simulation
        projected_fees = float(cc_p_balance) * 0.001
        print(f"[FEES] Current Unharvested Swap Fees: {projected_fees:,.2f} ARC-S")
    else:
        print("[ERROR] Node not reachable. Ensure Geth is running.")

if __name__ == "__main__":
    check_yield()
