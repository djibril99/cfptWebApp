# Generated by Django 5.0 on 2024-02-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_utilisateurs', '0002_utilisateur_remove_prestataire_user_delete_agent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='profil',
            field=models.ImageField(blank=True, null=True, upload_to='profil/'),
        ),
    ]
