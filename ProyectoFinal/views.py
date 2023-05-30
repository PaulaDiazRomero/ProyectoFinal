from django.shortcuts import render
from django.template import Template, loader
from django.contrib.auth.decorators import login_required 


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")


def sobremi(request):
    return render(request, "sobremi.html") 





