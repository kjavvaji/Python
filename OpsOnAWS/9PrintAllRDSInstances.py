import boto3

regions = ['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2',
           'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1',
           'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1']


def print_rds_instances(response):
    for db_instance in response['DBInstances']:
        print(db_instance['DBInstanceIdentifier'])


for region in regions:
    rds_conn = boto3.client('rds', region_name=region)
    print_rds_instances(rds_conn.describe_db_instances())