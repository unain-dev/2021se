# Generated by Django 3.2 on 2021-06-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartApp', '0002_auto_20210601_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='shipping_fee',
            field=models.IntegerField(null=True),
        ),
    ]
