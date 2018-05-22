
### 登录接口

#### request请求

    POST /user/login/

#### params参数

    mobile str 电话号码
    password str 密码

#### response响应

##### 失败响应1：

    {
        'code': 1001,
        'msg': '手机号不正确'
    }

##### 失败响应2：

    {
        'code': 1004,
        'msg': '用户不存在'
    }

##### 失败响应3：

    {
        'code': 1005,
        'msg': '密码不正确'
    }

##### 成功响应：

    {
        'code': 200
        'msg': '请求成功'
    }