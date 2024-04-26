from typing import Any
from django import forms
from .models import Utilisateur
from gestions_formations.models import Entreprise

from django.forms.widgets import ClearableFileInput

class ImageInput(ClearableFileInput):
    template_name = 'django/forms/widgets/clearable_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['accept'] = 'image/*'
        return context


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = [ 'first_name', 'last_name', 'email', 'type', 'date_naissance', 'address', 'phone' , 'entreprise', 'fonction','profil']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'email': 'Email',
            'type': 'Type Utilisateur',
            'date_naissance': 'Date de naissance',
            'address': 'Adresse',
            'phone': 'Téléphone', 
            'entreprise': 'Entreprise',
            'fonction': 'Fonction',
            
        }
        widgets = {
            'profil' : forms.TextInput(attrs={'class': 'form-control','type':'file', 'accept':'image/*', 'required' :False}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Saisir son prenom', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Saisir son nom', 'required': True}),
            'type': forms.Select(attrs={'class': 'form-control','placeholder':'Saisir son type', 'required': True}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control' , 'type': 'date','placeholder':'Saisir sa date de naissance', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Saisir son adresse', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Saisir son numéro de téléphone', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Saisir son email', 'required': True}),
            'entreprise': forms.Select(attrs={'class': 'form-control','placeholder':'Saisir son entreprise', 'required': True}),
            'fonction': forms.TextInput(attrs={'class': 'form-control','placeholder':'Saisir sa fonction', 'required': True}),
            
        }




