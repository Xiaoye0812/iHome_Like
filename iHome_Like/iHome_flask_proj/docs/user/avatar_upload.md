
### 上传头像接口

#### request请求

    POST /user/profile/

#### params参数

#### response响应

##### 失败响应1：

    {
        'code': 1006,
        'msg': '上传图片格式不正确'
    }

##### 失败响应2：

    {
        'code': 902,
        'msg': '登录超时'
    }

##### 成功响应：

    {
        'code': 200
        'msg': '请求成功'
    }