# Generated by Django 3.2 on 2022-07-20 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_productsize_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'product categories'},
        ),
    ]
