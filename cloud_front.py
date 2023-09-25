import boto3

from aws_wrapper.wrapper import CloudFrontWrapper


def invalidate_cache(distribution_id: str):
    client = boto3.client('cloudfront', 'eu-west-2')
    wrapper = CloudFrontWrapper(cloud_front_client=client)
    wrapper.invalidate_cache(distribution_id)


if __name__ == '__main__':
    invalidate_cache('E33Q1FMLV0KCEL')
