# Generated by Django 3.2 on 2021-06-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0017_remove_review_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='total_score',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
