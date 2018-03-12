import boto3

ec2_conn = boto3.client('ec2', region_name='us-east-1')

monitoring = {'Enabled': False}
resp = ec2_conn.run_instances(ImageId='ami-97785bed', InstanceType='t2.micro', MaxCount=1, MinCount=1, Monitoring=monitoring)

instanceId = []
for instance in resp['Instances']:
    instanceId.append(instance['InstanceId'])

while True:
    resp_status = ec2_conn.describe_instance_status(InstanceIds=instanceId)
    for inst_status in resp_status['InstanceStatuses']:
        if inst_status['InstanceState']['Name'] == 'running':
            exit()
