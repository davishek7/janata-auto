# Generated by Django 3.2 on 2022-07-29 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_alter_sale_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerdetail',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]