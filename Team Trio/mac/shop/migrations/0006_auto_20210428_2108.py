# Generated by Django 2.2.12 on 2021-04-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='pin_code',
        ),
        migrations.AddField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
    ]