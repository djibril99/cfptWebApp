from django import forms
from .models import Formation

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['libelle', 'validite']
        labels = {
            'libelle': 'libelle',
            'validite': 'Validité',

        }
        
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control','placeholder':'Saisir le libelle de la formation', 'required': True}),
            'validite': forms.DateInput(attrs={'class': 'form-control' , 'type': 'date','placeholder':'Saisir la validité de la formation', 'required': True}),
        }
