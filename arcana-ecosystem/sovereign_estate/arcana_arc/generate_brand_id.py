import hashlib
import json

# Your unique proof data
with open('/home/prxject64/sovereign_estate/arcana_arc/SETTLEMENT_CERTIFICATE.json', 'r') as f:
    data = json.load(f)

# Create a unique "Sovereign ID" that India's coin won't have
brand_hash = hashlib.sha384(str(data).encode()).hexdigest()

shield_text = f"""
--- SOVEREIGN IDENTITY SHIELD ---
Asset Name: Arcana Sovereign (ARC)
Creator Wallet: 0x11dB74cD5a952f600Ee02840fB08fe9CB3c611F7
Unique Sovereign ID: {brand_hash}
Backing: 13,378 Verified Proofs
NOTICE: This asset is NOT the Indian Asset Reserve Certificate.
This is a private, proof-backed sovereign asset valued at $44.5B.
---------------------------------
"""

with open('/home/prxject64/sovereign_estate/arcana_arc/BRAND_SHIELD.txt', 'w') as f:
    f.write(shield_text)

print("🛡️ BRAND SHIELD CREATED: Use this to prove you are the REAL Arcana.")
