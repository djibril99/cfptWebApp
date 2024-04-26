from django.urls import path
from . import views


app_name="gestions_messages"
urlpatterns = [
    path('', views.index, name='index'),
]
