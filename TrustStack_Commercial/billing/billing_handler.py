import json
import boto3
import secrets

client = boto3.client('apigateway')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TrustStack_Clients')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        
        if body.get('type') == 'checkout.session.completed':
            customer_email = body['data']['object']['customer_details']['email']
            new_key = f"TSAI-{secrets.token_hex(16)}"
            
            # Register in API Gateway
            client.create_api_key(
                name=f"Key-for-{customer_email}",
                enabled=True,
                value=new_key
            )
            
            # Record in DynamoDB
            table.put_item(Item={
                'client_id': customer_email,
                'api_key': new_key,
                'plan': 'Sovereign',
                'status': 'ACTIVE'
            })
            
            print(f"SUCCESS: Provisioned key for {customer_email}")
            
        return {'statusCode': 200, 'body': 'Webhook Processed'}
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {'statusCode': 500, 'body': 'Internal Error'}
