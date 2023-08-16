import logging
import os

import boto3
from boto3.exceptions import ResourceLoadException
from botocore.exceptions import ParamValidationError
from botocore.exceptions import SSLError
from dotenv import load_dotenv

from cicd.aws_wrapper import LambdaWrapper

logger = logging.getLogger(__name__)

load_dotenv()


def get_iam_role():
    try:
        iam = boto3.resource('iam')
    except ResourceLoadException as e:
        logger.error(f'An error occurred while fetching the resource.\n{e}')
    else:
        role_name = os.getenv('AWS_LAMBDA_IAM_ROLE_NAME')
        role = iam.Role(role_name)
        role.load()
        return role


def main():
    # boto3.set_stream_logger('')
    role = get_iam_role()
    client = LambdaWrapper(service_name='lambda', iam_resource=role)
    deployment_package = client.create_deployment_package(source_dir='/')
    try:
        client.create(
            function_name='codewithakay_mail_server',
            handler_name='send_mail',
            iam_role=role.arn,
            deployment_package=deployment_package
        )
    except (ParamValidationError, SSLError) as e:
        logger.error(f'There was an error while trying to create Lambda Function.\n{e}')


if __name__ == '__main__':
    main()
