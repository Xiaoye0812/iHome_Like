import re
import os

from flask import Blueprint, render_template, jsonify, session, request

from .models import db
from utils.functions import login_check
from utils.settings import UPLOAD_HOUSE_IMAGE_DIRS
from utils import status_code
from App.User.models import User
from App.House.models import House, Facility, Area, HouseImage

house_blue = Blueprint('house', __name__)


@house_blue.route('/createtable/')
def create_table():

    db.create_all()

    return '创建完成'


# 我的房源页面
@house_blue.route('/myhouse/', methods=['GET'])
@login_check
def myhouse():

    return render_template('myhouse.html')


# 我的房源接口
@house_blue.route('/auth_myhouse/', methods=['GET'])
def auth_myhouse():

    user = User.query.get(session['user_id'])

    if user.id_card:

        houses = House.query.filter(House.user_id == user.id).order_by(House.id.desc())

        house_list = []
        for house in houses:
            house_list.append(house.to_dict())

        return jsonify(code=status_code.SUCCESS['code'], house_list=house_list)

    else:

        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


# 发布新房源页面
@house_blue.route('/newhouse/', methods=['GET'])
@login_check
def new_house():

    return render_template('newhouse.html')


# 发布房源接口
@house_blue.route('/newhouse/', methods=['POST'])
def create_newhouse():

    info_dict = request.form

    user_id = session['user_id']
    area_id = info_dict.get('area_id')
    title = info_dict.get('title')
    price = info_dict.get('price')
    address = info_dict.get('address')
    room_count = info_dict.get('room_count')
    acreage = info_dict.get('acreage')
    unit = info_dict.get('unit')
    capacity = info_dict.get('capacity')
    beds = info_dict.get('beds')
    deposit = info_dict.get('deposit')
    min_days = info_dict.get('min_days')
    max_days = info_dict.get('max_days')
    facility_list = info_dict.getlist('facility')

    house = House()
    house.user_id = user_id
    house.area_id = area_id
    house.title = title
    house.price = price
    house.address = address
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days

    for facility_id in facility_list:
        faci = Facility.query.get(facility_id)
        house.facities.append(faci)

    try:
        house.add_update()
        return jsonify(code=status_code.SUCCESS['code'], house_id=house.id)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


# 上传房源图片接口
@house_blue.route('/uploadimg/', methods=['PUT'])
def upload_img():

    files_dict = request.files
    house_id = request.form.get('house_id')

    if 'house_image' in files_dict:

        house_image = files_dict['house_image']

        if not re.match(r'^image/.*$', house_image.mimetype):
            return jsonify(status_code.MYHOUSE_UPLOAD_TYPE_ERROR)

        save_url = os.path.join(UPLOAD_HOUSE_IMAGE_DIRS, '%s' % house_id)
        if not os.path.exists(save_url):
            os.makedirs(save_url)

        url = os.path.join(save_url, house_image.filename)

        house_image.save(url)

        house = House.query.get(house_id)
        image_url = os.path.join('/static/upload/house/%s' % house_id, house_image.filename)
        if not house.index_image_url:
            house.index_image_url = image_url

        house_image = HouseImage()
        house_image.url = image_url
        house_image.house_id = house_id

        try:
            house_image.add_update()
            house.add_update()
            return jsonify(status_code.SUCCESS)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)


# 查询设施与地区接口
@house_blue.route('/faci_area/', methods=['GET'])
def facility_area_info():

    facilities = Facility.query.all()
    areas = Area.query.all()
    facility_list = []
    for facility in facilities:
        facility_list.append(facility.to_dict())

    area_list = []
    for area in areas:
        area_list.append(area.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], facility_list=facility_list, area_list=area_list)


@house_blue.route('/detail/<int:house_id>/', methods=['GET'])
def detail(house_id):

    return render_template('detail.html')


@house_blue.route('/detailinfo/<int:house_id>/', methods=['GET'])
def detail_info(house_id):

    user_id = session['user_id']
    house = House.query.get(house_id)
    house_dict = house.to_full_dict()

    return jsonify(code=status_code.SUCCESS['code'], house_dict=house_dict)
