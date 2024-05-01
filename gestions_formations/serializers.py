from rest_framework import serializers
from .models import Formation

from .models import Entreprise


class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = ('id','libelle', 'validite')  # Ajoutez ici les champs spécifiques à la formation que vous souhaitez inclure dans le sérialiseur


class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ('id','nom', 'telephone',)  #