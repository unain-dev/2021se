# Generated by Django 3.2 on 2021-05-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingApp', '0004_auto_20210504_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccounts',
            name='user_address',
            field=models.CharField(max_length=100),
        ),
    ]
