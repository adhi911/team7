# Generated by Django 4.2.19 on 2025-02-14 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personapp', '0013_stationenquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stationenquiry',
            old_name='created_at',
            new_name='current_date',
        ),
    ]
