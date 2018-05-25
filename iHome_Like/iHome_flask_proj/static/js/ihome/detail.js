function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
    var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    });
    $(".book-house").show();
});

$(function () {
    var current_url = document.URL;
    var str_list = current_url.split('/');
    var house_id = str_list[str_list.length-2].split('=')[1];
    console.log(house_id);
    $.get('/house/detailinfo/' + house_id + '/', function (result) {
        if (result.code === 200) {
            var house = result.house_dict;
            var images = house.images;
            for (var i=0; i<images.length; i++){
                $('.swiper-wrapper').append(
                    $('<li>').attr('class', "swiper-slide").append(
                        $('<img>').attr('src', images[i])));
            }
            $('.house-price > span').text(house.price);
            $('.house-title').text(house.title);
            $('.landlord-pic').html('<img src="' + house.user_avatar + '">');
            $('.landlord-name > span').text(house.user_name);
            $('.house-info > h3').text(house.area);
            $('#house_address > li').text(house.address);
            $('.icon-house').next()
                .append($('<h3>').text('出租' + house.room + '间'))
                .append($('<p>').text('房屋面积:' + house.acreage + '平米'))
                .append($('<p>').text('房屋户型:' + house.unit));
            $('.icon-user').next().append($('<h3>').text('宜住' + house.capacity + '人'));
            $('.icon-bed').next()
                .append($('<h3>').text('卧床配置'))
                .append($('<p>').text(house.beds));
            $('#house_deposit').text(house.deposit);
            $('#house_min_days').text(house.min_days);
            $('#house_max_days').text(house.max_days===0?'无限制':house.max_days);
            var facility_list = house.facilities;
            for (var i=0; i<facility_list.length; i++){
                var facility = facility_list[i];
                $('.house-facility-list')
                    .append($('<li>')
                        .append($('<span>')
                            .attr('class', facility.css)).append(facility.name));
            }
            if (result.booking === 0){
                $('.book-house').hide();
            }else {
                $('.book-house').show();
            }
            $('.book-house').attr('href', '/house/booking/?id=' + house_id + '/');
        }

        var mySwiper = new Swiper ('.swiper-container', {
            loop: true,
            autoplay: 2000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            paginationType: 'fraction'
        });
    })
});

// <h3>出租6间</h3>
// <p>房屋面积:200平米</p>
// <p>房屋户型:三室两厅两卫</p>

// <li class="swiper-slide"><img src="/static/images/home02.jpg"></li>
// <li class="swiper-slide"><img src="/static/images/home03.jpg"></li>

/*
<li><span class="wirelessnetwork-ico"></span>无线网络</li>
<li><span class="shower-ico"></span>热水淋浴</li>
<li><span class="aircondition-ico"></span>空调</li>
<li><span class="heater-ico"></span>暖气</li>
<li><span class="smoke-ico"></span>允许吸烟</li>
<li><span class="drinking-ico"></span>饮水设备</li>
<li><span class="brush-ico"></span>牙具</li>
<li><span class="soap-ico"></span>香皂</li>
<li><span class="slippers-ico"></span>拖鞋</li>
<li><span class="toiletpaper-ico"></span>手纸</li>
<li><span class="towel-ico"></span>毛巾</li>
<li><span class="toiletries-ico"></span>沐浴露、洗发露</li>
<li><span class="icebox-ico"></span>冰箱</li>
<li><span class="washer-ico"></span>洗衣机</li>
<li><span class="elevator-ico"></span>电梯</li>
<li><span class="iscook-ico"></span>允许做饭</li>
<li><span class="pet-ico"></span>允许带宠物</li>
<li><span class="meet-ico"></span>允许聚会</li>
<li><span class="accesssys-ico"></span>门禁系统</li>
<li><span class="parkingspace-ico"></span>停车位</li>
<li><span class="wirednetwork-ico"></span>有线网络</li>
<li><span class="tv-ico"></span>电视</li>
<li><span class="jinzhi-ico"></span>浴缸</li>
*/