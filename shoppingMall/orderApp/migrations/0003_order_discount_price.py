# Generated by Django 3.2 on 2021-06-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0002_order_coupon_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
