# Generated by Django 5.0 on 2024-05-01 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestions_formations', '0015_alter_formation_validite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='symboles_cibles',
        ),
        migrations.AlterField(
            model_name='formation',
            name='validite',
            field=models.DateField(default=datetime.datetime(2025, 5, 1, 10, 11, 55, 308075, tzinfo=datetime.timezone.utc)),
        ),
    ]
