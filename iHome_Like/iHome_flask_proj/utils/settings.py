import os

from .functions import get_database_config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

DATABASE = {
    'database': 'mysql',
    'driver': 'pymysql',
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': '940812',
    'name': 'db_ihome',
}

SQLALCHEMY_DATABASE_URI = get_database_config(DATABASE)

UPLOAD_DIRS = os.path.join(STATIC_DIR, 'upload')
UPLOAD_AVATAR_DIRS = os.path.join(UPLOAD_DIRS, 'user')
UPLOAD_HOUSE_IMAGE_DIRS = os.path.join(UPLOAD_DIRS, 'house')
