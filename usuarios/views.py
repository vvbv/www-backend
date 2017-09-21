# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import viewsets, generics, status
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class Usuario2Detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        #username = self.kwargs['username']
        #return Usuario.objects.filter(purchaser__username=username)

        queryset = Usuario.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #def get_queryset(self):
    #    """
    #    This view should return a list of all the purchases for
    #    the user as determined by the username portion of the URL.
    #    """
    #    usernamex = self.kwargs['username']
    #    return Usuario.objects.filter(username=usernamex)
    #    print("username_paramusername_paramusername_paramusername_paramusername_paramusername_paramusername_paramusername_param")
    #    queryset = Usuario.objects.all()
    #    username_param = self.request.query_params.get('username', None)
    #    if username_param is not None:
    #        queryset = queryset.filter(username=username_param)
    #    return queryset
    #serializer_class = UsuarioSerializer