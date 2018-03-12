import boto3

"""regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2',
           'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1']"""
regions = ['us-east-1']
Instances = []
exception_list = ['i-01d99b0bea4f7634a']
for region in regions:
    ec2_conn = boto3.client('ec2', region_name=region)
    response_Instance_details = ec2_conn.describe_instances()
    for reservation in response_Instance_details["Reservations"]:
        for instance in reservation["Instances"]:
            Instances.append(instance['InstanceId'])
    response = ec2_conn.terminate_instances(InstanceIds=list(set(Instances)-set(exception_list)))

if response:
    print("All instances terminated")
else:
    print("-----Error-----")