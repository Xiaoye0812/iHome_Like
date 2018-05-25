function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');

});

$.get('/house/faci_area/', function (result) {
    if (result.code === 200){
        var total_html = '';
        for (var i=0; i<result.area_list.length; i++){
            var area = result.area_list[i];
            var html = '<option value="' + area.id + '">' + area.name + '</option>';
            total_html += html;
        }
        $('#area-id').html(total_html);
        for (var i=0; i<result.facility_list.length; i++) {
            var facility = result.facility_list[i];
            var html = '';
            html += '<div class="checkbox"><label>';
            html += '<input type="checkbox" name="facility" value="' + facility.id + '">'+ facility.name;
            html += '</label></div>';
            $('.house-facility-list').append($('<li>').html(html));
        }
    }
});

$('#form-house-info').submit(function (e) {
    e.preventDefault();
    $(this).ajaxSubmit({
        url: '/house/newhouse/',
        type: 'POST',
        data: $(this).serialize(),
        dataType: 'json',
        success: function (result) {
            if (result.code === 200) {
                $('#form-house-info').hide();
                $('#form-house-image').show();
                $('#house-id').val(result.house_id);
            }
        },
        error: function () {
            alert('请求出错');
        }
    })
});

$('#form-house-image').submit(function (e) {
    e.preventDefault();
    $(this).ajaxSubmit({
        url: '/house/uploadimg/',
        type: 'PUT',
        data: $(this).serialize(),
        processData: false,
        contentType: false,
        success: function (result) {
            if (result.code === 200){
                $('.house-image-cons').append($('<img>').attr('src', result.image_url));
                alert('上传成功');
            }
        },
        error: function () {
            alert('请求错误');
        }
    })
});

// <option value="2">西城区</option>

// <li>
//     <div class="checkbox">
//          <label>
//               <input type="checkbox" name="facility" value="1">无线网络
//          </label>
//     </div>
// </li>