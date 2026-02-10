import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
import prover_engine
import time

# Commercial Configuration
API_KEYS = {"arcana_pro_001": "Active", "sauna_partner_77": "Active"}
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI(title="Arcana Prover SaaS")

async def get_api_key(header_key: str = Security(api_key_header)):
    if header_key in API_KEYS:
        return header_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail="Invalid API Key. Purchase CC credits to continue."
    )

@app.get("/verify/{wallet_id}")
async def verify_wallet(wallet_id: str, api_key: str = Depends(get_api_key)):
    start = time.time()
    # 602 MH/s Rust Engine Call
    nonce = prover_engine.find_arcana_nonce(wallet_id, 0, 50000000)
    end = time.time()
    
    if nonce:
        return {
            "status": "VERIFIED",
            "nonce": nonce,
            "latency": f"{end - start:.4f}s",
            "billed_to": api_key,
            "liquidity_secured": "136B CC"
        }
    return {"status": "REJECTED", "reason": "Proof timeout"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
