import boto3
from web3 import Web3
from eth_account._utils.signing import to_eth_v
from eth_keys.datatypes import Signature
from eth_utils import keccak, to_checksum_address
from pyasn1.codec.der import decoder as der_decoder
from pyasn1.type import univ

# --- CONFIG ---
RPC_URL = "http://18.221.3.50:8545"
KMS_KEY_ID = "423109d3-0e10-436e-91c6-a3f1be424441" 
w3 = Web3(Web3.HTTPProvider(RPC_URL))
kms_client = boto3.client('kms', region_name='us-east-2')

def get_kms_address(key_id):
    """Downloads public key from KMS and converts to ETH address."""
    response = kms_client.get_public_key(KeyId=key_id)
    pub_key_der = response['PublicKey']
    decoded, _ = der_decoder.decode(pub_key_der, asn1Spec=univ.Sequence())
    bit_string = decoded[1]
    raw_pub_bytes = bit_string.asOctets()
    if raw_pub_bytes[0] == 0x04:
        raw_pub_bytes = raw_pub_bytes[1:]
    return to_checksum_address(keccak(raw_pub_bytes)[-20:])

def parse_kms_signature(kms_sig_bytes):
    decoded, _ = der_decoder.decode(kms_sig_bytes, asn1Spec=univ.Sequence())
    r, s = int(decoded[0]), int(decoded[1])
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    if s > n // 2: s = n - s
    return r, s

def get_v(msg_hash, r, s, addr):
    for v in [27, 28]:
        if Signature(vrs=(v, r, s)).recover_public_key_from_msg_hash(msg_hash).to_checksum_address() == addr:
            return v
    raise ValueError("V-Recovery failed.")

if __name__ == "__main__":
    try:
        VAULT_ADDR = get_kms_address(KMS_KEY_ID)
        print(f"✅ Vault Address Derived: {VAULT_ADDR}")
        
        # Priority 1: Dynamic Gas Check
        balance = w3.eth.get_balance(VAULT_ADDR)
        print(f"📊 Vault CC Balance: {w3.from_wei(balance, 'ether')} CC")
        
    except Exception as e:
        print(f"❌ Error: {e}")
