
### 获取实名信息接口

#### request请求

    GET /user/updateauth/

#### params参数

#### response响应

##### 失败响应1：

    {
        'code': 902,
        'msg': '登录超时'
    }

##### 成功响应：

    {
        'code': 200,
        'id_name': xxx,
        'id_card': xxx
    }