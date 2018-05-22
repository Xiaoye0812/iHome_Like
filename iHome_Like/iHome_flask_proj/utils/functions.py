
from flask import session, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_ext(app):

    db.init_app(app)


def get_database_config(database_conf):

    database = database_conf['database']
    driver = database_conf['driver']
    host = database_conf['host']
    port = database_conf['port']
    user = database_conf['user']
    password = database_conf['password']
    name = database_conf['name']

    return '{}+{}://{}:{}@{}:{}/{}'.format(database, driver, user, password, host, port, name)


import functools
def login_check(run_func):

    @functools.wraps(run_func)
    def decorator():

        try:
            # 验证用户是否登录
            if 'user_id' in session:
                return run_func()
            else:
                return redirect('/user/login/')
        except:
            return redirect('/user/login/')

    return decorator