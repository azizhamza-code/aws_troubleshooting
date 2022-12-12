import boto3
import json
# Create an IAM client
iam_client = boto3.client('iam')

# List the policies that are attached to the role
response = iam_client.list_attached_role_policies(
    RoleName='AWSServiceRoleForApplicationAutoScaling_DynamoDBTable'
)

# For each policy, get the default version and list the services that are using the role
for policy in response['AttachedPolicies']:
    # Get the default version of the policy
    policy_response = iam_client.get_policy(
        PolicyArn=policy['PolicyArn']
    )
    default_version_id = policy_response['Policy']['DefaultVersionId']

    # List the services that are using the role through the policy
    entities_response = iam_client.list_entities_for_policy(
        PolicyArn=policy['PolicyArn'],
        #PolicyVersionId=default_version_id
    )
    print(json.dumps(entities_response , indent=2))

    # Print the names of the services that are using the role
# Print the names of the services that are using the role
    for entity in entities_response['PolicyRoles']:
        # Check if the entity is a policy role
        if 'PolicyRole' in entity:
            for service_name in entity['PolicyRole']['ServiceNames']:
                print(service_name)

