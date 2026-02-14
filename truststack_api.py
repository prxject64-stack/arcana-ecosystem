from fastapi import FastAPI, HTTPException
import asyncio
import datetime
import json

app = FastAPI(title="TrustStack AI Core")

@app.get("/quickcheck/{wallet_address}")
async def quick_check(wallet_address: str, required_cc: int = 1000):
    try:
        proc = await asyncio.create_subprocess_exec(
            'miner', '!verify', '--address', wallet_address,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, _ = await proc.communicate()
        is_verified = str(required_cc) in stdout.decode()
        status = "VERIFIED" if is_verified else "REJECTED"
        
        log_entry = {"timestamp": datetime.datetime.utcnow().isoformat(), "wallet": wallet_address, "status": status}
        with open("audit_log.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        return {"status": status, "wallet": wallet_address, "timestamp": log_entry["timestamp"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
