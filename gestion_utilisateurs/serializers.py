from rest_framework import serializers
from .models import Utilisateur, Prestataire
from gestions_formations.serializers import FormationSerializer
from gestions_formations.models import Entreprise
from gestions_formations.serializers import EntrepriseSerializer

class PrestataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestataire
        fields = ('formation',)  # Ajoutez ici les champs spécifiques aux prestataires que vous souhaitez inclure dans le sérialiseur

class UtilisateurSerializer(serializers.ModelSerializer):
    prestataire = PrestataireSerializer(source='prestataire_set', read_only=True)
    formation = serializers.SerializerMethodField()
    entreprise = EntrepriseSerializer( read_only=True)
    class Meta:
        model = Utilisateur
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_naissance', 'address', 'type', 'phone', 'profil', 'fonction', 'entreprise', 'qrTag', 'nfcTag', 'prestataire', 'formation')

    def get_formation(self, obj):
        if obj.type == 'Prestataire' and hasattr(obj, 'prestataire') and obj.prestataire.formation:
            return FormationSerializer(obj.prestataire.formation).data
        else:
            return None