from django.contrib import admin
from .models import User, Pass_reset

# Register your models here.
class User_admin(admin.ModelAdmin):
    fields = ['mailaddress', 'password']

class Pass_reset_admin(admin.ModelAdmin):
    fields = ['mailinfo', 'passreset_info']

admin.site.register(User, User_admin)
admin.site.register(Pass_reset, Pass_reset_admin)