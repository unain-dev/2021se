# Generated by Django 3.2 on 2021-06-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0004_alter_review_total_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='r_user_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
