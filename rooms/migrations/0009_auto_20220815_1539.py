# Generated by Django 2.2.5 on 2022-08-15 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20220815_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
