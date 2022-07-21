# Generated by Django 3.2 on 2022-06-26 17:41

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_model_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productsize'),
        ),
    ]
