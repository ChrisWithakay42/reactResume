from flask import request
from flask_mail import Message
from pydantic import BaseModel
from pydantic import ValidationError

from backend.autoapp import app
from backend.contact import contact_blueprint
from backend.contact import logger


class ValidateContactFormInput(BaseModel):
    name: str
    phone: int
    email: str
    subject: str
    message: str


@contact_blueprint.route('/contact-form', methods=['POST'])
def send_mail():
    data = request.form
    try:
        ValidateContactFormInput(**data)
    except ValidationError as e:
        logger.error(f'{e}')
    name = data['name']
    phone = data['phone']
    email = data['email']
    subject = data['email']
    message = data['message']
    msg = Message(subject, sender=app.config['FORWARDING_EMAIL_ADDRESS'], recipients='')
    msg.body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"
    return 202
