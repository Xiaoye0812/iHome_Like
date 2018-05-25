
### 城区和房屋设施接口

#### request请求1

    GET /house/faci_area/

#### params参数

#### response响应

##### 成功响应1：

    {
        'code': 200
        'facility_list':[
            {
                'id': 设施id,
                'name': 设施名称,
                'css': 设施图标
            },
        ],
        'area_list':[
            {
                'id': 城区id,
                'name': 城区名
            }
        ]
    }

##### 失败响应：

    {
        'code': 900,
        'msg': '访问数据库失败'
    }


#### request请求2

    GET /house/faci/

#### params参数

#### response响应

##### 成功响应1：

    {
        'code': 200
        'facility_list':[
            {
                'id': 设施id,
                'name': 设施名称,
                'css': 设施图标
            },
        ]
    }

##### 失败响应：

    {
        'code': 900,
        'msg': '访问数据库失败'
    }


#### request请求1

    GET /house/area/

#### params参数

#### response响应

##### 成功响应1：

    {
        'code': 200
        'area_list':[
            {
                'id': 城区id,
                'name': 城区名
            }
        ]
    }

##### 失败响应：

    {
        'code': 900,
        'msg': '访问数据库失败'
    }