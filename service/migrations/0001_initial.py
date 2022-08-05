# Generated by Django 3.2 on 2022-08-02 06:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryWarrantyClaim',
            fields=[
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('claim_status', models.CharField(blank=True, choices=[('Select Status', ''), ('Received', 'Received'), ('Send to Company', 'Send to Company'), ('Returned_OK', 'Returned OK'), ('F.O.C.', 'F.O.C.'), ('Handover to Customer', 'Handover to Customer')], max_length=50, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=50, null=True)),
                ('transport', models.CharField(blank=True, choices=[('Select Transport', ''), ('Dealer Vehicle', 'Dealer Vehicle'), ('Bus', 'Bus')], max_length=50, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
