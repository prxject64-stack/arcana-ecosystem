from web3 import Web3

# --- CONFIG ---
RPC_URL = "http://18.221.3.50:8545"
VAULT_ADDR = "0xBf073f0aAA5Fe1C9612bc376158B572E4263cAf9"
AMOUNT_CC = 1000 

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def fund_vault():
    try:
        # Web3 v6 access pattern
        coinbase = w3.eth.coinbase
        if not coinbase:
            print("⚠️ Coinbase not set, trying account[0]...")
            coinbase = w3.eth.accounts[0]
            
        print(f"📡 Source Account: {coinbase}")
        
        cb_bal = w3.from_wei(w3.eth.get_balance(coinbase), 'ether')
        print(f"💰 Source Balance: {cb_bal} CC")
        
        if cb_bal < AMOUNT_CC:
            print(f"❌ Error: Source does not have {AMOUNT_CC} CC.")
            return

        # Sending transaction
        tx_hash = w3.eth.send_transaction({
            'from': coinbase,
            'to': VAULT_ADDR,
            'value': w3.to_wei(AMOUNT_CC, 'ether'),
            'gas': 21000,
            'gasPrice': w3.eth.gas_price
        })
        
        print(f"🚀 Sent! Hash: {tx_hash.hex()}")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"✅ Confirmed! Block: {receipt.blockNumber}")
        print(f"💎 Vault Balance: {w3.from_wei(w3.eth.get_balance(VAULT_ADDR), 'ether')} CC")

    except Exception as e:
        print(f"❌ Operation Failed: {e}")

if __name__ == "__main__":
    fund_vault()
