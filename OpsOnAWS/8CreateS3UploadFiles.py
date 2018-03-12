import boto3

s3_conn = boto3.client('s3')
response = s3_conn.create_bucket(Bucket='techuser')
response1 = s3_conn.upload_file('C:\\Users\\suman\\MS\\Consultancy\\Python\\test.txt', 'techuser', 'test.txt')

print(response)