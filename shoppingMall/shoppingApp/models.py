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

  
    def __str__(self):
        return self.title

'''
class address(models.Model):
    title       = models.CharField(max_length=200, verbose_name="제목")
    contents    = models.TextField(verbose_name="내용")

    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title

    class Meta:
        db_table            = 'address'
        verbose_name        = '주소'
        verbose_name_plural = '주소'
        '''