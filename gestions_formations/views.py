from django.shortcuts import render
from .models import Formation
from .forms import FormationForm

# Create your views here.

def all_formations(request):
    formations = Formation.objects.all()
    context = { 'formations': formations }
    form = FormationForm()
    context['form'] = form

    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            context['success'] = "Formation ajoutée avec succès"
        else:
            context['error'] = "Erreur lors de l'ajout de la formation"
    return render(request, 'all_formations.html', context)
    

def detail_formation(request, formation_id):
    formation = Formation.objects.filter(id=formation_id).first()
    context = { 'formation': formation }
    return render(request, 'detail_formation.html', context)


def delete(request, formation_id):
    formation = Formation.objects.filter(id=formation_id).first()
    formation.delete()
    return all_formations(request)


    