# Generated by Django 5.0 on 2024-04-02 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_utilisateurs', '0003_utilisateur_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='type',
            field=models.CharField(choices=[('Agent', 'Agent'), ('Prestataire', 'Prestataire'), ('Autre', 'Autre')], default='Agent', max_length=20),
        ),
        migrations.CreateModel(
            name='Prestataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fonction', models.CharField(blank=True, max_length=100, null=True)),
                ('employeur', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employes', to='gestion_utilisateurs.utilisateur')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateurs.utilisateur')),
            ],
        ),
    ]