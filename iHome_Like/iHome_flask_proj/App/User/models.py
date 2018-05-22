from werkzeug.security import generate_password_hash, check_password_hash

from App.basemodels import BaseModel, db


class User(BaseModel, db.Model):

    __tablename__ = 'tb_ihome_user'
    id = db.Column(db.INTEGER, primary_key=True)
    phone = db.Column(db.String(11), unique=True)
    passwd_hash = db.Column(db.String(200))
    name = db.Column(db.String(30), unique=True)
    avatar = db.Column(db.String(100))  # 头像
    id_name = db.Column(db.String(30))  # 实名认证姓名
    id_card = db.Column(db.String(18), unique=True)  # 实名认证身份证

    # houses = db.relationship('House', backref='user')
    # orders = db.relationship('Order', backref='user')

    #读
    @property
    def password(self):

        return ''

    # 写
    @password.setter
    def password(self, pwd):

        self.passwd_hash = generate_password_hash(pwd)

    # 对比匹配
    def check_pwd(self, pwd):

        return check_password_hash(self.passwd_hash, pwd)

    def to_basic_dict(self):

        return {
            'id': self.id,
            'avatar': self.avatar if self.avatar else '',
            'name': self.name,
            'phone': self.phone
        }