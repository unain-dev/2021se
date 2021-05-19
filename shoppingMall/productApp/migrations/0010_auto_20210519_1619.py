# Generated by Django 3.2.2 on 2021-05-19 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0009_auto_20210518_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('status', models.IntegerField(choices=[(0, 'under 10000'), (1, '10000-19990'), (2, '20000-29990'), (3, '30000-39990'), (4, '40000-49990'), (5, 'up to 50000')], default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productApp.product')),
            ],
        ),
    ]
