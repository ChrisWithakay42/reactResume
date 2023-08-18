import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def send_mail(event, context):
    message_details = event.get('body', None)

    if message_details is None:
        raise ValueError('There was an error with the request body')

    name = message_details.get('name', None)
    phone = message_details.get('phone', None)
    email = message_details.get('email', None)
    subject = message_details.get('subject', None)
    message = message_details.get('message', None)

    email_body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'

    client = boto3.client('ses', region_name='eu-west-2')
    try:
        client.send_email(
            Source='codewithakay@gmail.com',
            Destination='kris@codewithakay.com',
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
    except ClientError as e:
        return {
            'StatusCode': 503,
            'body': json.dumps(f'Error: {str(e)}')
        }
    else:
        return {
            'StatusCode': 200,
            'body': json.dumps('Email Sent Successfully')
        }


def handle_message(name: str, phone: str, email: str, subject: str, message: str):
    try:
        client = boto3.client('ses', ...)
    except ClientError as err:
        if err.response['Error']['Code'] == 'SomeException':
            print(str(err))
