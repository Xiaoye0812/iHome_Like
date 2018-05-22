

SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 900, 'msg': '数据库访问失败'}
PARAMS_ERROR = {'code': 901, 'msg': '参数有误'}
USER_LOGIN_TIMEOUT = {'code': 902, 'msg': '登录超时'}

# 用户模块
USER_REGISTER_PARAMS_ERROR = {'code': 1000, 'msg': '注册信息参数错误'}
USER_REGISTER_MOBILE_ERROR = {'code': 1001, 'msg': '手机号不正确'}
USER_REGISTER_MOBILE_IS_EXSITS = {'code': 1002, 'msg': '手机号已注册'}
USER_REGISTER_PAWSSWORD_ERROR = {'code': 1003, 'msg': '两次密码不一致'}


USER_LOGIN_IS_NOT_EXSITS = {'code': 1004, 'msg': '用户名不存在'}
USER_LOGIN_PASSWORD_ERROR = {'code': 1005, 'msg': '密码不正确'}

USER_UPLOAD_TYPE_ERROR = {'code': 1006, 'msg': '上传图片格式不正确'}
USER_NAME_IS_EXSITS = {'code': 1008, 'msg': '用户名已存在，不可更改'}

USER_CARD_TYPE_ERROR = {'code': 1007, 'msg': '身份证格式不正确'}

# 房屋模块
MYHOUSE_USER_IS_NOT_AUTH = {'code': 2000, 'msg': '用户未实名认证'}
MYHOUSE_UPLOAD_TYPE_ERROR = {'code': 2001, 'msg': '上传图片格式不正确'}
