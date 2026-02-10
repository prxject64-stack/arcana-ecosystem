import sys
import asyncio
import re
from web3 import Web3

async def generate_teaser(raw_addr):
    # Pro-mode sanitation: Keep ONLY hex digits and 'x'
    clean_addr = re.sub(r'[^0-9a-fA-Fx]', '', str(raw_addr))
    
    # Validation: Must be 42 chars (0x + 40 hex)
    if not clean_addr.startswith('0x') or len(clean_addr) != 42:
        print(f"ERROR: Invalid Address Format [{clean_addr}]")
        return

    target = Web3.to_checksum_address(clean_addr)
    print(f"--- ALPHASEC TEASER for {target} ---")
    print("RESULT: ✅ READY FOR SCAN")
    print("STABILITY: Logic baseline initialized.")
    print("--------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(generate_teaser(sys.argv[1]))
    else:
        print("Usage: python3 audit_teaser.py <address>")
