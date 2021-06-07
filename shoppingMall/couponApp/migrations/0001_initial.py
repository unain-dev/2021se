# Generated by Django 3.2 on 2021-06-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_id', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('dueDate', models.DateTimeField()),
                ('activation', models.BooleanField()),
                ('type', models.CharField(choices=[('price', 'price'), ('percentage', 'percentage')], max_length=20)),
                ('discount_percentage', models.IntegerField()),
                ('discount_price', models.IntegerField()),
            ],
        ),
    ]