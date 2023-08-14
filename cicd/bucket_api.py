import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class S3Manager:
    _s3_client = None

    def __init__(self):
        self.client = self._get_s3_client()

    @staticmethod
    def _get_s3_client():
        try:
            client = boto3.client('s3')
        except ClientError as e:
            logger.error(f'There was an error connection to AWS services\n{e}')
        return client

    def get_or_create_bucket(self, bucket_name):
        try:
            self.client.head_bucket(bucket_name)
            return True
        except ClientError as e:
            if int(e.response['Error']['Code']) >= 400:
                logger.error(
                    f'The bucket named: "{bucket_name}" does not exist or you do not have permission to access it!\n{e}'
                )
            return False

    def configure_bucket(self):
        ...

    def deploy_to_bucket(self):
        ...
