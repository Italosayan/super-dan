# S3 prefix
import itertools

prefix = 'DEMO-scikit-byo-iris'

# Define IAM role
import boto3
import sagemaker as sage

import os
import pandas as pd
from sagemaker.predictor import csv_serializer

role = os.environ.get('ARN_USER')

session = boto3.Session(profile_name='italouser',
                        region_name="eu-west-1")
sess = sage.Session(boto_session=session)
WORK_DIRECTORY = 'data'

data_location = sess.upload_data(WORK_DIRECTORY, key_prefix=prefix)

account = sess.boto_session.client('sts').get_caller_identity()['Account']
region = sess.boto_session.region_name
image = '{}.dkr.ecr.{}.amazonaws.com/dtrees:latest'.format(account, region)
tree = sage.estimator.Estimator(image,
                                role, 1, 'ml.c4.2xlarge',
                                output_path="s3://{}/output".format(sess.default_bucket()),
                                sagemaker_session=sess)

tree.fit(data_location)
predictor = tree.deploy(1, 'ml.m4.xlarge', serializer=csv_serializer)

shape = pd.read_csv("data/iris.csv", header=None)
shape.sample(3)
# drop the label column in the training set
shape.drop(shape.columns[[0]], axis=1, inplace=True)
shape.sample(3)

a = [50 * i for i in range(3)]
b = [40 + i for i in range(10)]
indices = [i + j for i, j in itertools.product(a, b)]

test_data = shape.iloc[indices[:-1]]

print(predictor.predict(test_data.values).decode('utf-8'))
