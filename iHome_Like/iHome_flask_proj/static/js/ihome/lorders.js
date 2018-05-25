//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $.get('/order/mylorders/', function (result) {
        if (result.code === 200) {
            var orderlist = template('orders_li', {orders:result.order_list});
            $('.orders-list').html(orderlist);
            $(".order-accept").on("click", function(){
                var orderId = $(this).parents("li").attr("order-id");
                $(".modal-accept").attr("order-id", orderId);

            });
            $(".order-reject").on("click", function(){
                var orderId = $(this).parents("li").attr("order-id");
                $(".modal-reject").attr("order-id", orderId);
            });
        }
    });
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);

    $('.modal-accept').click(function () {
        $.ajax({
            url: '/order/accept/',
            type: 'POST',
            data: {'order_id': $(this).attr('order-id')},
            dataType: 'json',
            success: function (result) {
                if (result.code === 200) {
                    alert('接单成功');
                    $('.order-operate').hide();
                    $('#accept-modal').modal('hide');
                    // $('.modal-backdrop').css('display', 'None');
                    // $('#accept-modal').hide();
                }
            },
            error: function () {
                alert('接单失败');
            }
        });
    });
    $('.modal-reject').click(function () {
        var reject_comment = $('#reject-reason').text();
        $.ajax({
            url: '/order/reject/',
            type: 'POST',
            data: {'order_id': $(this).attr('order-id'), 'comment': reject_comment},
            dataType: 'json',
            success: function (result) {
                if (result.code === 200) {
                    alert('拒接成功');
                    $('.order-operate').hide();
                    $('#reject-modal').modal('hide');
                    // $('.modal-backdrop').css('display', 'None');
                    // $('#reject-modal').hide();
                }
            },
            error: function () {
                alert('拒接失败');
            }
        });
    });

});