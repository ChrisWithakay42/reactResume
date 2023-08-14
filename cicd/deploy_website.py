import os

from bucket_api import S3Manager


def deploy_to_s3():
    s3_manager = S3Manager()
    s3_manager.get_or_create_bucket(bucket_name='codewithakay.com', region=os.getenv('AWS_REGION'))
    s3_manager.configure_bucket_for_web_hosting(bucket_name='codewithakay.com', index_document='index.html')
    s3_manager.deploy_to_bucket(bucket_name='codewithakay.com')

if __name__ == '__main__':
    deploy_to_s3()
