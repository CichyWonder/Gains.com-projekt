from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

cart_bp = Blueprint('cart', __name__, template_folder = 'templates')

from . import routes
db = SQLAlchemy()