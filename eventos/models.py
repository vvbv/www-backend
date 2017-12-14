# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.db import models
from django.db.models import Count
from usuarios.models import Usuario 
import eventos.validators as validators
from django.utils import timezone
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
    imagen = models.ImageField(_('Imagen'), null=False, default=0, upload_to='static/imagenes/eventos')
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
    fechaCreacion = models.DateTimeField(auto_now_add=True, editable=False)
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

    ACEPTADO = 'A'
    RECHAZADO = 'R'
    ESPERA_APROVACION = 'EA'
    ESTADO_NAMES = (_('Preinscripción aceptada'), _('Preinscripcion rechazada'), _('Espera Aprovación') )

    ESTADO_VALS = (ACEPTADO, RECHAZADO, ESPERA_APROVACION)
    ESTADO_TYPES = tuple(zip(ESTADO_VALS,ESTADO_NAMES))
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='preinscripcionEvento_evento')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='preinscripionEvneto_participante')
    fechaPreInscripcion = models.DateTimeField(auto_now_add=True, editable=False)
    estado = models.CharField(null=False,choices=ESTADO_TYPES, default=ESPERA_APROVACION, max_length=2)
        
class InscripcionEvento(models.Model):
    class Meta:
        unique_together = (('evento', 'participante'))
    ESPERA_PAGO = 'EP'
    PAGADO = 'P'
    RECHAZADO = 'R'
    ESPERA_APROVACION_OPERADOR = 'EO'
    ESPERA_APROVACION_USUARIO = 'EU'
    
    ESTADO_NAMES = (_('Rechazado'), _('En espera aprovacion de un operador'), _('En espera de pago'), _('Pagado'), _('Espera de confirmación de usuario'))
    ESTADO_VALS = (RECHAZADO, ESPERA_APROVACION_OPERADOR, ESPERA_PAGO, PAGADO, ESPERA_APROVACION_USUARIO)
    ESTADO_TYPES = tuple(zip(ESTADO_VALS, ESTADO_NAMES))
    fechaRegistro = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    fechaModificacion = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    estado = models.CharField(choices=ESTADO_TYPES, default=ESPERA_APROVACION_OPERADOR, max_length=2)
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscripcionEvento_evento')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripcionEvento_participante')


class AsistenciaActividad(models.Model):
    class Meta:
        unique_together = ('participante', 'actividad')
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='asistenciaActividad_participante')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=False, related_name='asistenciaActividad_actividad')
    fechaModificacion = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    fechaRegistro = models.DateTimeField(auto_now_add=True, null=False, editable=False )

class Noticia(models.Model):
    titulo = models.CharField(_('Titulo'), max_length = 100, null=False)
    resumen = models.TextField(_('Descripción'), null=False)
    contenido = models.TextField(_('Contenido'), null =False)
    imagen = models.ImageField(_('Imagen'), null=False, upload_to='static/imagenes/noticias')
    fechaRegistro = models.DateTimeField(auto_now_add=True, null=False, editable=False )
    usuarioRegistra = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='noticia_usuario_registra')
    fechaModificacion = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    estado = models.BooleanField(_('Estado'), null=False, default= True)

class EstadisticasEventos:
    cantidadEventosCancelados = 0
    cantidadEventosSinIniciar = 0
    cantidadEventosTerminados = 0
    cantidadEventosEnCurso = 0
    numeroTotalEventos = 0
    
    def toJSON(self):
        return self.__dict__

class EstadisticasInscripciones:
    cantidadInscripciones = 0
    cantidadInscripcionesAceptadas = 0
    cantidadInscripcionesRechazadas = 0
    cantidadInscripcionesPendientes = 0
    
    def toJSON(self):
        return self.__dict__
    
    

class ReportesEventos:
    def cantidadEventosEnCurso(self):
        fecha_actual = timezone.now()
        return Evento.objects.filter(fechaInicio__lte = fecha_actual, fechaFinalizacion__gte=fecha_actual).count()
    def cantidadEventosFinalizados(self):
        return Evento.objects.filter(estado=Evento.FINALIZADO).count()
    def cantidadEventosSinIniciar(self):
        return Evento.objects.filter(estado=Evento.SIN_INICIAR).count()
    def cantidadEventosCancelados(self):
        return Evento.objects.filter(estado=Evento.CANCELADO).count()
    def estadisticas(self):
        estadisticasEventos = EstadisticasEventos()
        estadisticasEventos.cantidadEventosCancelados = self.cantidadEventosCancelados()
        estadisticasEventos.cantidadEventosSinIniciar = self.cantidadEventosSinIniciar()
        estadisticasEventos.cantidadEventosTerminados = self.cantidadEventosFinalizados()
        estadisticasEventos.cantidadEventosEnCurso = self.cantidadEventosEnCurso()
        return estadisticasEventos

class ReportesInscripciones:
    def cantidadInscripcionesAceptadas(self):
        return InscripcionEvento.objects.filter(estado = InscripcionEvento.ACEPTADO).count()
    def cantidadInscripcionesRechazadas(self):
        return InscripcionEvento.objects.filter(estado = InscripcionEvento.RECHAZADO).count()
    def cantidadInscripciones(self):
        return InscripcionEvento.objects.count()
    def cantidadInscripcionesEnEsperaPago(self):
        return InscripcionEvento.objects.filter(estado = InscripcionEvento.ESPERA_PAGO).count()
    def cantidadInscripcionesPagadas(self):
        return InscripcionEvento.objects.filter(estado = InscripcionEvento.PAGADO).count()
    
    def estadisticas(self):
        estadisticasInscripciones =  EstadisticasInscripciones()
        estadisticasInscripciones.cantidadInscripcionesPagadas = self.cantidadInscripcionesPagadas()
        estadisticasInscripciones.cantidadInscripcionesEnEsperaPago = self.cantidadInscripcionesEnEsperaPago()
        estadisticasInscripciones.cantidadInscripcionesAceptadas = self.cantidadInscripcionesAceptadas()
        return estadisticasInscripciones