# Generated by Django 3.2.2 on 2021-05-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingApp', '0018_auto_20210525_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_default',
            field=models.BooleanField(default=False, null=True),
        ),
    ]