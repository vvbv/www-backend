# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagenes.models import Imagen
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

# Create your models here.

class Usuario(User):
    """
    Modelo para los usuarios del sistema/publicos
    """
    username_validator = ASCIIUsernameValidator()
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    imagenPerfil = models.ForeignKey(Imagen, on_delete=models.CASCADE, related_name='imagen_usuario')
    ROLES = (
        ('AD', 'Administrador'),
        ('GR', 'Gerente'),
        ('OP', 'Operador'),
        ('UP', 'Usuario público'),
    )
    rol = models.CharField(max_length=2,choices=ROLES,null=False)
    estadoHabilitado = models.BooleanField(default=True, null=False)
    fechaHoraRegistro = models.DateField(auto_now_add=True, null=False)

