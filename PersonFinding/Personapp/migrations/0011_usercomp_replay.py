# Generated by Django 5.1.4 on 2025-02-13 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personapp', '0010_usercomp_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomp',
            name='replay',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
