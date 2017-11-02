# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, generics
from .models import Evento, Actividad, PreInscripcionEvento
from .serializers import EventoSerializer, ActividadSerializer, PreInscripcionEventoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'actividades': reverse('actividad-list', request=request, format=format),
        'eventos': reverse('eventos-list', request=request, format=format)
    })

class ActividadList(generics.ListAPIView):    
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        evento = self.kwargs['evento']
        return Actividad.objects.filter(evento=evento)

class ActivdadCreate(generics.CreateAPIView):    
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class EventosEstadosList(APIView):
    def get(self, request, format=None):
        serializer =  EventoEstadosSerializer(Evento.ESTADO_EVENTOS)
        return Response(serializer.data)

class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer

class EventoEstadoChoicesViewSet(APIView):
    def get(self, request):
        return Response(Evento.ESTADO_TYPES)

class PreInscripcionEventoList(generics.ListCreateAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer

class PreInscripcionEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer