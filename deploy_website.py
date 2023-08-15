import logging

from cicd.aws_wrapper import BucketWrapper

logger = logging.getLogger(__name__)


def main(bucket_name: str):
    bucket = BucketWrapper('s3')
    exists = bucket.exists(bucket_name=bucket_name)
    if not exists:
        bucket.create(bucket_name=bucket_name)
        bucket.upload_files(bucket_name=bucket_name)
        bucket.configure_web_hosting(bucket_name=bucket_name, index_file='index.html')
        bucket.set_acl(bucket_name=bucket_name)
    else:
        bucket.upload_files(bucket_name=bucket_name)
        bucket.configure_web_hosting(bucket_name=bucket_name, index_file='index.html')
        bucket.set_acl(bucket_name=bucket_name)


if __name__ == '__main__':
    main(bucket_name='codewithakay.com')
