function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$('#form-auth').submit(function (evt) {
    evt.preventDefault();
    var real_name = $('input[name="real_name"]').val();
    var id_card = $('input[name="id_card"]').val();
    $.ajax({
        url: '/user/updateauth/',
        type: 'POST',
        data: {'real_name': real_name, 'id_card': id_card},
        dataType: 'json',
        success: function (result) {
            if (result.code === 200){
                alert('请求成功');
            }
            else if (result.code === 1007){
                alert('已实名认证，无法更改');
            }
        },
        error: function () {
            alert('请求失败');
        }
    })
})