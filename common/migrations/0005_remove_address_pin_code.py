# Generated by Django 3.2 on 2022-06-25 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='pin_code',
        ),
    ]