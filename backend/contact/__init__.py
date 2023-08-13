import logging

from flask import Blueprint

logger = logging.getLogger(__name__)

contact_blueprint = Blueprint('/', __name__)
