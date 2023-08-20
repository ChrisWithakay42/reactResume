import json
import logging
import mimetypes
import os

from botocore.exceptions import ClientError

from cicd import PROJECT_ROOT
from cicd.exceptions import BucketAlreadyOwnedByYou

logger = logging.getLogger(__name__)


class S3Wrapper:

    def __init__(self, client, region_name: str):
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
        config = {}

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
        logger.info(f'Files successfully uploaded to {bucket_name} bucket.')

