import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def create_bucket(*, bucket_name):
    try:
        client = boto3.resource('s3')
    except ClientError as e:
        logger.error(e)
        return False
    else:
        client.create_bucket(
            Bucket=bucket_name,
            BucketConfiguration={
                'LocationConstraint': os.getenv('AWS_REGION')
            }
        )
    return True
