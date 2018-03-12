import boto3

ec2_conn = boto3.client('ec2')
response = ec2_conn.create_image(InstanceId='i-01d99b0bea4f7634a', Name='ami-newsnap')

print(response['ImageId'])