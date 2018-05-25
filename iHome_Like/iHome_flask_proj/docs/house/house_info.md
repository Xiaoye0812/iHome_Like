
### 房源详情接口

#### request请求

    GET /house/detailinfo/xxx/ xxx为house_id

#### params参数

#### response响应

##### 失败响应1：

##### 成功响应：

    {
        'code': 200
        'house_dict': {
            'id': 房源编号,
            'user_avatar': 房东头像,
            'user_name': 房东名称,
            'title': 房源标题,
            'image': 房源图片,
            'area': 地区,
            'price': 每晚价格,
            'create_time': 创建时间,
            'acreage': 面积,
            'unit': 房屋单元,
            'capacity': 可住人数,
            'beds': 床位配置,
            'deposit': 押金,
            'min_days': 最少入住天数,
            'max_days': 最多入住天数,
            'images': [image_url,] 房屋详情图片,
            'facilities': 房屋设施列表,
            'room': 房间数量,
            'order_count': 已下订单数量,
            'address': 详细地址
        }
    }