import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal.settings')
django.setup()
from django.conf import settings
from django.urls import path
from django import views
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from AppInicio.views import *


urlpatterns = [
    path('login/', login_request, name = "login"),
    path('registro/', registro, name = "registro"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('posteos/', posteos, name = "posteos"),
    path('crearPosteo/', crearPosteo, name = "crearPosteo"),
    path('posteos/<id>/', verPosteo, name = "verPosteo"),
    path('editarPosteo/<id>/', editarPosteo, name = "editarPosteo"),
    path('eliminarPosteo/<id>/', eliminarPosteo, name = "eliminarPosteo"),
] 