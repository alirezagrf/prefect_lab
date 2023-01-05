from prefect_aws.s3 import S3Bucket
from prefect_aws import AwsCredentials
import os
from prefect.filesystems import GitHub

s3_bucket = S3Bucket(
        bucket_name='s3-bucket',
        basepath='rend-prefect-s3',
        aws_credentials=AwsCredentials(
                                        aws_access_key_id=os.getenv('aws_access_key_id'),
                                        aws_secret_access_key=os.getenv('aws_secret_access_key'))
    )
s3_bucket.save(name='s3-bucket', overwrite=True)

github_storage = GitHub(reference='main',repository=os.getenv('GITHUB_REPOSITORY'))
github_storage.save(name='github',overwrite=True)