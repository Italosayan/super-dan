import os
import boto3
# Test input requests
role = os.environ.get('ARN_USER')

session = boto3.Session(profile_name='italouser',
                        region_name="eu-west-1")

client = session.client('sagemaker-runtime')

test_data = "10.0,2.0,34.0,5.0"
response = client.invoke_endpoint(
    EndpointName='test-algo-2020-04-28-07-47-07-645',
    Body=test_data,
    ContentType='text/csv'
)
print(response)
print(response["Body"].read().decode())