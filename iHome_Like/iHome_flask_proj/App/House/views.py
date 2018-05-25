import re
import os

from flask import Blueprint, render_template, jsonify, session, request
from sqlalchemy import or_

from .models import db, Order
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

    # for facility_id in facility_list:
    #     faci = Facility.query.get(facility_id)
    #     house.facities.append(faci)

    if facility_list:
        facities = Facility.query.filter(Facility.id.in_(facility_list)).all()
        house.facities = facities

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


# 查询地区接口
@house_blue.route('/area/', methods=['GET'])
def area_info():

    areas = Area.query.all()

    area_list = []
    for area in areas:
        area_list.append(area.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], area_list=area_list)


# 查询设施接口
@house_blue.route('/faci/', methods=['GET'])
def facility_info():

    facilities = Facility.query.all()
    facility_list = []
    for facility in facilities:
        facility_list.append(facility.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], facility_list=facility_list)


# 房屋详情页面
@house_blue.route('/detail/', methods=['GET'])
@login_check
def detail():

    return render_template('detail.html')


# 房屋详情接口
@house_blue.route('/detailinfo/<int:house_id>/', methods=['GET'])
def detail_info(house_id):

    user_id = session['user_id']
    house = House.query.get(house_id)
    house_dict = house.to_full_dict()

    booking = 0 if user_id == house.user_id else 1

    return jsonify(code=status_code.SUCCESS['code'], house_dict=house_dict, booking=booking)


# 预约页面
@house_blue.route('/booking/', methods=['GET'])
# @login_check
def booking():

    return render_template('booking.html')


# 查找结果页面
@house_blue.route('/search/', methods=['GET'])
def search_html():

    return render_template('search.html')


# 查找房源接口
@house_blue.route('/searchhouse/', methods=['GET'])
def search_house():

    info_dict = request.args
    area_id = info_dict['area_id']
    start_date = info_dict['start_date']
    end_date = info_dict['end_date']
    sort_key = info_dict['sort_key']
    next_page = info_dict['next_page']

    if area_id:
        houses = House.query.filter(House.area_id == area_id)
    else:
        houses = House.query

    orders = Order.query.filter(or_(Order.begin_date <= end_date, Order.end_date >= start_date)).all()

    order_list = [order.id for order in orders]

    houses = houses.filter(House.id.notin_(order_list)).all()

    house_list = []
    for house in houses:
        house_list.append(house.to_full_dict())

    return jsonify(code=status_code.SUCCESS['code'], house_list=house_list)


# 主页现实房源接口
@house_blue.route('/indexhouse/', methods=['GET'])
def index_house():

    houses = House.query.order_by(House.create_time).limit(5)
    house_list = []
    for house in houses:
        house_list.append(house.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], house_list=house_list)
