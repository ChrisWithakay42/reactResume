import logging
import os

import boto3
from boto3.exceptions import ResourceLoadException
from dotenv import load_dotenv

from cicd import PROJECT_ROOT
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


def main(function_name: str):
    client = boto3.client('lambda', 'eu-west-2')
    lambda_wrapper = LambdaWrapper(
        client=client,
        iam_resource=get_iam_role()
    )
    deployment_file = lambda_wrapper.create_deployment_file(f'{PROJECT_ROOT}/contact_us/')
    if lambda_wrapper.get_function(function_name):
        lambda_wrapper.update_function_code(function_name=function_name, deployment_package=deployment_file)
    else:
        lambda_wrapper.create_function(
            function_name='test_function',
            function_description='testing function deployment code',
            handler_name='test_handler',
            deployment_file=deployment_file
        )


if __name__ == '__main__':
    main('codewithakay_mail_server')
