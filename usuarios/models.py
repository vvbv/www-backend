# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import ugettext as _

# Create your models here.

class Usuario(User):
    """
    Modelo para los usuarios del sistema/publicos
    """
    ADMINISTRADOR = _('AD')
    GERENTE = _('GR')
    OPERADOR = _('OP')
    USUARIO_PUBLICO = _('UP')
     
    ROL_VALS = (ADMINISTRADOR, GERENTE, OPERADOR, USUARIO_PUBLICO)
    ROL_NAMES = (_('Administrador'), _('Gerente'), _('Operador'),  _('Usuario público') )
    ROLES =   tuple(zip(ROL_VALS, ROL_NAMES))


    username_validator = ASCIIUsernameValidator()
    numero_identificacion = models.CharField(_('Número de identificación'), max_length=60, null=False, unique=True)
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    imagenPerfil = models.IntegerField(max_length=None, null=True)


    rol = models.CharField(max_length=2,choices=ROLES,null=False, default = USUARIO_PUBLICO  )
    estadoHabilitado = models.BooleanField(default=True, null=False)
    fechaHoraRegistro = models.DateField(auto_now_add=True, null=False)
    custom_email = models.EmailField(_('Correo electrónico'),max_length=255, unique=True, null=False)
 
