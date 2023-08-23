import logging
import os

import boto3

from cicd.aws_wrapper import S3Wrapper
from cicd.exceptions import BucketAlreadyOwnedByYou

logger = logging.getLogger(__name__)


def main(bucket_name: str):
    region_name = 'eu-west-2'
    client = boto3.client('s3', region_name=region_name)
    s3_wrapper = S3Wrapper(client=client, region_name=region_name)
    location_configuration = {
        'LocationConstraint': 'eu-west-2'
    }
    try:
        s3_wrapper.create_bucket(bucket_name=bucket_name, bucket_configuration=location_configuration)
    except BucketAlreadyOwnedByYou:
        s3_wrapper.upload_files(bucket_name=bucket_name, source_dir='/frontend/dist')
    else:
        s3_wrapper.configure_bucket_for_web_hosting(bucket_name=bucket_name)
        s3_wrapper.upload_files(bucket_name=bucket_name, source_dir='/frontend/dist')


if __name__ == '__main__':
    main(bucket_name='codewithakay.com')
