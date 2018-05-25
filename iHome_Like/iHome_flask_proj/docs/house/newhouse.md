
### 新增房源接口

#### request请求

    POST /house/newhouse/

#### params参数

    area_id int 地区编号
    title str 标题
    price int 每晚价格 单位：分
    address str 具体地址
    room_count int 房间数
    acreage int 房屋面积
    unit str 房屋配置
    capacity int 可住人数
    beds str 床配置
    deposit int 房屋押金
    min_days int 最少可住天数
    max_days int 最大可住天数 0为无限制
    facility list 房屋设施编号

#### response响应

##### 成功响应1：

    {
        'code': 200
        'msg': '发布成功'
    }

##### 失败响应：

    {
        'code': 900,
        'msg': '服务器出错'
    }