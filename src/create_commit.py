import boto3

client = boto3.client('codecommit')

def lambda_handler(event, context):
    data = event[0::]
    new_data = data[0][0]
    file_data = data[1]
    commit_data = file_data + new_data
    commit_data_bytes = commit_data.encode('ascii')
    commit_id = event[0][1]

    # Create Commit to CodeCommit repository
    response = client.create_commit(
        repositoryName='aws-deployment-framework-bootstrap',
        branchName='master',
        parentCommitId=commit_id,
        commitMessage='added new account details',
        putFiles=[
            {
                'filePath': 'adf-accounts/account.yml',
                'fileContent': commit_data_bytes
             },
        ]
    )

    return response