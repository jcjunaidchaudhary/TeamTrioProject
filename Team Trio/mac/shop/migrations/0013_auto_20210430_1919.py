# Generated by Django 2.2.12 on 2021-04-30 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210430_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='zip_code',
            new_name='pin_code',
        ),
    ]