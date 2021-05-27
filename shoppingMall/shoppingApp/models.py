from django.db import models
from django.utils import timezone
# Create your models here.
class UserAccounts(models.Model):
    user_id = models.CharField(max_length=100)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    user_address = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_phone = models.IntegerField(null=True)


class address(models.Model):
    accounts = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, null=True)
    
    title = models.CharField(max_length=200)
    post_num= models.CharField(max_length=200,null=True)
    road_address=models.CharField(max_length=200,null=True)
    detail_address=models.TextField()
    post_name=models.CharField(max_length=20,null=True)
    post_phonenum=models.IntegerField(null=True)
    is_default = models.BooleanField(default=False,null=True)


  
    def __str__(self):
        return self.title
    
