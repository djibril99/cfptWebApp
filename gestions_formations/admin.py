from django.contrib import admin
from .models import *

# Register your models here.

class FormationAdmin(admin.ModelAdmin):
    list_display =[field.name for field in Formation._meta.fields]



class EntrepriseAdmin(admin.ModelAdmin):
    list_display =[field.name for field in Entreprise._meta.fields]


admin.site.register(Formation, FormationAdmin)
admin.site.register(Entreprise, EntrepriseAdmin)