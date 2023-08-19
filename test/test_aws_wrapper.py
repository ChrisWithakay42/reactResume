import pytest
from botocore.exceptions import ClientError

from cicd.exceptions import BucketAlreadyOwnedByYou


class TestS3Wrapper:
    bucket_name = 'test_bucket'
    region_name = 'eu-west-2'
    location_constraints = {
        'LocationConstraint': 'eu-west-2',
    }

    def test_create_bucket(self, mock_s3_client, s3_wrapper):
        s3_wrapper.create_bucket(
            bucket_name='test_bucket',
            bucket_configuration=self.location_constraints
        )
        buckets = mock_s3_client.list_buckets()
        assert 'test_bucket' in [bucket['Name'] for bucket in buckets['Buckets']]

    def test_create_bucket_with_the_same_name(self, mock_s3_client, s3_wrapper):
        bucket_name = 'test_bucket'
        s3_wrapper.create_bucket(
            bucket_name=bucket_name,
            bucket_configuration=self.location_constraints
        )
        with pytest.raises(BucketAlreadyOwnedByYou):
            s3_wrapper.create_bucket(
                bucket_name=bucket_name,
                bucket_configuration=self.location_constraints
            )

    def test_set_bucket_up_for_web_hosting(self, mock_s3_client, s3_wrapper):
        s3_wrapper.create_bucket(
            bucket_name=self.bucket_name,
            bucket_configuration=self.location_constraints
        )

        with pytest.raises(ClientError) as err:
            mock_s3_client.get_bucket_website(
                Bucket=self.bucket_name
            )

        assert err.value.response['Error']['Code'] == 'NoSuchWebsiteConfiguration'

        s3_wrapper.configure_bucket_for_web_hosting(bucket_name=self.bucket_name)
        response = mock_s3_client.get_bucket_website(
            Bucket=self.bucket_name
        )
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    def test_set_bucket_acl_policies(self, s3_wrapper):
        ...

    def test_upload_files_to_bucket(self, s3_wrapper):
        ...


class TestLambdaWrapper:

    def test_create_lambda_function(self):
        ...
