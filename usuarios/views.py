# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import rest_framework.permissions as rest_permissions
from rest_framework import viewsets, generics, status, mixins
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.

class UsuariosList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioPkApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class =  UsuarioSerializer

class UsuarioUsernameApi(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    queryset = Usuario.objects.all()
    serializer_class =  UsuarioSerializer

class UsuarioCreateApi(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
