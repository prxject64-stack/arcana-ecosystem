import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import hashlib

def generate_wallet():
    # 1. Generate RSA Private Key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    # 2. Derive Public Key
    public_key = private_key.public_key()
    
    # 3. Create a short 'Address' using SHA-256 (The openssl dgst -sha256 logic)
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    address = hashlib.sha256(public_bytes).hexdigest()[:40]
    
    # 4. Save the Private Key (DO NOT SHARE THIS)
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    
    print("====================================================")
    print("          ARCANA SOVEREIGN WALLET CREATED           ")
    print("====================================================")
    print(f"YOUR ADDRESS: arcana_{address}")
    print("PRIVATE KEY SAVED TO: private_key.pem")
    print("Keep your private key safe. It is your 12D signature.")
    print("====================================================")

if __name__ == "__main__":
    generate_wallet()
