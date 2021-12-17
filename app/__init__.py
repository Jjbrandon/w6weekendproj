from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from .models import User, db

###### bringing in routes for registration #######




app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app,db)

from app import routes, models

from .models import db



db.init_app(app)





