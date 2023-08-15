import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

from cicd import PROJECT_ROOT

logger = logging.getLogger(__name__)


def get_client():
    try:
        client = boto3.client('s3')
    except ClientError as e:
        logger.error(f'{e}')
    return client


def get_bucket(client, bucket_name) -> bool:
    try:
        bucket = client.head_bucket(Bucket=bucket_name)
    except ClientError:
        return False
    else:
        if bucket:
            return True


def create_bucket(client, bucket_name: str):
    bucket_configuration = {
        'LocationConstraint': 'eu-west-2',
    }
    client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration=bucket_configuration
    )
    logger.info(f'Configured bucket for web hosting with a read only ACL Policy')

    client.delete_public_access_block(
        Bucket=bucket_name,
    )


def configure_web_hosting(client, bucket_name: str, index_file: str, error_file: str = None):
    bucket_website_configuration = {
        'IndexDocument': {'Suffix': index_file},
        # 'ErrorDocument': {'Key': error_file}
    }
    client.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration=bucket_website_configuration
    )


def deploy_files(client, bucket_name):
    source_directory = '/frontend/dist'
    for root, _, files in os.walk(PROJECT_ROOT + source_directory):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = os.path.relpath(local_path, PROJECT_ROOT + source_directory)
            extra_args = {
                'ContentType': 'text/html',  # Set the Content-Type header
                'ContentDisposition': 'inline',  # Set the Content-Disposition header
            }
            try:
                client.upload_file(local_path, bucket_name, s3_path, ExtraArgs=extra_args)
                logger.info(f'Uploading {file} to {s3_path}...')
            except ClientError as e:
                logger.error(f'An error occurred. Check logs for further details \n{e}')
    logger.info(f'Files successfully uploaded to {bucket_name} bucket.')


def set_bucket_acl(client, bucket_name):
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
        client.put_bucket_policy(
            Bucket='codewithakay.com',
            Policy=json.dumps(bucket_policy)
        )
    except ClientError as e:
        logger.error(f'{e}')


def main(bucket_name: str):
    client = get_client()
    bucket = get_bucket(client, bucket_name=bucket_name)
    if not bucket:
        create_bucket(client, bucket_name=bucket_name)
        deploy_files(client, bucket_name=bucket_name)
        configure_web_hosting(client, bucket_name=bucket_name, index_file='index.html')
        set_bucket_acl(client, bucket_name)
    else:
        deploy_files(client, bucket_name=bucket_name)
        configure_web_hosting(client, bucket_name=bucket_name, index_file='index.html')
        set_bucket_acl(client, bucket_name)


if __name__ == '__main__':
    bucket_name = 'codewithakay.com'
    main(bucket_name=bucket_name)
