# from prefect.filesystems import S3
# from prefect_aws import AwsCredentials
# import os
# from prefect.filesystems import GitHub

# s3_bucket = S3(
#         bucket_path='s3-bucket',
#         basepath='rend-prefect-s3',
#         aws_credentials=AwsCredentials(
#                                         aws_access_key_id=os.getenv('aws_access_key_id'),
#                                         aws_secret_access_key=os.getenv('aws_secret_access_key'))
#     )
# s3_bucket.save(name='s3-bucket', overwrite=True)

# github_storage = GitHub(reference='main',repository=os.getenv('GITHUB_REPOSITORY'))
# github_storage.save(name='github',overwrite=True)

# define and update required blocks here

import os
from prefect.blocks.system import Secret,String

cme_api_password = Secret(value=os.getenv('cme_api_password'.upper()))
cme_api_password.save(name="cme-api-password",overwrite=True)

# Secret(value=os.getenv('curves-api-token')).save(name="curves-api-token",overwrite=True)
# Secret(value=os.getenv('db-password')).save(name="db-password",overwrite=True)
# Secret(value=os.getenv('eex-api-password')).save(name="eex-api-password",overwrite=True)
# Secret(value=os.getenv('entsoe-api-key')).save(name="entsoe-api-key",overwrite=True)
# Secret(value=os.getenv('greenfact-client-id')).save(name="greenfact-client-id",overwrite=True)
# Secret(value=os.getenv('greenfact-client-secret')).save(name="greenfact-client-secret",overwrite=True)
# Secret(value=os.getenv('greenfact-portal-user-password')).save(name="greenfact-portal-user-password",overwrite=True)
# Secret(value=os.getenv('ice-mft-pem-content')).save(name="ice-mft-pem-content",overwrite=True)
# Secret(value=os.getenv('ice-mft-sftp-hostname')).save(name="ice-mft-sftp-hostname",overwrite=True)
# Secret(value=os.getenv('ice-mft-sftp-username')).save(name="ice-mft-sftp-username",overwrite=True)
# Secret(value=os.getenv('ice-trading-mft-pem-content')).save(name="ice-trading-mft-pem-content",overwrite=True)
# Secret(value=os.getenv('supabase-db-non-curve-password')).save(name="supabase-db-non-curve-password",overwrite=True)
# Secret(value=os.getenv('supabase-db-non-curve-user')).save(name="supabase-db-non-curve-user",overwrite=True)
# Secret(value=os.getenv('supabase-db-reference-id')).save(name="supabase-db-reference-id",overwrite=True)
# Secret(value=os.getenv('greenfact-client-id')).save(name="greenfact-client-id",overwrite=True)

dataflowopstest = String(value='dataflowopstest')
dataflowopstest.save(name="dataflowopstest",overwrite=True)

s2 = String(value='flavio@greenfact.com')
s2.save(name="greenfact-portal-user",overwrite=True)
s3 = String(value='PR')
s3.save(name="pr-deployment-name",overwrite=True)


