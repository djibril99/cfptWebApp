from django.urls import path
from . import views

app_name = 'gestion_utilisateurs'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('settings/', views.settings, name="settings"),
    path('addUser/', views.addUser, name="addUser"),
    path('delete/<int:utilisateur_id>/', views.delete, name="delete"),
    path('listePrestataire/', views.listePrestataire, name="listePrestataire"),
    path('listeAgent/', views.listeAgent, name="listeAgent"),


    #write nfc and qr code
    path('writeNfc/<int:utilisateur_id>/<str:tag>/', views.SetNfcTag, name="writeNfc"),
    path('writeQr/<int:utilisateur_id>/<str:tag>/', views.SetQrTag, name="writeQr"),

    #api
    path('api/utilisateurs/', views.serialiserGetUser, name="utilisateurs"),
    path('api/utilisateurs/<int:utilisateur_id>/', views.serialiserGetUserById, name="utilisateur"),
    path('api/utilisateurs/search/<str:word>/', views.serialiserGetUserByWord, name="searchUser"),
    path('api/readByNfc/<str:tag>/', views.readNfcTag, name="readNfc"),
    path('api/readByQr/<str:tag>/', views.readQrTag, name="readQr"),
]