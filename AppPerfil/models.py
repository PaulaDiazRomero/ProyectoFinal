from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True, default = "avatares/default.jpg")
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
    
    
class Mensaje(models.Model):
    emisor = models.EmailField()
    receptor = models.EmailField()
    mensaje = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.emisor} - {self.receptor} - {self.mensaje}"
    