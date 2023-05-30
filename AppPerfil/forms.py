from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="imagen")        
    
    
class MensajeForm(forms.Form):
    emisor = forms.EmailField(label="emisor")
    receptor = forms.EmailField(label="receptor")
    mensaje = forms.CharField(max_length=200, label="mensaje")