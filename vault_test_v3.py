import boto3
from web3 import Web3
from eth_account._utils.signing import extract_chain_id, to_eth_v
from eth_keys.datatypes import Signature
from pyasn1.codec.der import decoder as der_decoder
from pyasn1.type import univ

# --- CONFIGURATION ---
RPC_URL = "http://18.221.3.50:8545"
KMS_KEY_ID = "YOUR_KMS_KEY_ID_HERE"  # Replace with your actual Key ID/ARN
w3 = Web3(Web3.HTTPProvider(RPC_URL))
kms_client = boto3.client('kms', region_name='us-east-1')

def parse_kms_signature(kms_sig_bytes):
    """Unpacks ASN.1 DER into (r, s) and enforces EIP-2 Low-S."""
    decoded, _ = der_decoder.decode(kms_sig_bytes, asn1Spec=univ.Sequence())
    r = int(decoded[0])
    s = int(decoded[1])
    
    # EIP-2: Enforce low-S
    secp256k1_n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    if s > secp256k1_n // 2:
        s = secp256k1_n - s
    return r, s

def get_v_recovery(msg_hash, r, s, expected_addr):
    """Iterates v=27/28 to match the KMS Public Key's address."""
    for v in [27, 28]:
        sig = Signature(vrs=(v, r, s))
        recovered_addr = sig.recover_public_key_from_msg_hash(msg_hash).to_checksum_address()
        if recovered_addr.lower() == expected_addr.lower():
            return v
    raise ValueError("Signature mismatch: Address recovery failed.")

def sign_with_hsm(tx_dict, from_addr):
    """The Core Vault Signer."""
    # 1. Hash the transaction
    unsigned_tx = w3.eth.account.serializable_unsigned_transaction_from_dict(tx_dict)
    tx_hash = unsigned_tx.hash()
    
    # 2. Call AWS KMS
    response = kms_client.sign(
        KeyId=KMS_KEY_ID,
        Message=tx_hash,
        MessageType='DIGEST',
        SigningAlgorithm='ECDSA_SHA_256'
    )
    
    # 3. Parse and Fix Signature
    r, s = parse_kms_signature(response['Signature'])
    v_base = get_v_recovery(tx_hash, r, s, from_addr)
    
    # 4. Final RSV assembly (EIP-155)
    v = to_eth_v(v_base, chain_id=tx_dict['chainId'])
    return unsigned_tx.encode_vrs(v, r, s)

if __name__ == "__main__":
    # STRESS TEST DATA
    TEST_ADDR = "0xYourKmsAddressHere" # UPDATE THIS
    TO_ADDR = "0x..." 
    
    print(f"--- Arcana Vault v3 Active ---")
    try:
        # Example Tx Construction
        tx = {
            'nonce': w3.eth.get_transaction_count(TEST_ADDR),
            'to': TO_ADDR,
            'value': w3.to_wei(0.1, 'ether'),
            'gas': 21000,
            'maxFeePerGas': w3.to_wei(50, 'gwei'),
            'maxPriorityFeePerGas': w3.to_wei(2, 'gwei'),
            'chainId': 1
        }
        signed_raw = sign_with_hsm(tx, TEST_ADDR)
        print(f"✅ Signed Raw Transaction: {signed_raw.hex()}")
    except Exception as e:
        print(f"❌ Operation Failed: {e}")
