import json
import logging
import os
from typing import Callable

import boto3
from botocore.exceptions import ClientError

from cicd import PROJECT_ROOT

logger = logging.getLogger(__name__)


class S3Manager:
    _s3_client = None

    def __init__(self):
        self._s3_client = self._get_s3_client()

    @staticmethod
    def _get_s3_client():
        try:
            client = boto3.client('s3')
        except ClientError as e:
            logger.error(f'There was an error connection to AWS services\n{e}')
        return client

    def get_or_create_bucket(self, bucket_name: str, region: str) -> tuple:
        location = {'LocationConstraint': region}
        try:
            logger.info(f'Checking if bucket with name {bucket_name} exists')
            bucket = self._s3_client.head_bucket(Bucket=bucket_name)
            return bucket, False  # If we find the bucket, we assume its configuration is already set
        except self._s3_client.exceptions.NoSuchBucket as e:
            logger.info(
                f'The bucket named: "{bucket_name}" does not exist or you do not have permission to access it!'
                f'See error below for more details'
                f'{e}'
                f'Creating new bucket {bucket_name}'
            )
            bucket = self._s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
            return bucket, True

    def configure_bucket_for_web_hosting(
            self,
            bucket_name: str,
            index_document: str = 'index.html',
            error_document: str = None
    ):
        website_configuration = {
            'IndexDocument': {'Suffix': index_document},
            'ErrorDocument': {'Key': error_document}
        }
        self._s3_client.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

        # Set the bucket policy to make objects publicly readable
        bucket_policy = {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': f'arn:aws:s3:::{bucket_name}/*'
            }]
        }
        self._s3_client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))

        logger.info(
            f'Configured bucket {bucket_name} for web hosting with index document: {index_document}, error document: '
            f'{error_document}, and public read ACL'
        )

    def deploy_to_bucket(self, bucket_name: str, source_directory: str = '/frontend/dist'):
        for root, _, files in os.walk(PROJECT_ROOT + source_directory):
            for file in files:
                local_path = os.path.join(root, file)
                s3_path = os.path.join(local_path, source_directory)
                try:
                    self._s3_client.upload_file(local_path, bucket_name, s3_path)
                except ClientError as e:
                    logger.error(f'An error occurred. Check logs for further details \n{e}')
        logger.info(f'Files successfully uploaded to {bucket_name} bucket.')

