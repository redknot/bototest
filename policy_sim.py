import boto3
import sys

from botocore.config import Config

my_config = Config(
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

iam = boto3.client('iam',config=my_config)

print("Checking secret: {0}".format(sys.argv[1]))

for role in iam.list_roles(MaxItems=999)['Roles']:
	response = iam.simulate_principal_policy(
		PolicySourceArn=role['Arn'],
		ActionNames=['secretsmanager:*'],
		ResourceArns=[sys.argv[1]]
	)
	if(response['EvaluationResults'][0]['EvalDecision'] == 'allowed'):
		print("Role: {0} EvalDecision: {1}".format(role['RoleName'],response['EvaluationResults'][0]['EvalDecision']))