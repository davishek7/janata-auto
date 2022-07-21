# Generated by Django 3.2 on 2022-07-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warrantyclaim',
            name='handover_date',
        ),
        migrations.RemoveField(
            model_name='warrantyclaim',
            name='received_date',
        ),
        migrations.RemoveField(
            model_name='warrantyclaim',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='warrantyclaim',
            name='send_date',
        ),
        migrations.AddField(
            model_name='warrantyclaim',
            name='claim_status',
            field=models.CharField(blank=True, choices=[('Select Status', ''), ('Received', 'Received'), ('Send to Company', 'Send to Company'), ('Returned_OK', 'Returned OK'), ('F.O.C.', 'F.O.C.'), ('Handover to Customer', 'Handover to Customer')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='warrantyclaim',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='warrantyclaim',
            name='transport',
            field=models.CharField(blank=True, choices=[('Select Transport', ''), ('Dealer Vehicle', 'Dealer Vehicle'), ('Bus', 'Bus')], max_length=50, null=True),
        ),
    ]