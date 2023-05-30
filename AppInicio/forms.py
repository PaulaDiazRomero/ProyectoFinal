import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal.settings')
django.setup()
from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppInicio.models import * 

    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="Usuario")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class PosteoCreadoForm(forms.Form):
    titulo = forms.CharField(max_length=50, label="Titulo")
    subtitulo = forms.CharField(max_length=100, label="Subtitulo")
    cuerpo = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=50, label= "Autor")
    fecha = forms.DateField(label= "Fecha")
    imagen = forms.ImageField(label="imagen") 
    
    