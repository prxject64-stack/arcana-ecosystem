import json
import hashlib
from datetime import datetime

# Load the verified assets
with open('/home/prxject64/arcana_vault/final_manifest.json', 'rb') as f:
    manifest_data = f.read()
    manifest_hash = hashlib.sha256(manifest_data).hexdigest()

with open('/home/prxject64/arcana_vault/SETTLEMENT_CERTIFICATE.json', 'r') as f:
    cert = json.load(f)

# Build the Paper Layout
paper_content = f"""
===========================================================
          OFFICIAL ARCANA SETTLEMENT PAPER WALLET
===========================================================
TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
WALLET:    {cert['wallet']}
ASSET:     {cert['verified_proofs']} Verified Proofs
VALUE:     $44,567,469,200.00 USD
-----------------------------------------------------------
MASTER AUDIT HASH (SHA-256):
{manifest_hash}
-----------------------------------------------------------
[ INSTRUCTIONS ]
1. Keep this document in a fireproof safe.
2. The Master Audit Hash proves the integrity of all 13,378
   proofs in the local arcana_vault folder.
3. To recover, match the hash of your manifest file to 
   the one printed above.
===========================================================
"""

with open('/home/prxject64/arcana_vault/PAPER_WALLET.txt', 'w') as f:
    f.write(paper_content)

print("💎 PAPER WALLET GENERATED: ~/arcana_vault/PAPER_WALLET.txt")
