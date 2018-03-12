import boto3

regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2',
           'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1']

stopped_instances = []
for region in regions:
    ec2_conn = boto3.client('ec2', region_name=region)
    response = ec2_conn.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'stopped':
                stopped_instances.append(instance['InstanceId'])

ec2_con = boto3.client('ec2')
ec2_con.start_instances(InstanceIds=stopped_instances)