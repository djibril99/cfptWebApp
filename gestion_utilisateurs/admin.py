from django.contrib import admin
from .models import *
# Register your models here.
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","profil","date_naissance","address","type","phone","fonction","entreprise","qrTag","nfcTag"]
    list_editable = ["first_name","last_name","profil","date_naissance","address","type","phone","fonction","entreprise","qrTag","nfcTag"]
    list_display_links = None  # Aucun lien cliquable dans la liste
class PrestataireAdmin(admin.ModelAdmin):
    list_display =[field.name for field in Prestataire._meta.fields]
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "utilisateur":
            # Filtrer le champ utilisateur pour n'afficher que les utilisateurs de type "Prestataire"
            kwargs["queryset"] = Utilisateur.objects.filter(type='Prestataire')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Prestataire, PrestataireAdmin)