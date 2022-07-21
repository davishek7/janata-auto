# Generated by Django 3.2 on 2022-06-18 18:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('bf492c3f-ce94-4f2b-9456-2f8500753a2f'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Select Type', ''), ('Success', 'success'), ('Warning', 'warning'), ('Info', 'info'), ('Error', 'error')], max_length=255, null=True)),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
    ]
