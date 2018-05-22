
### 更新用户名接口

#### request请求

    POST /user/name/

#### params参数

    name str 新用户名

#### response响应

##### 失败响应1：

    {
        'code': 902,
        'msg': '登录超时'
    }

##### 失败响应2：

    {
        'code': 1008
        'msg': '用户名已存在，无法更改'
    }

##### 成功响应：

    {
        'code': 200
        'msg': '请求成功'
    }