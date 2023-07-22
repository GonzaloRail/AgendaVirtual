# nombre_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enviar_mensaje/', views.enviar_mensaje_whatsapp),
    path('agregar_contacto/', views.agregar_contacto),
    # Otras URLs de tu aplicación...
]
