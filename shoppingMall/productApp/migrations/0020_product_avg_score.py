# Generated by Django 3.2 on 2021-06-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0019_review_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg_score',
            field=models.IntegerField(default='0'),
        ),
    ]