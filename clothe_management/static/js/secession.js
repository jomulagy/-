
$('.secession_btn').click(function () {
    let userid = $(".userId").val();
    let userpwd = $(".userPwd").val();
    checkUser(userid,userpwd);
});

function checkUser(userid,userpwd){
   console.log(userid,userpwd);
}
