# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, generics
from .models import Evento, Actividad, PreInscripcionEvento, InscripcionEvento, Noticia
from .serializers import EventoSerializer, ActividadSerializer, PreInscripcionEventoSerializer, InscripcionEventoSerializer, NoticiaSerializer
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
    queryset = Actividad.objects.all().order_by('fechaInicio')
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

class NoticiasList(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class NoticiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all() 
    serializer_class = NoticiaSerializer

class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all().order_by('fechaInicio')
    serializer_class = EventoSerializer
    #def post(self, request):
    #    print(request.query_params['file'])

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all() 
    serializer_class = EventoSerializer

class EventoEstadoChoicesViewSet(APIView):
    def get(self, request):
        return Response(Evento.ESTADO_TYPES)

class PreInscripcionEventoList(generics.ListCreateAPIView):
    queryset = PreInscripcionEvento.objects.all().order_by('fechaPreInscripcion')
    serializer_class = PreInscripcionEventoSerializer

class PreInscripcionEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer

class PreInscripcionByEventApi(generics.ListAPIView):
    lookup_field = 'evento'
    queryset = PreInscripcionEvento.objects.all()
    serializer_class =  PreInscripcionEventoSerializer

class InscripcionEventoList(generics.ListCreateAPIView):
    queryset = InscripcionEvento.objects.all().order_by('fechaRegistro')
    serializer_class = InscripcionEventoSerializer

class InscripcionEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InscripcionEvento.objects.all()
    serializer_class = InscripcionEventoSerializer

class PreInscripcionEventoByIdUserIdEvent(generics.ListAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        evento = self.kwargs['evento']
        usuario = self.kwargs['usuario']
        return PreInscripcionEvento.objects.filter(evento=evento, participante=usuario)