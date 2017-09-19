# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

#class CustomUser(User):
#    username_validator=ASCIIUsernameValidator()

# Create your models here.

class Usuario(User):
    """
    Modelo para los usuarios del sistema/publicos
    """

    username_validator = ASCIIUsernameValidator()
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    id_imagen_perfil = models.CharField(max_length=10, null=True)
    ADMINISTRADOR = 'AD'
    GERENTE = 'GR'
    OPERADOR = 'OP'
    USUARIO_PUBLICO = 'UP'

    ROLES = (
        (ADMINISTRADOR, 'Administrador'),
        (GERENTE, 'Gerente'),
        (OPERADOR, 'Operador'),
        (USUARIO_PUBLICO, 'Usuario público'),
    )
    rol = models.IntegerField(choices=ROLES,null=False)
    estadoHabilitado = models.BooleanField(default=True, null=False)
    fechaHoraRegistro = models.DateField(auto_now_add=True, null=False)

