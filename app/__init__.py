from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from .models import User, db

###### bring in routes for registration here #######
from .post.routes import post




app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app,db)

from app import routes, models, post

from .models import User, db

#### REGISTER BLUEPRINTS HERE

app.register_blueprint(post)

## initialize db
db.init_app(app)
