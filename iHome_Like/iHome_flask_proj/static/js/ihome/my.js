function logout() {
    $.get("/user/logout/", function(data){
        if (0 === data.code) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.get('/user/user/', function (result) {
        if (result.code === 200){
            $('#user-mobile').html(result.user.phone);
            $('#user-name').html(result.user.name);
            $('#user-avatar').attr('src', result.user.avatar);
        }
    });
})