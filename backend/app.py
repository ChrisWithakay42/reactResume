from flask import Flask
from flask import request
from flask_cors import CORS
from flask_mail import Mail
from flask_mail import Message

from config import Config


def get_config_object():
    return Config()


def create_app(config_object=None):
    if config_object is None:
        config_object = get_config_object()

    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)


def register_extensions(app):
    Mail(app)
    CORS(app)


def submit_form() -> int:
    data = request.form
    name = data['name']
    phone = data['phone']
    email = data['email']
    subject = data['subject']
    message = data['message']
    msg = Message(subject, sender=email, recipients=['recipient@example.com'])
    msg.body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

    return 202  # request Accepted
