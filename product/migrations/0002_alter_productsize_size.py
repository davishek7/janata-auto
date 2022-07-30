# Generated by Django 3.2 on 2022-07-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(blank=True, choices=[('', 'Select Size'), (500, 500), (800, 800), (900, 900), (1000, 1000), (2, 2), (5, 5), (10, 10)], max_length=255, null=True),
        ),
    ]