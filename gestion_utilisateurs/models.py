from django.db import models
from django.contrib.auth.models import User


class Utilisateur(User):
    profil = models.ImageField(upload_to='profil/', null=True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    TYPE = (
        ('Agent', 'Agent'),
        ('Prestataire', 'Prestataire'),
        ('Autre','Autre')
    )
    type = models.CharField(max_length=20, choices=TYPE, default=TYPE[0][0])    
    phone = models.CharField(max_length=20, null=True, blank=True)
    fonction = models.CharField(max_length=100, null=True, blank=True)
    entreprise = models.ForeignKey('gestions_formations.Entreprise', on_delete=models.CASCADE, null=True)
    symboles_cibles = models.CharField(max_length=500, null=True, blank=True)
    #chanp pour les lecteur nfc et qr code

    nfcTag = models.CharField(max_length=120, null=True, blank=True)
    qrTag  = models.CharField(max_length=120, null=True, blank=True)

    def get_username(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.get_username()
    
class Prestataire(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    formation = models.OneToOneField('gestions_formations.Formation', related_name='prestataires', blank=True , on_delete=models.CASCADE)
    
    