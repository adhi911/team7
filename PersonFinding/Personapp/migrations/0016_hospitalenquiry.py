# Generated by Django 5.1.4 on 2025-02-20 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personapp', '0015_stationenquiry_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('current_date', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personapp.hospital')),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Personapp.login')),
            ],
        ),
    ]
