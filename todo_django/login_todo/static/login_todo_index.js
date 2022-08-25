var loginbutton = document.getElementById('login_button');
loginbutton.onclick = function(){
    document.login_info_form.submit();
}

var re_passbutton = document.getElementById('re_password_button');
re_passbutton.onclick = function(){
    location.href='repass';
}