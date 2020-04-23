import os
import boto3

role = os.environ.get('ARN_USER')

session = boto3.Session(profile_name='italouser',
                        region_name="eu-west-1")

client = session.client('sagemaker-runtime',)

test_data = "1.5,16.0,14,23.0"
response = client.invoke_endpoint(
    EndpointName='dtrees-2020-04-23-17-10-14-683',
    Body=test_data,
    ContentType='text/csv'
)
print(response)
print(dir(response))
print(response["Body"].read().decode())