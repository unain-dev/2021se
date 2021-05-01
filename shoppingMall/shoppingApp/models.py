from django.db import models

# Create your models here.
class UserAccounts(models.Model):
    user_id = models.CharField(max_length=100)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    user_address = models.TextField()
    user_email = models.CharField(max_length=100)
    user_phone = models.IntegerField(null=True)

def __str__(self):
    return self.user_id


#공지, 이벤트 - 상민
class Notice(models.Model):
    title = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    contents = models.TextField()
    uniqueNumber = models.IntegerField()

class Event(models.Model):
    title = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    contents = models.TextField()
    on_off = models.TextChoices('on','off')
    activation = models.CharField(choices=on_off.choices, max_length=10)
    dueDate = models.DateTimeField()
    uniqueNumber = models.IntegerField()    