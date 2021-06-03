# Generated by Django 3.2 on 2021-06-03 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_user', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('total_price', models.IntegerField()),
                ('total_quantity', models.IntegerField()),
                ('order_state', models.CharField(choices=[('order_continue', 'order_continue'), ('order_cancle', 'order_cancle'), ('pay_cancle', 'pay_cancle'), ('pay_complete', 'pay_complete'), ('shipping', 'shipping'), ('shipping_complete', 'shipping_complete'), ('order_complete', 'order_complete')], max_length=20)),
                ('total_shipping_fee', models.IntegerField()),
                ('shipping_address', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('rings', 'rings'), ('glasses', 'glasses'), ('hats', 'hats'), ('necklace', 'necklace')], max_length=20, null=True)),
                ('product_id', models.IntegerField()),
                ('product_title', models.CharField(max_length=500)),
                ('shipping_fee', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderApp.order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
