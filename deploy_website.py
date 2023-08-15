import logging

from cicd.aws_wrapper import S3Wrapper

logger = logging.getLogger(__name__)


def main(bucket_name: str):
    s3_client = S3Wrapper('s3')
    bucket = s3_client.get_bucket(bucket_name=bucket_name)
    if not bucket:
        s3_client.create_bucket(bucket_name=bucket_name)
        s3_client.deploy_files(bucket_name=bucket_name)
        s3_client.configure_web_hosting(bucket_name=bucket_name, index_file='index.html')
        s3_client.set_bucket_acl(bucket_name=bucket_name)
    else:
        s3_client.deploy_files(bucket_name=bucket_name)
        s3_client.configure_web_hosting(bucket_name=bucket_name, index_file='index.html')
        s3_client.set_bucket_acl(bucket_name=bucket_name)


if __name__ == '__main__':
    main(bucket_name='codewithakay.com')
