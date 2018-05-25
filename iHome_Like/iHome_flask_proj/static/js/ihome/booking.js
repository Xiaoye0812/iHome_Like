function hrefBack() {
    history.go(-1);
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

function showErrorMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function(){
    $(".input-daterange").datepicker({
        format: "yyyy-mm-dd",
        startDate: "today",
        language: "zh-CN",
        autoclose: true
    });
    $(".input-daterange").on("changeDate", function(){
        var startDate = $("#start-date").val();
        var endDate = $("#end-date").val();

        if (startDate && endDate && startDate > endDate) {
            showErrorMsg();
        } else {
            var sd = new Date(startDate);
            var ed = new Date(endDate);
            days = (ed - sd)/(1000*3600*24) + 1;
            var price = $(".house-text>p>span").html();
            var amount = days * parseFloat(price);
            $(".order-amount>span").html(amount.toFixed(2) + "(共"+ days +"晚)");
        }
    });
})


$(document).ready(function () {
    var path = location.search;
    var id = path.split('=')[1].split('/')[0];

    $.get('/house/detailinfo/' + id + '/', function (result) {
        if (result.code === 200) {
            var house_booking = template('house_booking', {ohouse:result.house_dict});
            $('.house-info').append(house_booking);
        }
    });

    $('.submit-btn').click(function () {

        var path = location.search;
        id = path.split('=')[1].split('/')[0];

        var start_date = $('#start-date').val();
        var end_date = $('#end-date').val();

        $.ajax({
            url: '/order/',
            type: 'POST',
            data: {'house_id': id, 'start_time': start_date, 'end_time': end_date},
            dataType: 'json',
            success: function (result) {
                if (result.code === 200) {
                    alert('预定成功');
                    location.href = '/';
                }else if (result.code === 3000){
                    alert('选取时间不正确');
                }else if (result.code === 3001){
                    alert('此房源入住人数已满');
                }else if (result.code === 3002){
                    alert('少于最少入住时间');
                }else if (result.code === 3003){
                    alert('大于最大入住时间');
                }else {
                    alert('预定失败')
                }
            },
            error: function () {
                alert('请求失败');
            }
        });
    })
})