from django.conf import settings
from django.db import models

# Create your models here.

class PosteoCreado(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='posteos', null=True, blank = True)
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
