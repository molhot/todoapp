submit_button = document.getElementById('submitbutton');

submit_button.onclick = function(){
    document.passreset_info.action = "reset";
    document.passreset_info.method = "POST";
    document.passreset_info.submit();
}