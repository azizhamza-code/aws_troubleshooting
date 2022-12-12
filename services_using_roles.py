import boto3
import json

iam_client = boto3.client('iam')


response = iam_client.list_attached_role_policies(
    RoleName='AWSServiceRoleForApplicationAutoScaling_DynamoDBTable'
)

policies = response['AttachedPolicies']

for policy in policies:
    policy_arn = policy['PolicyArn']
    response = iam_client.get_policy(PolicyArn=policy_arn)
    policy_version = iam_client.get_policy_version(
    PolicyArn = policy_arn, 
    VersionId = response['Policy']['DefaultVersionId']
)
# Get the policy document
    print(policy_version )
    policy_document = policy_version['Policy']['PolicyDocument']

    # Parse the policy document to get the list of allowed services
    allowed_services = []
    for statement in policy_document['Statement']:
        if statement['Effect'] == 'Allow':
            for action in statement['Action']:
                service_name = action.split(':')[0]
                allowed_services.append(service_name)

    # Print the list of allowed services
    print(allowed_services)







    