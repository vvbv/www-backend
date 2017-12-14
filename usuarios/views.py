# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import IntegrityError
import rest_framework.permissions as rest_permissions
from rest_framework import viewsets, generics, status, mixins
from usuarios.models import Usuario, MedioDePago
from usuarios.serializers import UsuarioSerializer, MedioDePagoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from pagos_middleware import api_conn
# Create your views here.

class UsuariosList(generics.ListAPIView):
    queryset = Usuario.objects.all().order_by('-fechaHoraRegistro')
    serializer_class = UsuarioSerializer

class UsuarioPkApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class =  UsuarioSerializer

class MedioDePagoPorUsuario(generics.ListAPIView):
    serializer_class = MedioDePagoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        username = self.kwargs['username']
        return MedioDePago.objects.all().filter(usuario__username = username)

def abonarPago():
    return 0

class UsuarioUsernameApi(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    queryset = Usuario.objects.all()
    serializer_class =  UsuarioSerializer

class UsuarioCreateApi(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class respuesta:
    codigo = 1
    mensaje = ''
    def __init__(self, codigo, mensaje):
        self.codigo = codigo
        self.mensaje = mensaje
    def toJSON(self):
        return self.__dict__
respuestaUsuarioNoExiste = respuesta(0, 'El usuario no existe')
respuestaTarjetaValida = respuesta(1, 'La tarjeta es valida')
respuestaTarjetaInvalida = respuesta(2, 'El numero de tarjeta o la contraseña son invalidos')
respuestaTarjetaDuplicada = respuesta(3, 'Otro usuario ya ha registrado esta tarjeta')
def registrarMedioPago(request, numero_cuenta, username, password):
    api_pagos = api_conn.ApiPagos()
    try:
        user = Usuario.objects.get(username = username)
    except Usuario.DoesNotExist:
        return JsonResponse(respuestaUsuarioNoExiste.toJSON())
    tarjetaValida, mensajeRetorno = api_pagos.validar_tarjeta(numero_cuenta, password)
    if tarjetaValida:
        medio_de_pago = MedioDePago.create(user, numero_cuenta)
        try:
            medio_de_pago.save()
        except IntegrityError as e: 
            return JsonResponse(respuestaTarjetaDuplicada.toJSON())
        print (medio_de_pago.save())
        return JsonResponse(respuestaTarjetaValida.toJSON())
    else:
        print (respuestaUsuarioNoExiste.toJSON())
        return JsonResponse(respuestaTarjetaInvalida.toJSON())
        
    