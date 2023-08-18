import io
import json
import logging
import mimetypes
import os
import zipfile

import boto3
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

        try:
            self.client.put_bucket_website(
                Bucket=bucket_name,
                WebsiteConfiguration=config,
            )
        except ClientError as err:
            if err.response['Error']['Code'] == 'Something':
