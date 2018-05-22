function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$('#form-avatar').submit(function upload_image(evt) {
    evt.preventDefault();
    var formdata = new FormData($('#form-avatar')[0]);
    $.ajax({
        url: '/user/profile/',
        type: 'POST',
        data: formdata,
        processData: false,
        contentType: false,
        success: function (result) {
            if (result.code === 200){
                alert('上传成功');
                $("#user-avatar").attr('src', result.url);
            }
        },
        error: function () {
            alert('上传失败')
        }
    })
});

$('#form-name').submit(function (evt) {
    evt.preventDefault();
    $('.error-msg').hide();
    var name = $('input[name="name"]').val();
    $.ajax({
        url: '/user/profile/name/',
        type: 'POST',
        data: {'name': name},
        dataType: 'json',
        success: function (result) {
            if (result.code === 200){
                alert('修改成功');
            }else if (result.code === 1008){
                alert('用户名已存在，无法更改');
                $('.error-msg').show();
            }
        },
        error: function () {
            alert('请求出错');
        }
    })
});