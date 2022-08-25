from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Pass_reset
from django.core.exceptions import ObjectDoesNotExist
import smtplib
import requests
from email.mime.text import MIMEText
from email.utils import formatdate
import random
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def login(request):
    return render(request, 'login_todo_index.html')

def regist(request):
    return render(request, 'registaccount.html')

def regist_processing(request):
    if(request.method == 'POST'):
        print(request.POST)
        mail = request.POST.get('mail')
        password = request.POST.get('pass')
        #登録処理を記載
        try:
            user_info_ = User.objects.get(mailaddress=mail)
        except ObjectDoesNotExist:
            User.objects.create(mailaddress=mail, password=password)
            return redirect('login')
        else:
            return redirect('registed')
    return redirect('login')

def check_your_account(request):
    return render(request, 'registed.html')

def repass(request):
    return render(request, 'repass.html')

def repass_mail(request, mailaddress):
    print(mailaddress)
    try:
        user_table = User.objects.get(mailaddress=mailaddress)
    except ObjectDoesNotExist:
        return render(request, 'mail_not_found.html')
    else:
        #メールアドレスにパスワード再設定用のメールを送る
        pass_number = random.randrange(1000,9000, 1)

        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login('自分のグーグルメールアドレス', 'グーグルのアプリキー')

        msg = MIMEText(str(pass_number))
        msg['Subject'] = 'パスワード再設定'
        msg['From'] = '自分のグーグルメールアドレス'
        msg['To'] = mailaddress
        msg['Date'] = formatdate()

        smtpobj.sendmail('自分のグーグルメールアドレス', mailaddress, msg.as_string())
        smtpobj.close()
        Pass_reset.objects.create(mailinfo=mailaddress, passreset_info=pass_number)
        return render(request, 'repass_set.html')
    return render(request, 'login_todo_index.html')

def passreset(request, mailaddress):
    #ここにパスワード再設定用の関数を置く
    input_resetpass = request.POST.get('secretnumber')
    resetpass = Pass_reset.objects.filter(mailinfo=mailaddress)[0].passreset_info
    print(input_resetpass,resetpass)
    if input_resetpass != resetpass:
        Pass_reset.objects.get(mailinfo=mailaddress).delete()
        return redirect('repass_mail', mailaddress)
    else:
        return render(request, 'reset_pass_end.html')

