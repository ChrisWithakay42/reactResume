import json
from unittest.mock import Mock
from unittest.mock import patch

import pytest
from moto import mock_ses

from contact_us.main import send_email_via_ses
from contact_us.main import send_mail


class TestSendMailFunction:

    @patch('contact_us.main.get_ses_client')
    @patch('contact_us.main.send_email_via_ses')
    def test_send_mail_successful(
            self,
            mock_send_email_via_ses,
            mock_get_ses_client,
            event
    ):
        mock_client = Mock()
        mock_get_ses_client.return_value = mock_client

        send_mail(event, context={})
        body = json.loads(event['body'])

        mock_send_email_via_ses.assert_called_once_with(
            client=mock_client,
            subject='Test Subject',
            sender_email='codewithakay@gmail.com',
            recipient_email='codewithakay@gmail.com',
            email_body=f'Name: {body["name"]}\nPhone: {body["phone"]}\nEmail: {body["email"]}\nMessage: {body["message"]}'
        )

    @pytest.mark.parametrize("missing_field", ['name', 'phone', 'email', 'subject', 'message'])
    def test_send_mail_missing_fields(self, event, missing_field):
        event_data = json.loads(event['body'])
        event_data.pop(missing_field)
        modified_event = {
            'body': json.dumps(event_data)
        }

        with pytest.raises(ValueError, match=f'The following fields are missing: {missing_field}'):
            send_mail(modified_event, context={})

