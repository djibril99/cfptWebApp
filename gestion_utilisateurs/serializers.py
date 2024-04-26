from rest_framework import serializers
from .models import Utilisateur, Prestataire

class PrestataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestataire
        fields = ('formation',)  # Ajoutez ici les champs spécifiques aux prestataires que vous souhaitez inclure dans le sérialiseur

class UtilisateurSerializer(serializers.ModelSerializer):
    prestataire = PrestataireSerializer(source='prestataire_set', read_only=True)

    class Meta:
        model = Utilisateur
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_naissance', 'address', 'type', 'phone', 'profil', 'fonction', 'entreprise', 'qrTag','nfcTag','prestataire')
