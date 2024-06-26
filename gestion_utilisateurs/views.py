from django.shortcuts import render, redirect
from django.http import HttpResponse  , HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import loader
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


from .serializers import * #import forms
from .forms import UtilisateurForm
from .models import Utilisateur , Prestataire

import json

import openpyxl
from io import BytesIO


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
    
#recevoir une image et l'associer a un utilisateur
@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES['file'] and 'userId' in request.POST:
        uploaded_file = request.FILES['file']
        user_id = request.POST['userId']
        user = Utilisateur.objects.get(id=user_id)
        user.profil = uploaded_file
        user.save()
        return HttpResponse('File uploaded and saved successfully for user {}'.format(user_id))
    return HttpResponse('Failed to upload file')

#telecharger toute les donnees sur un fichier excel


def excel_download_view(request):
    # Récupérer les données du modèle
    queryset = Prestataire.objects.all()

    # Créer un nouveau classeur Excel
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Ajouter des en-têtes de colonne
    headers = ["Identifiant", "Date de Naissance", "Prenom", "Nom", "Entreprise", "Telephone", "Fonction", "Date d'expiration", "Titre Habilitation", "CNI"]
    worksheet.append(headers)

    # Ajouter les données du modèle au classeur Excel
    for prestataire in queryset:
        user = prestataire.utilisateur
        formation = prestataire.formation
        row = [user.id, user.date_naissance.strftime('%d/%m/%Y'), user.first_name , user.last_name, user.entreprise.nom, user.phone, user.fonction, formation.validite.strftime('%d/%m/%Y'), user.symboles_cibles, user.cni]
        worksheet.append(row)

    # Créer un flux BytesIO pour stocker le fichier Excel
    excel_file = BytesIO()
    workbook.save(excel_file)
    excel_file.seek(0)

    # Créer une réponse HTTP pour le fichier Excel
    response = HttpResponse(
        excel_file,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="donnees.xlsx"'

    return response
