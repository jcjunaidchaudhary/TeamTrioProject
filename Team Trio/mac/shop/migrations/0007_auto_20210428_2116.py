# Generated by Django 2.2.12 on 2021-04-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210428_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
    ]