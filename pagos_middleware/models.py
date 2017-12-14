from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class InfoConeccionPagos(models.Model):
    key = models.CharField(_('Llave de acceso'), max_length=200, null = False)
    fecha_vencimiento = models.DateField(_('Fecha vencimiento'), null = False)
    