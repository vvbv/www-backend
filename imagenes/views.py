from rest_framework import viewsets, generics, status
from imagenes.models import Imagen
from imagenes.serializers import ImagenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
# Create your views here.

class ImagenApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class ImagenCreateApi(generics.CreateAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class ImagenList(generics.ListAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer