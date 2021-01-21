import boto3

client = boto3.client('codecommit')

def lambda_handler(event, context):
    # Parse form data from "name" field to alias for configuration file
    alias_data = event['body'][0]['name']
    alias = ' '.join(alias_data.split()).replace(' ', '-').replace('---', '-').lower()

    # Parse form data as content for configuration file
    data = '\n  - account_full_name: %s\n    organizational_unit_path: /\n    email: %s\n    allow_billing: True\n    delete_default_vpc: True\n    alias: %s\n    tags:\n      - networkType: %s\n ' % (event['body'][0]['name'], event['body'][0]['email'], alias, event['body'][0]['network'])

    # Get branch information from CodeCommit repository
    parent_commit_id_value = client.get_branch(
        repositoryName='aws-deployment-framework-bootstrap',
        branchName='master'
    )

    # Parse parent commit id value from branch information
    id = parent_commit_id_value['branch']['commitId']

    return data, id