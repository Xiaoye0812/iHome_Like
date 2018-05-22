
### 实名认证接口

#### request请求

    POST /user/updateauth/

#### params参数

    real_name str 名字
    id_card str 身份证号码

#### response响应

##### 失败响应1：

    {
        'code': 902,
        'msg': '登录超时'
    }

##### 失败响应2：

    {
        'code': 1007,
        'msg': '身份证格式不正确'
    }

##### 成功响应：

    {
        'code': 200
        'msg': '请求成功'
    }