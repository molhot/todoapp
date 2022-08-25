repass_button = document.getElementById('repass_mail')

repass_button.onclick = function(){
    mailaddress = document.getElementById('mail').value;
    if(mailaddress == ''){
        alert('メールアドレスを入力してください');
    }else{
        url = 'repass_mail/' + mailaddress + '/'; 
        location.href=url;
    }
} 