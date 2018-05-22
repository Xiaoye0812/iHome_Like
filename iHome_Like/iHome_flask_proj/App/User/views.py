import re
import os

from flask import Blueprint, request, jsonify, redirect, render_template, session, sessions

from .models import db, User
from utils import status_code
from utils.settings import UPLOAD_DIRS

index_blue = Blueprint('index', __name__)
user_blue = Blueprint('user', __name__)


@index_blue.route('/')
def index():

    return render_template('index.html')


@user_blue.route('/createtables/')
def create_tables():

    db.create_all()

    return '创建完成'


# 注册页面
@user_blue.route('/register/', methods=('GET',))
def register():
    return render_template('register.html')


# 注册用户API
@user_blue.route('/register/', methods=('POST',))
def to_register():

    register_dict = request.form

    phone = register_dict.get('mobile')
    pwd1 = register_dict.get('password')
    pwd2 = register_dict.get('password2')

    if not all((phone, pwd1, pwd2)):  # 如果有任一为空
        return jsonify(status_code.USER_REGISTER_PARAMS_ERROR)

    if not re.match(r'^1[34578]\d{9}$', phone):  # 匹配手机号
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)

    if User.query.filter(User.phone == phone).count():  # 手机号已注册
        return jsonify(status_code.USER_REGISTER_MOBILE_IS_EXSITS)

    if pwd1 != pwd2:  # 密码不匹配
        return jsonify(status_code.USER_REGISTER_PAWSSWORD_ERROR)

    user = User()
    user.phone = phone
    user.name = phone
    user.password = pwd1

    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


# 登录页面
@user_blue.route('/login/', methods=('GET',))
def login():

    return render_template('login.html')


# 登录api
@user_blue.route('/login/', methods=('POST',))
def user_login():

    user_dict = request.form

    mobile = user_dict.get('mobile')
    password = user_dict.get('password')

    if not all((mobile, password)):
        return jsonify(status_code.PARAMS_ERROR)

    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)

    user = User.query.filter(User.phone == mobile).first()

    if user:
        if user.check_pwd(password):
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PASSWORD_ERROR)
    else:
        return jsonify(status_code.USER_LOGIN_IS_NOT_EXSITS)


# 个人中心页面
@user_blue.route('/my/', methods=('GET',))
def my():

    return render_template('my.html')


@user_blue.route('/user/', methods=('GET',))
def get_user_info():

    user_id = session['user_id']
    user = User.query.get(user_id)

    return jsonify({'user': user.to_basic_dict(), 'code': 200})


@user_blue.route('/profile/', methods=('GET',))
def profile():

    return render_template('profile.html')


@user_blue.route('/profile/', methods=('POST',))
def upload_profile():

    user_id = session['user_id']
    file_dict = request.files

    if 'avatar' in file_dict:

        avatar = file_dict['avatar']

        if not re.match(r'^image/.*$', avatar.mimetype):
            return jsonify(status_code.USER_UPLOAD_TYPE_ERROR)

        url = os.path.join(UPLOAD_DIRS, avatar.filename)

        avatar.save(url)

        user = User.query.filter(User.id == user_id).first()
        image_url = os.path.join('/static/upload', avatar.filename)

        user.avatar = image_url

        try:
            user.add_update()
            return jsonify(code=status_code.SUCCESS['code'], url=image_url)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)


@user_blue.route('/profile/name/', methods=['POST'])
def update_name():

    user_id = session['user_id']
    name = request.form.get('name')
    if not user_id:
        return jsonify(status_code.USER_LOGIN_TIMEOUT)

    if User.query.filter(User.name == name).count:
        return jsonify(status_code.USER_NAME_IS_EXSITS)

    user = User.query.filter(User.id == user_id).first()

    if not user:
        return jsonify(status_code.USER_LOGIN_IS_NOT_EXSITS)

    user.name = name
    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


@user_blue.route('/auth/', methods=['GET'])
def realname():

    return render_template('auth.html')


@user_blue.route('/updateauth/', methods=['POST'])
def update_auth():

    user_id = session['user_id']
    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')


    if not user_id:
        return jsonify(status_code.USER_LOGIN_TIMEOUT)

    if not all((real_name, id_card)):
        return jsonify(status_code.PARAMS_ERROR)

    user = User.query.filter(User.id == user_id).first()

    if not user:
        return jsonify(status_code.USER_LOGIN_IS_NOT_EXSITS)

    if user.id_name or user.id_card:
        return jsonify(status_code.USER_REAL_NAME_IS_EXSITS)

    user.id_name = real_name
    user.id_card = id_card
    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception:
        return jsonify(status_code.DATABASE_ERROR)


@user_blue.route('/logout/', methods=('GET',))
def logout():

    return jsonify(status_code.SUCCESS)
