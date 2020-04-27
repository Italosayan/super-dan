import os
import boto3
# Test input requests
role = os.environ.get('ARN_USER')

session = boto3.Session(profile_name='italouser',
                        region_name="eu-west-1")

client = session.client('sagemaker-runtime')

test_data = "1.0,1.0,1.0,1.0"
response = client.invoke_endpoint(
    EndpointName='decision-tree-2020-04-27-17-32-08-246',
    Body=test_data,
    ContentType='text/csv'
)
print(response)
print(response["Body"].read().decode())