import logging

from cicd.aws_wrapper import BucketWrapper

logger = logging.getLogger(__name__)


def main(bucket_name: str):
    bucket = BucketWrapper('s3')
    exists = bucket.exists(bucket_name=bucket_name)
    if not exists:
        logger.info(f'Bucket {bucket_name} does not exist. Creating now...')
        bucket.create(bucket_name=bucket_name)
        bucket.upload_files(bucket_name=bucket_name)
        bucket.configure_web_hosting(bucket_name=bucket_name, index_file='index.html')
        bucket.set_acl(bucket_name=bucket_name)
        logger.info(f'Success fully created bucket {bucket_name}. Files are uploaded. Bucket configured for web hosting.')
    else:
        logger.info(f'Found bucket {bucket_name}. Starting file upload and configuration.')
        bucket.upload_files(bucket_name=bucket_name)
        bucket.configure_web_hosting(bucket_name=bucket_name, index_file='index.html')
        bucket.set_acl(bucket_name=bucket_name)
        logger.info(f'Successfully uploaded files and set web hosting configuration for {bucket_name}.')


if __name__ == '__main__':
    main(bucket_name='codewithakay.com')
