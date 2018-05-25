
from App.basemodels import BaseModel, db
# from App.User.views import User

ihome_house_facility = db.Table(
    'tb_ihome_house_facility',
    db.Column('house_id', db.Integer, db.ForeignKey('tb_ihome_house.id'), primary_key=True),
    db.Column('facility', db.Integer, db.ForeignKey('tb_ihome_facility.id'), primary_key=True)
)


class House(BaseModel, db.Model):

    """房屋信息"""

    __tablename__ = 'tb_ihome_house'

    id = db.Column(db.Integer, primary_key=True)  # 房屋编号
    # 房屋主人的用户编号
    user_id = db.Column(db.Integer, db.ForeignKey('tb_ihome_user.id'), nullable=False)
    # 归属地的区域编号
    area_id = db.Column(db.Integer, db.ForeignKey('tb_ihome_area.id'), nullable=False)
    title = db.Column(db.String(64), nullable=False)  # 标题
    price = db.Column(db.Integer, default=0)  # 价格，单位：分
    address = db.Column(db.String(512), default='')  # 地址
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)  # 房屋面积
    unit = db.Column(db.String(32), default='')  # 房屋单元
    capacity = db.Column(db.Integer, default=1)  # 房屋容纳人数
    beds = db.Column(db.String(64), default='')  # 房屋床铺配置
    deposit = db.Column(db.Integer, default=0)  # 房屋押金
    min_days = db.Column(db.Integer, default=1)  # 最少入住天数
    max_days = db.Column(db.Integer, default=0)  # 最多入住天数，0表示不限制
    order_count = db.Column(db.Integer, default=0)  # 预定完成的该房屋订单数
    index_image_url = db.Column(db.String(256), default='')  # 房屋主图片的路径

    # 房屋的设施
    facities = db.relationship('Facility', secondary=ihome_house_facility)

    images = db.relationship('HouseImage', backref='house')  # 房屋图片

    orders = db.relationship('Order', backref='house')

    def to_dict(self):

        return {
            'id': self.id,
            'title': self.title,
            'image': self.index_image_url if self.index_image_url else '',
            'area': self.area.name,
            'price': self.price,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            #'avatar': current_app.config['QINIU_URL'] + self.user.avatar if self.user.avatar else '',
            'room': self.room_count,
            'order_count': self.order_count,
            'address': self.address
        }

    def to_full_dict(self):

        return {
            'id': self.id,
            'user_avatar': self.user.avatar if self.user.avatar else '',
            'user_name': self.user.name,
            'title': self.title,
            'image': self.index_image_url if self.index_image_url else '',
            'area': self.area.name,
            'price': self.price,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'acreage': self.acreage,
            'unit': self.unit,
            'capacity': self.capacity,
            'beds': self.beds,
            'deposit': self.deposit,
            'min_days': self.min_days,
            'max_days': self.max_days,
            'images': [image.url for image in self.images],
            'facilities': [facility.to_dict() for facility in self.facities],
            'room': self.room_count,
            'order_count': self.order_count,
            'address': self.area.name + self.address
        }


class HouseImage(BaseModel, db.Model):

    """房屋图片"""

    __tablename__ = 'tb_ihome_house_image'

    id = db.Column(db.Integer, primary_key=True)
    # 房屋编号
    house_id = db.Column(db.Integer, db.ForeignKey('tb_ihome_house.id'), nullable=False)
    url = db.Column(db.String(256), nullable=False)  # 图片路径


class Facility(BaseModel, db.Model):

    """设施信息，房间规格等"""

    __tablename__ = 'tb_ihome_facility'

    id = db.Column(db.Integer, primary_key=True)  # 设施编号
    name = db.Column(db.String(32), nullable=False)  # 设施名称
    css = db.Column(db.String(30), nullable=False)  # 设施展示的图标

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'css': self.css
        }

    def to_house_dict(self):
        return {'id': self.id}


class Area(BaseModel, db.Model):

    """城区"""

    __tablename__ = 'tb_ihome_area'

    id = db.Column(db.Integer, primary_key=True)  # 区域编号
    name = db.Column(db.String(32), nullable=False)  # 区域名称
    houses = db.relationship('House', backref='area')  # 区域房屋

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Order(BaseModel, db.Model):

    """订单"""

    __tablename__ = 'tb_ihome_order'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tb_ihome_user.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('tb_ihome_house.id'), nullable=False)
    begin_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    house_price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(
        db.Enum(
            'WAIT_ACCEPT',  # 待接单
            'WAIT_PAYMENT',  # 待付款
            'PAID',  # 已付款
            'WAIT_COMMENT',  # 待评价
            'COMPLETE',  # 已完成
            'CANCLEED',  # 已取消
            'REJECTED'  # 已拒单
        ),
        default='WAIT_ACCEPT', index=True
    )
    comment = db.Column(db.Text)

    def to_dict(self):

        return {
            'order_id': self.id,
            'house_title': self.house.title,
            'image': self.house.index_image_url,
            'create_date': self.create_time.strftime('%Y-%m-%d'),
            'begin_date': self.begin_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'amount': self.amount,
            'days': self.days,
            'status': self.status,
            'comment': self.comment

        }