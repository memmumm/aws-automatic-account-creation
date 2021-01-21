import json
import boto3

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Form data
    body = json.loads(event['body'])

    # Enable CORS
    response = {'headers': {'Access-Control-Allow-Origin': '*'}}

    # Start state machine execution
    try:
        sfn_response = client.start_execution(
             stateMachineArn='',    # Add state machine ARN
             input=json.dumps({'body': body})
        )
        # Generate response message for HTML web form submission
        response['statusCode'] = sfn_response['ResponseMetadata']['HTTPStatusCode']
        response['body'] = '{"message": "Success"}'
    except Exception as e:
        print(e)
        response['statusCode'] = 500

    return response