from django.db import models

# Create your models here.

#model de messagerie 
class Message(models.Model):
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    auteur = models.CharField(max_length=200)
    destinataire = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/', null=True, verbose_name="Fichier", blank=True)
    def __str__(self):
        return self.auteur