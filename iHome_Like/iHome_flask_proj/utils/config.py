import redis

from .settings import SQLALCHEMY_DATABASE_URI


class Config:

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key'

    # 配置redis
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')
    SESSION_KEY_PREFIX = 'aj_'
