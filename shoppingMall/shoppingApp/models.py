from django.db import models

# Create your models here.
class UserAccounts(models.Model):
    user_id = models.CharField(max_length=100)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    user_address = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_phone = models.IntegerField(null=True)


class address(models.Model):
    UserAccounts = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    body=models.TextField()