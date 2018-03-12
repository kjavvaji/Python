import boto3

ec2_conn = boto3.client('ec2', region_name='us-east-1')
response = ec2_conn.describe_instances(InstanceIds=['i-01d99b0bea4f7634a'])

volumeId = ''
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for blockdevice in instance['BlockDeviceMappings']:
            volumeId = blockdevice['Ebs']['VolumeId']

snapshot = ec2_conn.create_snapshot(VolumeId=volumeId)
if snapshot:
    print("Snapshot created for volumeid," + volumeId)
else:
    print("*****Error*****")