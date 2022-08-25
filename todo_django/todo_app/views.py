from django.shortcuts import render
from login_todo.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def todo(request):
    mailaddress = request.POST.get("mailsddress_info")
    password = request.POST.get("password_info")
    try:
        user_mailaddress = User.objects.get(mailaddress=mailaddress)
        print(user_mailaddress)
    except ObjectDoesNotExist:
        print("アカウントがありません")
        return render(request, 'fail_login_page.html')
    return render(request, 'todo_page.html')

