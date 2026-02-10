import requests

def get_arcana_proof(wallet_address):
    # Your Cloudflare Gateway
    url = "https://declare-cartridges-request-trek.trycloudflare.com/verify/" + wallet_address
    headers = {"X-API-Key": "arcana_pro_001"} # Using your active key
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Simulate a buyer checking a wallet
    print(get_arcana_proof("0x11dB4806a640989fA44874051DFA4889c09534B4"))
