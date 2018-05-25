
### 上传房源图片接口

#### request请求

    PUT /house/uploadimg/

#### params参数

    house_image file 头像

#### response响应

##### 失败响应1：

    {
        'code': 2001,
        'msg': '上传图片格式不正确'
    }

##### 失败响应2：

    {
        'code': 900,
        'msg': '访问数据库失败'
    }

##### 成功响应：

    {
        'code': 200
        'msg': '请求成功'
    }