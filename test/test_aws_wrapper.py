import pytest
from botocore.exceptions import ClientError

from cicd.aws_wrapper import S3Wrapper


class TestS3Wrapper:
    service_name = 's3'
    region_name = 'eu-west-2'

    def test_bucket_exists(self, mock_bucket):
        s3_wrapper = S3Wrapper(service_name=self.service_name, region=self.region_name)
        assert s3_wrapper.exists('test_bucket') is True

    def test_bucket_does_not_exits(self, mock_bucket):
        s3_wrapper = S3Wrapper(service_name=self.service_name, region=self.region_name)
        assert s3_wrapper.exists('non_existent_test_bucket') is False

    def test_create_bucket(self, mock_s3_client):
        s3_wrapper = S3Wrapper(service_name=self.service_name, region=self.region_name)
        s3_wrapper.create(bucket_name='test_bucket')
        buckets = mock_s3_client.list_buckets()
        assert 'test_bucket' in [bucket['Name'] for bucket in buckets['Buckets']]

    @pytest.mark.skip
    def test_create_when_exception_raised(self, mock_bucket):
        s3_wrapper = S3Wrapper(service_name=self.service_name, region=self.region_name)
        with pytest.raises(ClientError):
            s3_wrapper.create(bucket_name='test_bucket')

    def test_create_when_delete_default_public_access_block(self, mock_s3_client):
        s3_wrapper = S3Wrapper(service_name=self.service_name, region=self.region_name)
        s3_wrapper.create(bucket_name='test_bucket', delete_default_public_access_block=True)





