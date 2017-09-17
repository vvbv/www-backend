# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from usuarios.models import Usuario 
# Create your models here.

class Evento(models.Model):
    FINALIZADO = _('FN')
    SIN_INICIAR = _('SI')
    CANCELADO = _('CC')
     
    ESTADO_VALS = (FINALIZADO,SIN_INICIAR,CANCELADO)
    ESTADO_NAMES = (_('Finalizado'), _('Sin iniciar'), _('Cancelado'))
    ESTADO_TYPES=   tuple(zip(ESTADO_VALS, ESTADO_NAMES))
    nombre = models.CharField(max_length=50, null=False )
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    fechaFinalizacion = models.DateTimeField(auto_now=False, auto_now_add=False, null=False) 
    estado = models.CharField(max_length=2, choices=ESTADO_TYPES,default=SIN_INICIAR)
    usuariosPreinscritos = models.ManyToManyField(
                                     Usuario,
                                     through='PreInscripcionEvento',
                                     through_fields=('evento', 'participante'),
                                     related_name='usuariosPreinscritos'
                                     )
    usuariosInscritos = models.ManyToManyField(
                                Usuario,
                                through='InscripcionEvento',
                                through_fields=('evento', 'participante'),
                                related_name='usuariosInscritos'
    )
    
    class Meta:
        permissions = (
            ('crear', _('Puede crear un evento')),
            ('editar_fechas', _('Puede editar las fechas de inicio y fin de un evento')),
            ('cancelar', _('Puede cambiar el estado de un evento a cancelado')),
        )


class Actividad(models.Model):
    nombre = models.CharField(max_length=50, null=False )
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    fechaFinalizacion = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    evento = models.ForeignKey('Evento',related_name = 'actividades', on_delete=models.CASCADE, )
    asistentes = models.ManyToManyField(
        Usuario,
        through='AsistenciaActividad',
        through_fields=('actividad', 'participante')
    )

class PreInscripcionEvento(models.Model):
    ACEPTADO = _('A')
    RECHAZADO = _('R')
    ESTADO_NAMES = (_('Aceptado'), _('Rechazado'))
    ESTADO_VALS = (ACEPTADO, RECHAZADO)
    ESTADO_TYPES = tuple(zip(ESTADO_VALS,ESTADO_NAMES))
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='preinscripcionEvento_evento')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='preinscripionEvneto_participante')
    fecha = models.DateTimeField(auto_now_add=True, editable=False)
    estado = models.CharField(null=False,choices=ESTADO_TYPES, default=RECHAZADO, max_length=2)

class InscripcionEvento(models.Model):
    ACEPTADO = _('A')
    RECHAZADO = _('R')
    ESTADO_NAMES = (_('Aceptado'), _('Rechazado'))
    ESTADO_VALS = (ACEPTADO, RECHAZADO)
    ESTADO_TYPES = tuple(zip(ESTADO_VALS, ESTADO_NAMES))
    fecha = models.DateField(auto_now_add=True, null=False, editable=False)
    estado = models.CharField(choices=ESTADO_TYPES, default=ACEPTADO, max_length=2)
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscripcionEvento_evento')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripcionEvento_participante')

class AsistenciaActividad(models.Model):
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asistenciaActividad_participante')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=False, related_name='asistenciaActividad_actividad')
    fechaModificacion = models.DateField(auto_now_add=True, null=False, editable=False)