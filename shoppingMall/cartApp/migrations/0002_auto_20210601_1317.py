# Generated by Django 3.2 on 2021-06-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_shipping_fee',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='shipping_fee',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
