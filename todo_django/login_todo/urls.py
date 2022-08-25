from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registaccount', views.regist, name='registaccount'),
    path('regist_processing', views.regist_processing, name='regist_process'),
    path('test', views.test, name='test'),
    path('todo', include('todo_app.urls')),
    path('repass', views.repass, name='repass'),
    path('repass_mail/<str:mailaddress>/', views.repass_mail, name='repass_mail'),
    path('repass_mail/<str:mailaddress>/reset', views.passreset, name='reset'),
    path('registedaccount', views.check_your_account, name='registed'),
]