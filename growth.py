from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import boto3
import uvicorn

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('TrustStack_Clients')

@app.get("/leaderboard")
@limiter.limit("5/minute")
async def get_leaderboard(request: Request):
    response = table.scan()
    items = response.get('Items', [])
    referral_map = {}
    for item in items:
        ref = item.get('referred_by')
        if ref:
            referral_map[ref] = referral_map.get(ref, 0) + 1
    sorted_leaders = sorted(referral_map.items(), key=lambda x: x[1], reverse=True)
    return {
        "top_referrers": [
            {"client_id": k, "referrals": v, "reward_eligible": v * 500} 
            for k, v in sorted_leaders[:10]
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)
