from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from foodsharing.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init database
    db.init_app(app)
    
    # import blueprints
    from .views.home import home
    
    # register blueprints
    app.register_blueprint(home, url_prefix="/")

    return app
