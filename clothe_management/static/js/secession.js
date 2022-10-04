
$('.secession_btn').click(function () {
    let pwd = $('.userPwd').val();
    secession_user(user_id, pwd);
});

$('.userPwd').on("keyup",function(key){
    if(key.keyCode==13){
        let pwd = $('.userPwd').val();
    secession_user(user_id, pwd);
    }
});

$('.close-btn').click(function () {
    $('.modal-wrap').css('display', 'none');
    $('.modal').css('display', 'none');
});

$('#modal_return_btn').click(function () {
    $('.modal-wrap').css('display', 'none');
    $('.modal').css('display', 'none');
});

$('#modal_secession_btn').click(function () {

});

function secession_user($userid, $pwd) {
    $.ajax({
        //요청이 전송될 URL 주소
        url: 'http://127.0.0.1:8000/check_pwd/',
        type: "POST",
        dataType: "JSON",
        data: JSON.stringify({
            "id": $userid,
            "pwd": $pwd
        }),
        headers: { "X-CSRFToken": "{{ csrf_token }}" },

        success: function (data) {
            if (data.result == true && data.error=="") {
                $('.modal-wrap').css('display', 'block');
                $('.modal').css('display', 'block');
            }
            else {
                alert(data.error);
            }
        },
        error: function (xhr, textStatus, thrownError) {
            alert(
                "Could not send URL to Django. Error: " +
                xhr.status +
                ": " +
                xhr.responseText
            );
        },
    });
}
