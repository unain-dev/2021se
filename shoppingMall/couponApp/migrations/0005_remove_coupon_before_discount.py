# Generated by Django 3.2 on 2021-06-05 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0004_coupon_before_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='before_discount',
        ),
    ]
