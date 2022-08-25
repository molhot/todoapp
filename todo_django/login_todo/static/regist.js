var check_txt = '';

var button = document.getElementById('registbutton');

button.onclick = function(){
    var result = window.confirm('登録して問題なければ送信ボタンのクリックをお願いします');
    if(result){
        let mailaddress = document.getElementById('mail').value;
        let password = document.getElementById('pass').value;
        if(mailaddress == '' | password == ''){
            alert('メールアドレス、パスワードが入力できていません');
        }else if(password.length < 8){
            alert('パスワードの長さが要件を満たしていません');
        }else{
            format = 
            '<input type="submit" value="登録" id="regist_button_hide">';

            regist_inner = document.getElementById('regist_check_button_text_id');
            regist_inner.innerHTML = format;
            document.getElementById('regist_button_hide').click();
        }
    }
}