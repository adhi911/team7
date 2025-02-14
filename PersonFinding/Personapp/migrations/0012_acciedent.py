# Generated by Django 5.1.4 on 2025-02-13 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personapp', '0011_usercomp_replay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciedent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('currentdate', models.DateField(auto_now_add=True)),
                ('accidentdetails', models.CharField(max_length=200)),
                ('media', models.ImageField(blank=True, upload_to='image')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accidentid', to='Personapp.login')),
            ],
        ),
    ]
