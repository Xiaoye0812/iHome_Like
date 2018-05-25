
from flask import Flask

from utils.settings import STATIC_DIR, TEMPLATES_DIR
from .User.views import user_blue, index_blue
from .House.views import house_blue
from .Order.views import order_blue
from utils.config import Config
from utils.functions import init_ext


def create_app():
    app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATES_DIR)

    app.register_blueprint(blueprint=user_blue, url_prefix='/user')
    app.register_blueprint(blueprint=index_blue, url_prefix='')
    app.register_blueprint(blueprint=house_blue, url_prefix='/house')
    app.register_blueprint(blueprint=order_blue, url_prefix='/order')

    app.config.from_object(Config)

    init_ext(app)

    return app
