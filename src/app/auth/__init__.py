from flask import Blueprint
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

auth_bp = Blueprint('auth', __name__, template_folder='templates')

from . import routes

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
