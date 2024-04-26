from django.db import models
from django.utils import timezone
import datetime
from gestion_utilisateurs.models import Utilisateur

class Formation(models.Model):
    libelle = models.CharField(max_length=100)
    symboles_cibles = models.CharField(max_length=100, null=True, blank=True)
    validite = models.DateField(default=(timezone.now() + datetime.timedelta(days=365)))
    #prestataires = models.ManyToManyField(Utilisateur , related_name='formations', blank=True)
    #date_debut = models.DateField(default=timezone.now)
    #la duree est de 3 mois par defaut
    #date_fin = models.DateField( null=True) #default=(timezone.now() + datetime.timedelta(days=90)) 

    def __str__(self):
        return self.libelle
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"




class Entreprise(models.Model):
    nom = models.CharField(max_length=100)
    #description = models.TextField()
    #adresse = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    #email = models.EmailField(max_length=100, null=True, blank=True)
    #logo = models.ImageField(upload_to='uploads/', null=True, verbose_name="Logo", blank=True)
    #une entreprise peut avoir plusieurs utilisateurs
    #utilisateurs = models.ManyToManyField(Utilisateur, related_name='entreprises', blank=True)
    
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"