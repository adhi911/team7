# Generated by Django 5.1.4 on 2025-01-10 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationid', models.CharField(max_length=50, unique=True)),
                ('addressline1', models.CharField(max_length=250)),
                ('addressline2', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=200)),
                ('contactno', models.CharField(max_length=200)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personapp.login')),
            ],
        ),
    ]
