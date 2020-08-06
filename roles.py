import boto3
iam = boto3.client('iam')

for role in iam.list_roles(MaxItems=999)['Roles']:
	print("RoleName: {0}\nRoleId: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
		role['RoleName'],
		role['RoleId'],
		role['Arn'],
		role['CreateDate']
 		)
 	)