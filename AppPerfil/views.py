import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal.settings')
django.setup()
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from AppPerfil.models import *
from AppPerfil.forms import *

# Create your views here.


def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user = request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/avatares/default.jpg"


def perfil(request):
    return render(request, "perfil.html", {"avatares": obtenerAvatar(request)})


def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name = form.cleaned_data['first_name']
            usuario.last_name = form.cleaned_data['last_name']
            usuario.email = form.cleaned_data['email']
            usuario.password1 = form.cleaned_data['password1']
            usuario.password2 = form.cleaned_data['password2']
            usuario.save()
            return render(request, "perfil.html", {"avatares": obtenerAvatar(request)})
    else:
        form = UserEditForm()
        return render(request, "editarPerfil.html")

    return render(request, "editarPerfil.html", {"form": form, "usuario": usuario})



def editarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usu = User.objects.get(username = request.user)
            avatares = Avatar(user = usu, imagen = form.cleaned_data['imagen'])
            avatarViejo = Avatar.objects.filter(user = request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatares.save()
            return render(request, "perfil.html", {"avatares": obtenerAvatar(request)})
        else:
           form = AvatarForm()
           return render(request, "editarAvatar.html", {"form": form, "usuario": request.user, "avatares": obtenerAvatar(request)})
    else:
        form = AvatarForm()
        return render(request, "editarAvatar.html",  {"form": form, "usuario": request.user, "avatares": obtenerAvatar(request)})




def mensajeria(request):
    return render(request, "mensajeria.html")




def mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = Mensaje()
            mensaje.emisor = form.cleaned_data['emisor']
            mensaje.receptor = form.cleaned_data['receptor']
            mensaje.mensaje = form.cleaned_data['mensaje']
            mensaje.save()
            return render(request, "mensaje.html", {"form": form, "mensaje":"Mensaje enviado."})
        else:
            form = MensajeForm()
            return render(request, "mensaje.html", {"form": form, "mensaje":"Error al enviar mensaje"})
    else:
        form = MensajeForm(request.POST)
    mensajes = Mensaje.objects.all()    
    return render(request, "mensaje.html", {"mensajes": mensajes, "form": form})



def buzon(request): 
    usuario = request.user
    email_receptor = Mensaje.objects.filter(receptor__icontains = usuario.email)
    print(email_receptor)
    return render(request, "buzon.html", {"email_receptor" : email_receptor})
