# Generated by Django 3.2 on 2021-06-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount_category',
            field=models.CharField(choices=[('rings', 'rings'), ('glasses', 'glasses'), ('hats', 'hats'), ('necklace', 'necklace')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='min_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]