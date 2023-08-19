import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def send_mail(event, context):
    message_details = json.loads(event.get('body', None))

    name = message_details.get('name', None)
    phone = message_details.get('phone', None)
    email = message_details.get('email', None)
    subject = message_details.get('subject', None)
    message = message_details.get('message', None)

    email_body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'

    client = get_ses_client()

    try:
        client.send_email(
            Source='codewithakay@gmail.com',
            Destination={'ToAddresses': ['codewithakay@gmail.com']},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Email sent successfully')
        }
    except ClientError as e:
        logger.error(f'An error occurred while trying to send the email.\n{e}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }


def get_ses_client():
    try:
        client = boto3.client('ses', region_name='eu-west-2')
    except ClientError as err:
        logger.error(f'An error occurred.\n{err}')
        raise
    return client
