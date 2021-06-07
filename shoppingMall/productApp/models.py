from django.db import models
from django.utils import timezone
from django.urls import reverse

class P_range(object):
    OPTION_0, OPTION_1, OPTION_2, OPTION_3, OPTION_4, OPTION_5 = range(0, 6)

    CHOICES = (
        (OPTION_0, 'under 10000'),
        (OPTION_1, '10000-19990'),
        (OPTION_2, '20000-29990'),
        (OPTION_3, '30000-39990'),
        (OPTION_4, '40000-49990'),
        (OPTION_5, 'up to 50000'),
    )

class product(models.Model):
    CATEGORY_CHOICES=(
        ('rings', 'rings'),
        ('glasses', 'glasses'),
        ('hats', 'hats'),
        ('necklace', 'necklace'),
    )

    product_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    thumbnail=models.ImageField(upload_to='thumbnail/', blank=True, null=True)
   
    price=models.IntegerField()
    description=models.TextField()
    stock=models.IntegerField()
    salesamount=models.IntegerField()
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    pubDate = models.DateTimeField(default=timezone.now)
    published=models.BooleanField(default=True)
    shipping_fee=models.IntegerField()

    status = models.IntegerField(
        choices=P_range.CHOICES,
        default=P_range.OPTION_0
    )



    
class Photo(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    
    def __str__(self):
      return str(self.product.name)

class review(models.Model):
    CATEGORY_CHOICES1=(
        ('적극추천', '적극추천'),
        ('추천','추천'),
        ('비추천', '비추천'),
    )
    CATEGORY_CHOICES2=(
        ('빠름', '빠름'),
        ('보통','보통'),
        ('느림', '느림'),
    )
   
    num_choices = zip( range(1,6), range(1,6) ) 


    r_product= models.ForeignKey(product, on_delete=models.CASCADE, null=True,default='')
    r_stage=models.CharField(max_length=20, choices=CATEGORY_CHOICES1, default='')
    shipping_score=models.CharField(max_length=20, choices=CATEGORY_CHOICES2, default='')
    r_content=models.TextField(null=True)
    r_user_id=models.CharField(max_length=50,null=True)
    update_at=models.DateTimeField(auto_now_add=True)
    total_score= models.IntegerField(choices=num_choices, blank=True)
   
    

