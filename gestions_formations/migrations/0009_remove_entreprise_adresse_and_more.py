# Generated by Django 5.0 on 2024-04-02 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestions_formations', '0008_alter_formation_date_fin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='description',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='email',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='entreprise',
            name='utilisateurs',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='date_fin',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='prestataires',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='prix',
        ),
        migrations.AddField(
            model_name='formation',
            name='symboles_cibles',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formation',
            name='validite',
            field=models.DateField(default=datetime.datetime(2025, 4, 2, 18, 52, 58, 38684, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Module',
        ),
    ]
