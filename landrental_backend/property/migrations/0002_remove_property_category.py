# Generated by Django 5.0.2 on 2024-08-10 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
    ]
