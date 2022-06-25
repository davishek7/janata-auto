# Generated by Django 3.2 on 2022-06-21 04:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarrantyClaim',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('Select Status', ''), ('Received', 'Received'), ('Send to Company', 'Send to Company'), ('Returned_OK', 'Returned OK'), ('F.O.C.', 'F.O.C.')], max_length=50, null=True)),
                ('received_date', models.DateField(blank=True, null=True)),
                ('send_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('handover_date', models.DateField(blank=True, null=True)),
                ('transport', models.CharField(blank=True, choices=[('Select Status', ''), ('Dealer Vehicle', 'Dealer Vehicle'), ('Bus', 'Bus')], max_length=50, null=True)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.sale')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
    ]