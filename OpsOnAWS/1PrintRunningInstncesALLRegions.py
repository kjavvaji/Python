import boto3

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2',
           'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1']


def print_instance_details(response):
    for item in response["Reservations"]:
        #print(response["Reservations"])
        for instance in item["Instances"]:
            if instance['State']['Name'] == 'running':
                print('{:50s}'.format(instance["PublicDnsName"]), end=': ')
                print('{:20s}'.format(instance["PublicIpAddress"]), end='   ')
                print(instance["Placement"]["AvailabilityZone"])
                print("---------------------------------------------------------------------------------------")
            #else:
               # print('No Running Instances')

for region in regions:
    ec2_conn = boto3.client('ec2', region_name=region)
    #print(ec2_conn.describe_instances())
    print_instance_details(ec2_conn.describe_instances())

