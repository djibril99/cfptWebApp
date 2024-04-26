from django.urls import path
from . import views


app_name = 'gestion_formations'
urlpatterns = [
    path('', views.all_formations, name='all_formations'),
    path('formation/<int:formation_id>/', views.detail_formation, name='detail_formation'),
    path('delete/<int:formation_id>/', views.delete, name='delete'),
    
    # Ajoutez d'autres URL ici
]
