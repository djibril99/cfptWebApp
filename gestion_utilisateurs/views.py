from django.shortcuts import render, redirect
from django.http import HttpResponse  , HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import loader
from django.db.models import Q

from .serializers import * #import forms
from .forms import UtilisateurForm
from .models import Utilisateur , Prestataire

import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    #recureperer le login et le password
    username = request.POST.get('login')
    password = request.POST.get('password')
    #verifier si le user existe
    user = User.objects.filter(username=username, password=password) if username and password else None
    if user:
        return redirect(request , 'gestion_formations:index')
    else:
        context = { 'error': 'Login ou mot de passe incorrect' }
        return render(request, 'index.html', context)

def register(request):
    return render(request, 'register.html')

def logout(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')


def addUser(request):
    context = {}
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            form = UtilisateurForm()
            context = { 'success': 'Utilisateur ajouté avec succès' , 'form': form }

            return render(request, 'Admin/addUser.html', context)
        else:
            listeErreurs = form.errors
            context = { 'form': form , 'error': listeErreurs }

    else:
        form = UtilisateurForm()
        context = { 'form': form }
    return render(request, 'Admin/addUser.html', context)

def delete(request, utilisateur_id):
    utilisateur = Utilisateur.objects.filter(id=utilisateur_id).first()
    if utilisateur:
        utilisateur.delete()
    return redirect('gestion_utilisateurs:listePrestataire')

def listePrestataire(request):
    utilisateurs = Utilisateur.objects.filter(type='Prestataire')
    context = { 'utilisateurs': utilisateurs }
    return render(request, 'Admin/listeUser.html', context)

def listeAgent(request):
    utilisateurs = Utilisateur.objects.filter(type='Agent')
    context = { 'utilisateurs': utilisateurs }
    return render(request, 'Admin/listeUser.html', context)



#api serialiser

def serialiserGetUser(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    data= serializer.data
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def serialiserGetUserById(request, utilisateur_id):
    utilisateur = Utilisateur.objects.filter(id=utilisateur_id).first()
    serializer = UtilisateurSerializer(utilisateur)
    data = serializer.data
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


def serialiserGetUserByWord(request, word):


    utilisateurs = Utilisateur.objects.filter(
        Q(username__icontains=word) |
        Q(first_name__icontains=word) |
        Q(last_name__icontains=word) |
        Q(email__icontains=word) |
        Q(address__icontains=word) |
        Q(type__icontains=word) |
        Q(phone__icontains=word) 
    )
    
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    data = serializer.data
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

#api pour les lectruer nfc et qr code
#assoction d'un utilisateur a un tag nfc
def SetNfcTag(request, utilisateur_id, tag):
    utilisateur = Utilisateur.objects.filter(id=utilisateur_id).first()
    utilisateur.nfcTag = tag
    utilisateur.save()
    return HttpResponse("ok", content_type='application/json')
def SetQrTag(request, utilisateur_id, tag):
    utilisateur = Utilisateur.objects.filter(id=utilisateur_id).first()
    utilisateur.qrTag = tag
    utilisateur.save()
    return HttpResponse("ok", content_type='application/json')

def readNfcTag(request, tag):
    utilisateur = Utilisateur.objects.filter(nfcTag=tag).first()
    if utilisateur:
        serializer = UtilisateurSerializer(utilisateur)
        data = serializer.data
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse("not found", content_type='application/json')
def readQrTag(request, tag):
    utilisateur = Utilisateur.objects.filter(qrTag=tag).first()
    if utilisateur:
        serializer = UtilisateurSerializer(utilisateur)
        data = serializer.data
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse("not found", content_type='application/json')
    

def upload_file(request):
    if request.method == 'POST' and request.FILES['file'] and 'userId' in request.POST:
        uploaded_file = request.FILES['file']
        user_id = request.POST['userId']
        user = Utilisateur.objects.get(id=user_id)
        user.image = uploaded_file
        user.save()
        return HttpResponse('File uploaded and saved successfully for user {}'.format(user_id))
    return HttpResponse('Failed to upload file')