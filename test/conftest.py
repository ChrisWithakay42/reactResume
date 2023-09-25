import json

import boto3
import moto
import pytest
from moto import mock_s3
from moto import mock_ses

from aws_wrapper.wrapper import S3Wrapper


@pytest.fixture
def mock_s3_client():
    with mock_s3() as mock:
        yield boto3.client('s3', region_name='eu-west-2')


@pytest.fixture
def s3_wrapper(mock_s3_client):
    wrapper = S3Wrapper(mock_s3_client, region_name='eu-west-2')
    return wrapper


@pytest.fixture
def event():
    return {
        'body': json.dumps({
            'name': 'John Doe',
            'phone': '1234567890',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        })
    }


@pytest.fixture
def mock_ses_client():
    yield boto3.client('ses', region_name='eu-west-2')
