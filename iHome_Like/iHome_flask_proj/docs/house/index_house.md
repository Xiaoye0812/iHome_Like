
### 主页展示房源接口

#### request请求

    GET /house/indexhouse/

#### params参数

#### response响应

##### 成功响应1：

    {
        'code': 200
        'house_list':[
            {
                'id': 房源编号,
                'title': 标题,
                'image': 图片,
                'area': 地区,
                'price': 每晚价格,
                'create_time': 创建时间,
                'room': 房屋数量,
                'order_count': 下订单数量,
                'address': 具体地址
            },
        ]
    }

##### 失败响应：

    {
        'code': 900,
        'msg': '数据库访问失败'
    }