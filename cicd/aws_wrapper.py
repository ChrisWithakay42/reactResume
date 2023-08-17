import io
import json
import logging
import mimetypes
import os
import zipfile

import boto3
from botocore.exceptions import ClientError

from cicd import PROJECT_ROOT

logger = logging.getLogger(__name__)


class AwsWrapper:
    def __init__(self, service_name: str, region: str, iam_resource=None):
        self.region = region
        self.client = self.get_client(service_name, self.region)
        if service_name == 'lambda':
            self.iam_resource = iam_resource

    @staticmethod
    def get_client(service_name: str, region: str):
        try:
            client = boto3.client(service_name=service_name, region_name=region)
        except ClientError as e:
            logger.error(f'{e}')
        return client


class BucketWrapper(AwsWrapper):

    def exists(self, bucket_name) -> bool:
        try:
            bucket = self.client.head_bucket(Bucket=bucket_name)
            logger.info(f'Checking if bucket {bucket_name} exists')
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucket':
                logger.error(f'Bucket {bucket_name} does not exist')
                return False
        else:
            if bucket:
                return True

    def create(self, bucket_name: str, delete_default_public_access_block: bool = True):
        bucket_configuration = {
            'LocationConstraint': 'eu-west-2',
        }
        try:
            self.client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=bucket_configuration
            )
        except ClientError as e:
            logger.error(f'An error occurred\n{e}')
        if delete_default_public_access_block:
            logger.info('Deleting default public access configuration')
            self.client.delete_public_access_block(
                Bucket=bucket_name,
            )

    def configure_web_hosting(self, bucket_name: str, index_file: str, error_file: str = None):
        bucket_website_configuration = {
            'IndexDocument': {'Suffix': index_file},
            # 'ErrorDocument': {'Key': error_file}
        }
        try:
            self.client.put_bucket_website(
                Bucket=bucket_name,
                WebsiteConfiguration=bucket_website_configuration
            )
        except ClientError as e:
            logger.error(f'An error occurred while configuring bucket for static web hosting\n{e}')

    def upload_files(self, bucket_name):
        source_directory = '/frontend/dist'
        for root, _, files in os.walk(PROJECT_ROOT + source_directory):
            for file in files:
                local_path = os.path.join(root, file)
                s3_path = os.path.relpath(local_path, PROJECT_ROOT + source_directory)

                mime_type, _ = mimetypes.guess_type(local_path)

                metadata = {
                    'ContentType': mime_type,
                    'ContentDisposition': 'inline',
                }

                try:
                    self.client.upload_file(local_path, bucket_name, s3_path, ExtraArgs=metadata)
                    logger.info(f'Uploading {file} to {s3_path}...')
                except ClientError as e:
                    logger.error(f'An error occurred. Check logs for further details \n{e}')
        logger.info(f'Files successfully uploaded to {bucket_name} bucket.')

    def set_acl(self, bucket_name):
        bucket_policy = {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': f'arn:aws:s3:::{bucket_name}/*'
            }]
        }
        try:
            self.client.put_bucket_policy(
                Bucket='codewithakay.com',
                Policy=json.dumps(bucket_policy)
            )
            logger.info('Setting bucket ACL')
        except ClientError as e:
            logger.error(f'An error occurred during the configuration of ACL\n{e}')


class LambdaWrapper(AwsWrapper):

    @staticmethod
    def create_deployment_package(source_dir: str) -> bytes:
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zipped:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipped.write(file_path, arcname)
        buffer.seek(0)
        return buffer.read()

    def create(self, function_name, handler_name, iam_role, deployment_package):
        try:
            response = self.client.create_function(
                FunctionName=function_name,
                Description='Flask Mail server for codewithakay.com',
                Runtime='python3.10',
                Role=iam_role,
                Handler=handler_name,
                Code={'ZipFile': deployment_package},
                Publish=True)
            logger.info(f'Created function {function_name}')
        except ClientError as e:
            logger.error(f'Could not create function {function_name}.\n{e}')
        else:
            function_arn = response['FunctionArn']
            # waiter = self.client.get_waiter('function_active_v2')
            # waiter.wait(FunctionName=function_name)
            return function_arn

    def update_function_code(self, function_name, deployment_package):
        try:
            response = self.client.update_function_code(
                FunctionName=function_name,
                ZipFile=deployment_package
            )
        except ClientError as err:
            logger.error(
                f'Could not update function code! See errors below'
                f'{err["Error"]["Code"]}\n{err["Error"]["Message"]}'
            )
        else:
            return response

    def update_function_configuration(self):
        ...
