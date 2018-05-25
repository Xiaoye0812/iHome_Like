from datetime import datetime

from flask import Blueprint, request, jsonify, session, render_template

from App.House.models import Order, House
from App.User.models import User
from utils import status_code
from utils.functions import login_check


order_blue = Blueprint('order', __name__)


# 预定房间接口
@order_blue.route('/', methods=['POST'])
def create_order():

    order_dict = request.form
    house_id = order_dict['house_id']
    start_time = datetime.strptime(order_dict['start_time'], '%Y-%m-%d')
    end_time = datetime.strptime(order_dict['end_time'], '%Y-%m-%d')

    if not all((house_id, start_time, end_time)):
        return jsonify(status_code.PARAMS_ERROR)

    # 判断时间是否正确
    if start_time > end_time:
        return jsonify(status_code.ORDER_START_TIME_GT_END_TIME)

    house = House.query.get(house_id)

    if house.order_count >= house.capacity:
        return jsonify(status_code.ORDER_HOUSE_IS_FULL)

    order_obj = Order()
    order_obj.user_id = session['user_id']
    order_obj.house_id = house_id
    order_obj.begin_date = start_time
    order_obj.end_date = end_time
    order_obj.house_price = house.price

    order_obj.days = (end_time - start_time).days + 1
    # 判断是否不符合入住天数限制
    if house.max_days != 0 and order_obj.days > house.max_days:
        return jsonify(status_code.ORDER_GT_MAX_DAYS)
    if order_obj.days < house.min_days:
        return jsonify(status_code.ORDER_LT_MIN_DAYS)

    order_obj.amount = house.price * order_obj.days

    try:
        order_obj.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


# 我的订单页面
@order_blue.route('/orders/', methods=['GET'])
# @login_check
def order():

    return render_template('orders.html')


# 我的订单数据接口
@order_blue.route('/myorders/', methods=['GET'])
def my_orders():

    user_id = session['user_id']
    user = User.query.get(user_id)

    orders = user.orders
    order_list = []
    for sub_order in orders:
        order_list.append(sub_order.to_dict())

    return jsonify(code=status_code.SUCCESS['code'], order_list=order_list)


# 客户订单页面
@order_blue.route('/lorders/', methods=['GET'])
# @login_check
def lorders():

    return render_template('lorders.html')


# 客户订单数据接口
@order_blue.route('/mylorders/', methods=['GET'])
def my_lorders():

    user_id = session['user_id']
    houses = House.query.filter(House.user_id == user_id).all()

    # order_list = []
    # for house in houses:
    #     for order in house.orders:
    #         order_list.append(order.to_dict())

    houseid_list = [house.id for house in houses]
    orders = Order.query.filter(Order.house_id.in_(houseid_list)).order_by(Order.create_time).all()
    order_list = [ord.to_dict() for ord in orders]

    return jsonify(code=status_code.SUCCESS['code'], order_list=order_list)


# 接收客户订单接口
@order_blue.route('/accept/', methods=['POST'])
def accept_order():

    order_id = request.form['order_id']

    order1 = Order.query.get(order_id)
    order1.status = 'WAIT_COMMENT'

    try:
        order1.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


# 拒接客户订单接口
@order_blue.route('/reject/', methods=['POST'])
def reject_order():

    order_id = request.form['order_id']
    comment = request.form['comment']

    order1 = Order.query.get(order_id)
    order1.status = 'WAIT_COMMENT'
    order1.comment = comment

    try:
        order1.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)
