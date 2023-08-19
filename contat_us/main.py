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

    handle_message(
        client=client,
        sender_email='codewithakay@gmail.com',
        recipient_email='kris@codewithakay.com',
        subject=subject,
        email_body=email_body
    )


def get_ses_client():
    try:
        client = boto3.client('ses', region_name='eu-west-2')
    except ClientError as err:
        logger.error(f'An error occurred.\n{e}')
        raise
    return client


def handle_message(
        client,
        sender_email: str,
        recipient_email: str,
        subject: str,
        email_body: str
):
    try:
        client.send_email(
            Source=sender_email,
            Destination={'ToAddresses': [recipient_email, ], },
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
    except ClientError as e:
        logger.error(f'An error occurred while trying to send the email.\n{e}')