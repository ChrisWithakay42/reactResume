import boto3
import moto
import pytest
from moto import mock_s3

from cicd.aws_wrapper import S3Wrapper


@pytest.fixture
def mock_s3_client():
    with mock_s3() as mock:
        yield boto3.client('s3', region_name='eu-west-2')


@pytest.fixture
def s3_wrapper(mock_s3_client):
    wrapper = S3Wrapper(mock_s3_client, region_name='eu-west-2')
    return wrapper
