# Generated by Django 2.2.24 on 2025-03-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_owner_deprecated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_deprecated',
        ),
    ]
