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