import io
import json
import logging
import mimetypes
import os
import zipfile
from time import time

import boto3
from botocore.exceptions import ClientError

from cicd import PROJECT_ROOT
from cicd.exceptions import BucketAlreadyOwnedByYou

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Boto3Client:
    client = None

    def __init__(self, service_name: str, region_name: str):
        self.client = self._get_boto3_client(service_name, region_name)

    @staticmethod
    def _get_boto3_client(service_name: str, region_name: str):
        client = boto3.client(service_name, region_name)
        return client


class S3Wrapper:

    def __init__(self, client: Boto3Client, region_name: str):
        self.client = client
        self.region = region_name

    def create_bucket(self, bucket_name: str, bucket_configuration: dict) -> None:
        try:
            self.client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=bucket_configuration
            )
        except ClientError as err:
            if err.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                raise BucketAlreadyOwnedByYou(bucket_name=bucket_name)

    def configure_bucket_for_web_hosting(self, bucket_name: str, error_file: str = None):
        logger.info(f'Deleting default public access block for {bucket_name}.')

        self.client.delete_public_access_block(Bucket=bucket_name)

        config = {
            'IndexDocument': {
                'Suffix': 'index.html'
            },
        }

        if error_file:
            config['ErrorDocument'] = error_file

        self.client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration=config,
        )
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
                Bucket=bucket_name,
                Policy=json.dumps(bucket_policy)
            )
            logger.info('Setting bucket ACL')
        except ClientError as e:
            logger.error(f'An error occurred during the configuration of ACL\n{e}')

    def upload_files(self, bucket_name: str, source_dir: str):
        for root, _, files in os.walk(PROJECT_ROOT + source_dir):
            for file in files:
                local_path = os.path.join(root, file)
                s3_path = os.path.relpath(local_path, PROJECT_ROOT + source_dir)

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


class CloudFrontWrapper:

    def __init__(self, cloud_front_client):
        self.cloud_front_client = cloud_front_client

    def invalidate_cache(self, distribution_id):
        try:
            self.cloud_front_client.create_invalidation(
                DistribuitionId=distribution_id,
                InvalidationBatch={
                    'Paths': {
                        'Quantity': 1,
                        'Items': [
                            '/*'
                        ],
                    },
                    'CallerReference': str(time()).replace(".", "")
                }
            )
        except ClientError as e:
            logger.error(f'{e.response["Error"]["Code"]}, {e.response["Error"]["Message"]}')


class LambdaWrapper:

    def __init__(self, client: Boto3Client, iam_resource: str):
        self.client = client
        self.iam_resource = iam_resource

    @staticmethod
    def create_deployment_file(source_dir: str) -> bytes:
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as zipped:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)  # Corrected arcname
                    zipped.write(file_path, arcname=arcname)
        buffer.seek(0)
        return buffer.read()

    def create_function(
            self,
            function_name: str,
            function_description: str,
            handler_name: str,
            deployment_file: bytes
    ):
        try:
            self.client.create_function(
                FunctionName=function_name,
                Description=function_description,
                Runtime='python3.10',
                Role=self.iam_resource.arn,
                Handler=handler_name,
                Code={'ZipFile': deployment_file},
                Publish=True
            )
        except ClientError as e:
            logger.error(f'Could not create function with name {function_name}\n{e}')

    def update_function_code(self, function_name: str, deployment_package: bytes):
        try:
            self.client.update_function_code(
                FunctionName=function_name,
                ZipFile=deployment_package
            )
        except ClientError as e:
            logger.error(f'Could not update function {function_name}\n{e}')

    def get_function(self, function_name: str) -> bool:
        try:
            self.client.get_function(FunctionName=function_name)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                logger.error(f'Function {function_name} does not exist')
            else:
                logger.error(f'{e.response["Error"]["Code"]}\n{e.response["Error"]["Message"]}')
            return False


class ApiGatewayWrapper:

    def __init__(self, api_gateway_client):
        self.api_gateway_client = api_gateway_client

    def create_rest_api(self):
        ...
