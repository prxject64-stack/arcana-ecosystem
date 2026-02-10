from fastapi import FastAPI
import boto3
import uuid

app = FastAPI()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('TrustStack_Clients')

@app.post("/join")
async def onboard_customer():
    client_id = f"ARC-{uuid.uuid4().hex[:8].upper()}"
    table.put_item(
        Item={
            'client_id': client_id,
            'balance': 1000,
            'status': 'ACTIVE'
        }
    )
    return {"client_id": client_id, "bonus": "1000 CC"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
