# Generated by Django 2.2.5 on 2022-08-15 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20220815_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='gusets',
            new_name='guests',
        ),
    ]
