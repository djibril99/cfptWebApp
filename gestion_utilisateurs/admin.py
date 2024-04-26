from django.contrib import admin
from .models import *
# Register your models here.
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ["profil","date_naissance","address","type","phone","fonction","entreprise","qrTag","nfcTag"]
    


class PrestataireAdmin(admin.ModelAdmin):
    list_display =[field.name for field in Prestataire._meta.fields]

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Prestataire, PrestataireAdmin)