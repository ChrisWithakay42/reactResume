import boto3
import moto
import pytest
from moto import mock_s3


@pytest.fixture
def mock_s3_client():
    with mock_s3() as mock:
        yield boto3.client('s3', region_name='eu-west-2')


@pytest.fixture
def mock_bucket(mock_s3_client):
    mock_s3_client.create_bucket(
        Bucket='test_bucket',
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2',
        }
    )

