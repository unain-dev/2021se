# Generated by Django 3.2 on 2021-06-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0005_alter_review_r_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='total_score',
            field=models.IntegerField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default=''),
        ),
    ]