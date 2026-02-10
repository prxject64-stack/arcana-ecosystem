import requests
import time

# NEW GLOBAL URL
NODE_URL = "https://declare-cartridges-request-trek.trycloudflare.com"
API_KEY = "arcana_pro_001"

def request_proof(wallet_address):
    print(f"--- Global Request for {wallet_address} ---")
    headers = {
        "X-API-Key": API_KEY,
        "bypass-tunnel-reminder": "true" 
    }
    
    try:
        start = time.time()
        response = requests.get(f"{NODE_URL}/verify/{wallet_address}", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"SUCCESS: Nonce {data['nonce']} found in {data['latency']}")
            print(f"SECURED: {data['liquidity_secured']}")
        else:
            print(f"FAILED: Status {response.status_code}")
            print(f"RESPONSE: {response.text[:100]}")
            
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")

if __name__ == "__main__":
    request_proof("0x11dB4806a640989fA44874051DFA4889c09534B4")
