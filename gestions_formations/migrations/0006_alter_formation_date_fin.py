# Generated by Django 5.0 on 2024-02-19 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestions_formations', '0005_alter_formation_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='date_fin',
            field=models.DateField(default=datetime.datetime(2024, 5, 19, 10, 45, 38, 287448, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
