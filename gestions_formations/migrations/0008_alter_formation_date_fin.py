# Generated by Django 5.0 on 2024-02-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestions_formations', '0007_alter_formation_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='date_fin',
            field=models.DateField(null=True),
        ),
    ]
