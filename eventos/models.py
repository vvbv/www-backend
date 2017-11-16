# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import models
from usuarios.models import Usuario 
import eventos.validators as validators
# Create your models here.

class Evento(models.Model):
    FINALIZADO = _('FN')
    SIN_INICIAR = _('SI')
    CANCELADO = _('CC')
     
    ESTADO_VALS = (FINALIZADO,SIN_INICIAR,CANCELADO)
    ESTADO_NAMES = (_('Finalizado'), _('Sin iniciar'), _('Cancelado'))
    ESTADO_TYPES=   tuple(zip(ESTADO_VALS, ESTADO_NAMES))
    
    nombre = models.CharField(_('Nombre del evento'), max_length=50, null=False )
    descripcion = models.TextField(_('Descripción'))
    precio = models.IntegerField(_('Precio'), default=0,null=False)
    fechaInicio = models.DateTimeField(_('Fecha inicio'), auto_now=False, auto_now_add=False, null=False, validators=[validators.validate_date_start_event_before_now])
    fechaFinalizacion = models.DateTimeField(_('Fecha finalización'), auto_now=False, auto_now_add=False, null=False) 
    estado = models.CharField(max_length=2, choices=ESTADO_TYPES,default=SIN_INICIAR)
    imagen = models.ImageField(_('Imagen'), null=True, upload_to='static/imagenes/eventos')
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
    def clean(self):
        if (self.fechaInicio >= self.fechaFinalizacion):
            raise ValidationError(_('La fecha de finalización debe ser mayor a la fecha de inicio'))

    
    class Meta:
        permissions = (
            ('crear', _('Puede crear un evento')),
            ('editar_fechas', _('Puede editar las fechas de inicio y fin de un evento')),
            ('cancelar', _('Puede cambiar el estado de un evento a cancelado')),
        )


class Actividad(models.Model):
    fechaCreacion = models.DateField(auto_now_add=True, editable=False)
    nombre = models.CharField(max_length=50, null=False )
    descripcion = models.TextField(null=False)
    fechaInicio = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    fechaFinalizacion = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    evento = models.ForeignKey('Evento',related_name = 'actividades', on_delete=models.CASCADE, )
    asistentes = models.ManyToManyField(
        Usuario,
        through='AsistenciaActividad',
        through_fields=('actividad', 'participante')
    )

class PreInscripcionEvento(models.Model):
    class Meta:
            unique_together = (('evento', 'participante'),)

    ACEPTADO = _('A')
    RECHAZADO = _('R')
    ESPERA = _('E')
    INSCRITO = _('I')
    ESTADO_NAMES = (_('Aceptado'), _('Rechazado'), _('En espera'), _('Inscrito'))
    ESTADO_VALS = (ACEPTADO, RECHAZADO, ESPERA, INSCRITO)
    ESTADO_TYPES = tuple(zip(ESTADO_VALS,ESTADO_NAMES))
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='preinscripcionEvento_evento')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='preinscripionEvneto_participante')
    fechaPreInscripcion = models.DateTimeField(auto_now_add=True, editable=False)
    estado = models.CharField(null=False,choices=ESTADO_TYPES, default=ESPERA, max_length=2)

class InscripcionEvento(models.Model):
    class Meta:
        unique_together = (('evento', 'participante'),)
    
    ACEPTADO = _('A')
    RECHAZADO = _('R')
    ESPERA = _('E')
    ESTADO_NAMES = (_('Aceptado'), _('Rechazado'), _('En espera'))
    ESTADO_VALS = (ACEPTADO, RECHAZADO, ESPERA)
    ESTADO_TYPES = tuple(zip(ESTADO_VALS, ESTADO_NAMES))
    fechaRegistro = models.DateField(auto_now_add=True, null=False, editable=False)
    fechaModificacion = models.DateField(auto_now_add=True, null=False, editable=False)
    estado = models.CharField(choices=ESTADO_TYPES, default=ESPERA, max_length=2)
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscripcionEvento_evento')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripcionEvento_participante')

class AsistenciaActividad(models.Model):
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asistenciaActividad_participante')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=False, related_name='asistenciaActividad_actividad')
    fechaModificacion = models.DateField(auto_now_add=True, null=False, editable=False)
    fechaRegistro = models.DateField(auto_now_add=True, null=False, editable=False )

class Noticia(models.Model):
    titulo = models.CharField(_('Titulo'), max_length = 100, null=False)
    resumen = models.TextField(_('Descripción'), null=False)
    contenido = models.TextField(_('Contenido'), null =False)
    imagen = models.ImageField(_('Imagen'), null=False, upload_to='static/imagenes/noticias')
    fechaRegistro = models.DateField(auto_now_add=True, null=False, editable=False )
    usuarioRegistra = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='noticia_usuario_registra')
    fechaModificacion = models.DateField(auto_now_add=True, null=False, editable=False)
    estado = models.BooleanField(_('Estado'), null=False, default= True)