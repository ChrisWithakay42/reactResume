import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def send_mail(event, context):
    message_details = json.loads(event.get('body', {}))

    name = message_details.get('name', None)
    phone = message_details.get('phone', None)
    email = message_details.get('email', None)
    subject = message_details.get('subject', None)
    message = message_details.get('message', None)

    required_fields = [name, phone, email, subject, message]

    if any(item is None for item in required_fields):
        missing_fields = [field_name for field_name, item in
                          zip(['name', 'phone', 'email', 'subject', 'message'], required_fields) if item is None]
        raise ValueError(f"The following fields are missing: {', '.join(missing_fields)}")

    email_body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'

    client = get_ses_client()

    send_email_via_ses(
        client=client,
        subject=subject,
        sender_email='codewithakay@gmail.com',
        # same recipient as sender until SES is operating in a sandbox environment
        recipient_email='codewithakay@gmail.com',
        email_body=email_body
    )


def send_email_via_ses(client, subject: str, sender_email: str, recipient_email: str, email_body: str) -> dict:

    try:
        client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
        return {
            'status_code': 200,
            'message': 'Email sent successfully'
        }
    except ClientError as e:
        logger.error(f'An error occurred while trying to send the email.\n{e}')
        return {
            'status_code': 500,
            'message': f'Error: {str(e)}'
        }


def get_ses_client():
    try:
        client = boto3.client('ses', region_name='eu-west-2')
    except ClientError as err:
        logger.error(f'An error occurred.\n{err}')
        raise
    return client
