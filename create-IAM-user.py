import boto3
iam = boto3.client('iam')

# create a user
iam.create_user( UserName='John')

# attach a policy
iam.attach_user_policy(
 UserName = 'John', 
 PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)
