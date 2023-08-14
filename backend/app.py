from flask import Flask

from backend import commands
from backend.extensions import cors
from backend.extensions import mail
from backend.config import Config


def get_config_object():
    return Config()


def create_app(config_object=None):
    if config_object is None:
        config_object = get_config_object()

    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    register_commands(app)


def register_extensions(app):
    mail.init_app(app)
    cors(app)


def register_blueprints(app):
    from backend.contact import contact_blueprint
    app.register_blueprint(contact_blueprint)


def register_commands(app):
    app.cli.add_command(commands.create_s3_bucket)
