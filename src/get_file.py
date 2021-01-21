import json
import boto3

client = boto3.client('codecommit')

def lambda_handler(event, context):
    new_data = event[0::]

    response = client.get_file(
        repositoryName='aws-deployment-framework-bootstrap',
        filePath='adf-accounts/account.yml'
    )

    file_data = response['fileContent'].decode('ascii')

    return new_data, file_data