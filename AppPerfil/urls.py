from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppPerfil.views import *

urlpatterns = [
    path('perfil/', perfil, name = "perfil"),
    path('editarPerfil/', editarPerfil, name = "editarPerfil"),
    path('editarAvatar/', editarAvatar, name = "editarAvatar"),
    path('mensajeria/', mensajeria, name = "mensajeria"),
    path('mensaje/', mensaje, name = "mensaje"),
    path('buzon/', buzon, name = "buzon"),
]