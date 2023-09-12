from django.urls import path 
from . import views

app_name='apps.contacto'

urlpatterns = [
    path('contacto/', views.ContactoUsuario.as_view(),name='contacto'),
     path('inscribirse/', views.inscripcion_view, name='inscribirse'),
]