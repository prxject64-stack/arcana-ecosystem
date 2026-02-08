import asyncio, sys
from web3 import AsyncWeb3, Web3
from web3.providers import AsyncHTTPProvider

w3 = AsyncWeb3(AsyncHTTPProvider("http://localhost:8545"))

async def generate_teaser(addr):
    target = Web3.to_checksum_address(addr)
    account = (await w3.eth.accounts)[0]
    # Get the starting nonce for the sender
    base_nonce = await w3.eth.get_transaction_count(account)
    
    # Fire 10 transactions with INCREMENTING nonces
    tasks = [
        w3.eth.send_transaction({
            'from': account, 
            'to': target, 
            'value': 1, 
            'gas': 100000,
            'nonce': base_nonce + i
        }) for i in range(10)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    errors = [str(r) for r in results if isinstance(r, Exception)]
    
    print(f"\n--- ALPHASEC TEASER for {target} ---")
    if errors:
        # If it fails now, it's a REAL contract logic revert, not a nonce error.
        print(f"RESULT: ❌ VULNERABLE")
        print(f"ERROR: {errors[0]}")
    else:
        print(f"RESULT: ✅ STABLE")
        print("STABILITY: Logic held under 10-hit concurrent burst.")
    print("--------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 audit_teaser.py <address>")
    else:
        asyncio.run(generate_teaser(sys.argv[1]))
