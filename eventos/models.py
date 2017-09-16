# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.

class Evento(models.Model):
    FINALIZADO = _('FN')
    SIN_INICIAR = _('SI')
    CANCELADO = _('CC')

    ESTADO_EVENTOS= ( 
        (FINALIZADO, _('Finalizado')),
        (SIN_INICIAR, _('Sin iniciar')),
        (CANCELADO, _('Cancelado'))
        )

    nombre = models.CharField(max_length=50, null=False )
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    fechaFinalizacion = models.DateTimeField(auto_now=False, auto_now_add=False, null=False) 
    estado = models.CharField(max_length=2, choices=ESTADO_EVENTOS,default=SIN_INICIAR)
    class Meta:
        permissions = (
            (_("crear"), _('Puede crear un evento')),
            (_("editar_fechas"), _('Puede editar las fechas de inicio y fin de un evento')),
            (_('cancelar'), _('Puede cambiar el estado de un evento a cancelado')),
        )

class Actividad(models.Model):
    nombre = models.CharField(max_length=50, null=False )
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    fechaFinalizacion = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    evento = models.ForeignKey('Evento',related_name = 'actividades', on_delete=models.CASCADE, )


