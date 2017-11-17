from django.db import models

# Create your models here.
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes/cargas')
    fechaHoraRegistro = models.DateField(auto_now_add=True, null=False)
