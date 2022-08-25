from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user_info'
    
    mailaddress = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.mailaddress

class Pass_reset(models.Model):
    class Meta:
        db_table = 'for_passreset_info'

    mailinfo = models.CharField(max_length=100)
    passreset_info = models.IntegerField()

    def __str__(self):
        return self.mailinfo
