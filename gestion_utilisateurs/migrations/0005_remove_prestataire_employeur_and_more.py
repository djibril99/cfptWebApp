# Generated by Django 5.0 on 2024-04-02 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_utilisateurs', '0004_alter_utilisateur_type_prestataire'),
        ('gestions_formations', '0010_alter_formation_symboles_cibles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestataire',
            name='employeur',
        ),
        migrations.RemoveField(
            model_name='prestataire',
            name='fonction',
        ),
        migrations.AddField(
            model_name='prestataire',
            name='formation',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='prestataires', to='gestions_formations.formation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='entreprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestions_formations.entreprise'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='fonction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]