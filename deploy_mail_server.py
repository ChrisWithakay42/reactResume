import logging
import os

import boto3
from boto3.exceptions import ResourceLoadException
from dotenv import load_dotenv

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
    print('Hello Lambda!')


if __name__ == '__main__':
    main()
