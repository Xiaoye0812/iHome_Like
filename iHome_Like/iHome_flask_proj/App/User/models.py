
from App.models import db, BaseModel


class User(BaseModel):

    __tablename__ = 'tb_ihome_user'
    id = db.Column(db.INTEGER, primary_key=True)
    phone = db.Column(db.String(11), unique=True)
    passwd_hash = db.Column(db.String(200))
    name = db.Column(db.String(30), unique=True)
    avatar = db.Column(db.String(100))  # 头像
    id_name = db.Column(db.String(30))  # 实名认证姓名
    id_card = db.Column(db.String(18), unique=True)  # 实名认证身份证

    houses = db.relationship('House', backref='user')
    orders = db.relationship('Order', backref='user')

    #
    @property
    def password(self):

        return ''

    @password.setter
    def password(self, pwd):

        self.passwd_hash = generate_password_hash(pwd)
