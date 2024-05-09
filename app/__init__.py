from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

## Actions that need to be performed before internal imports occur
load_dotenv()
app = Flask(__name__)
db = SQLAlchemy()
login = LoginManager(app)

# Import controllers and models to ensure they are registered with the app
from app.controllers import index, auth
from app.models.main import *

# Load configuration from config.py
app.config.from_object(Config)
login.login_view = 'index'

# Define user loader function for Flask-Login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))



# Initialize SQLAlchemy and create database tables
db.init_app(app)

with app.app_context():
    db.create_all()
