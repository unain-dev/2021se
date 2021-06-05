from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class question(models.Model):
    CATEGORY_CHOICES=(
        ('상품', '상품'),
        ('배송', '배송'),
        ('반품/취소', '반품/취소'),
        ('기타', '기타'),
    )

    product_name=models.CharField(max_length=50, default='')
    title=models.CharField(max_length=50)
    content=models.TextField(null=True)
    q_category=models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='')
    pubDate = models.DateTimeField(default=timezone.now)
    is_checked=models.BooleanField(default=False,null=True)
    q_user_id=models.CharField(max_length=50)
    answer=models.TextField(null=True)
