from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils.settings import STATIC_DIR, TEMPLATES_DIR
from .User.views import user_blue
from utils.config import Config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATES_DIR)

    app.register_blueprint(blueprint=user_blue, url_prefix='/user')

    app.config.from_object(Config)

    init_ext(app)

    return app


def init_ext(app):

    db.init_app(app)
