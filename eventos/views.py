# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, generics
from .models import Evento, Actividad
from .serializers import EventoSerializer, ActividadSerializer

class ActividadList(generics.ListCreateAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer