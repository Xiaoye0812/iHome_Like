function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}
$.get('/user/updateauth/', function (result) {
    if (result.code === 200) {
        $('#real-name').val(result.id_name);
        $('#id-card').val(result.id_card);
        if (result.id_name && result.id_card) {
            $('.btn-success').hide();
        }
    }
});

$('#form-auth').submit(function (evt) {
    evt.preventDefault();
    $('.error-msg').hide();
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
            else{
                alert('实名认证出错');
                $('.error-msg').html('<i class="fa fa-exclamation-circle"></i>' + result.msg)
                $('.error-msg').show();
            }
        },
        error: function () {
            alert('请求失败');
        }
    })
})