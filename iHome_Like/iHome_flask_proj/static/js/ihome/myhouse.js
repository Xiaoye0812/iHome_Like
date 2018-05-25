$(document).ready(function(){
    $(".auth-warn").show();
});

$(function () {
    $('#houses-list').hide();
    $('.auth-warn').hide();
    $.get('/house/auth_myhouse/', function (result) {
        if (result.code === 2000) {
            $('#houses-list').hide();
        }
        else if (result.code === 200){
            $('#houses-list').show();
            $('.auth-warn').hide();
            for (var i=0; i<result.house_list.length; i++) {
                var house = result.house_list[i];
                var html = '';
                html += '<a href="/house/detail/?id='+ house.id +'/">';
                html += '<div class="house-title">';
                html += '<h3>房屋ID:'+ house.id + '——' + house.title + '</h3>';
                html += '</div><div class="house-content">';
                html += '<img src="' + house.image + '">';
                html += ' <div class="house-text"><ul>';
                html += '<li>位于：' + house.area + '</li>';
                html += '<li>价格：￥' + (house.price/100) + '/晚</li>';
                html += '<li>发布时间：' + house.create_time + '</li>';
                html += '</ul></div></div></a>';

                $('#houses-list').append($('<li>').html(html));
            }
        }
    });
});



// <li>
//     <a href="/detail.html?id={{house.house_id}}&f=my">
//         <div class="house-title">
//             <h3>房屋ID:1 —— 房屋标题1</h3>
//         </div>
//         <div class="house-content">
//             <img src="/static/images/home01.jpg">
//             <div class="house-text">
//                 <ul>
//                     <li>位于：西城区</li>
//                     <li>价格：￥200/晚</li>
//                     <li>发布时间：2016-11-11 20:00:00</li>
//                 </ul>
//             </div>
//         </div>
//     </a>
// </li>
