import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal.settings')
django.setup()
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.mixins import LoginRequiredMixin
from AppInicio.forms import UserRegisterForm, PosteoCreadoForm
from AppInicio.models import PosteoCreado
from AppPerfil.views import obtenerAvatar



# Create your views here.

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                posteos = PosteoCreado.objects.all() 
                return render(request, "posteos.html", {"posteos": posteos})
            else:
                form = AuthenticationForm()
                return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos."})
        else:
            form = AuthenticationForm()
            return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos."})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form}) 

            

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            form = UserRegisterForm()
            return render(request, "registro.html", {"mensaje":f"Usuario {username} registrado correctamente."})
        else:
            form = UserRegisterForm()
            return render(request, "registro.html", {"mensaje":f"Error al crear usuario. Intente nuevamente."})
    else:
        form = UserRegisterForm()
        return render(request, "registro.html", {"form": form})
    
    

def crearPosteo(request):
    if request.method == "POST":
        form = PosteoCreadoForm(request.POST, request.FILES)
        if form.is_valid():
            posteo = PosteoCreado()
            posteo.titulo = form.cleaned_data['titulo']
            posteo.subtitulo = form.cleaned_data['subtitulo']
            posteo.cuerpo = form.cleaned_data['cuerpo']
            posteo.autor = form.cleaned_data['autor']
            posteo.fecha = form.cleaned_data['fecha'] 
            posteo.imagen = form.cleaned_data['imagen']
            posteo.save()
            return render(request, "crearPosteo.html", {"form": form, "mensaje":"Posteo creado."})
        else:
            form = PosteoCreadoForm()
            return render(request, "crearPosteo.html", {"form": form, "mensaje":"Error al crear posteo."})
    else:
        form = PosteoCreadoForm()
    posteos = PosteoCreado.objects.all()    
    return render(request, "crearPosteo.html", {"posteos" : posteos, "form" : form})



def posteos(request):
    posteos = PosteoCreado.objects.all()   
    return render(request, "posteos.html", {"posteos": posteos})



def verPosteo(request, id):
    posteo = PosteoCreado.objects.get(id = id)
    posteos = PosteoCreado.objects.filter(id__icontains = id)
    return render(request, "verPosteo.html", {"posteos": posteos})


def editarPosteo(request, id):
    usuario = request.user
    Autor = PosteoCreado.objects.filter(autor__icontains=usuario.username)
    posteo = PosteoCreado.objects.get(id = id)
    if request.method == 'POST':
        form = PosteoCreadoForm(request.POST, request.FILES)
        if form.is_valid():
            posteo.titulo = form.cleaned_data['titulo']
            posteo.subtitulo = form.cleaned_data['subtitulo']
            posteo.cuerpo = form.cleaned_data['cuerpo']
            posteo.autor = form.cleaned_data['autor']
            posteo.fecha = form.cleaned_data['fecha'] 
            posteo.imagen = form.cleaned_data['imagen']
            posteo.save()
            posteos = PosteoCreado.objects.all()
            form = PosteoCreadoForm()
            return render(request, "editarPosteo.html", {"form": form, "mensaje":"Posteo editado."})
    else:
        form = PosteoCreadoForm()
        return render(request, "editarPosteo.html", {"form": form})

    return render(request, "editarPosteo.html", {"form": form, "usuario": usuario})
   


def eliminarPosteo(request, id):
    usuario = request.user
    Autor = PosteoCreado.objects.filter(autor__icontains = usuario.username)
    posteo = PosteoCreado.objects.get(id = id)
    posteo.delete()
    posteos = PosteoCreado.objects.all()
    form = PosteoCreadoForm()
    return render(request, "eliminarPosteo.html", {"posteos": posteos, "form": form})