# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import viewsets, generics
from .models import Usuario
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.

@api_view(['GET, POST'])
def obtenerUsuario(request, id):
    
    diccionario = {
        'uno':'1',
        'dos':'2',
        'metodo':'metodo',
        'msg':'mensaje',
        'user':'s'
    }
    retorno = json.dumps(diccionario)
    return Response(retorno)

def none():
    pass