import json

def lambda_handler(event, context):
    
    print('Hey man! I created Lambda function for the first time!!')
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    