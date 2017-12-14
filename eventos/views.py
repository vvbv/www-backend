# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, generics
from .models import Evento, Actividad, PreInscripcionEvento, InscripcionEvento, Noticia, AsistenciaActividad
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from usuarios.serializers import UsuarioSerializer
from django.db.models import Q
from django.http import JsonResponse

from .models import ReportesEventos

class AsistenciaActividadDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = AsistenciaActividad.objects.all()
    serializer_class = AsistenciaSerializer

class AsistenciaActividadList(generics.ListCreateAPIView):    
    queryset = AsistenciaActividad.objects.all().order_by('fechaRegistro')
    serializer_class = AsistenciaSerializer

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

class ActividadAllList(generics.ListCreateAPIView):    
    queryset = Actividad.objects.all().order_by('fechaInicio')
    serializer_class = ActividadSerializer

@api_view(['GET'])
def estadisticasEventos(request):
    reportesEventos = ReportesEventos()
    return JsonResponse(reportesEventos.estadisticas().toJSON())

class ActivdadCreate(generics.CreateAPIView):    
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer


class CincoUltimosEventosList(generics.ListAPIView):
    queryset = Evento.objects.all().order_by('fechaInicio')[:5]
    serializer_class = EventoSerializer

class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class NoticiasList(generics.ListCreateAPIView):
    queryset = Noticia.objects.all().order_by('-fechaRegistro')
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


@api_view(['GET'])
def aceptarInscripcionEventoPorUsuario(request, evento, usuario):
    try:
        inscripcion = InscripcionEvento.objects.get(evento = evento, participante = usuario)
        inscripcion.estado = InscripcionEvento.ESPERA_PAGO
        inscripcion.save()
        return JsonResponse(InscripcionEventoSerializer(inscripcion).data)
    except InscripcionEvento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        


@api_view(['GET'])
def getUsuariosPreinscritosPorEvento(request, idEvento):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        evento = Evento.objects.get(pk=idEvento)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsuarioSerializer(evento.usuariosPreinscritos.all(), many = True)
        return Response(serializer.data)
    

class PreInscripcionEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer

    def put(self, request, pk, format=None):
        inscripcion = InscripcionEvento()
        preInscripcion = self.get_object()
        serializer = PreInscripcionEventoSerializer(preInscripcion, data=request.data)
        print(request.data)
        if serializer.is_valid():
            if(request.data['estado'] == preInscripcion.ACEPTADO):
                inscripcion.evento = preInscripcion.evento
                inscripcion.participante = preInscripcion.participante
                inscripcion.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreInscripcionByEventApi(generics.ListAPIView):
    queryset = PreInscripcionEvento.objects.all()
    def get_queryset(self):
        evento = self.kwargs['evento']
        return  PreInscripcionEvento.objects.filter(evento=evento).order_by('fechaPreInscripcion')
    serializer_class =  PreInscripcionEventoSerializer

class PreInscripcionByEventConUsuarios(generics.ListAPIView):
    def get_queryset(self):
        evento = self.kwargs['evento']
        return PreInscripcionEvento.objects.filter(evento=evento).order_by('fechaPreInscripcion')
    serializer_class =  PreInscripcionEventoConUsuarioSerializer

class InscripcionByEventConUsuarios(generics.ListAPIView):
    def get_queryset(self):
        evento = self.kwargs['evento']
        return InscripcionEvento.objects.filter(evento=evento).order_by('fechaRegistro')
    serializer_class =  InscripcionEventoConUsuarioSerializer


class InscripcionByEventApi(generics.ListAPIView):
    def get_queryset(self):
        evento = self.kwargs['evento']
        return  InscripcionEvento.objects.filter(evento=evento).order_by('fechaRegistro')
    serializer_class =  InscripcionEventoSerializer

class InscripcionEventoList(generics.ListCreateAPIView):
    queryset = InscripcionEvento.objects.all().order_by('fechaRegistro')
    serializer_class = InscripcionEventoSerializer



class InscripcionEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InscripcionEvento.objects.all()
    serializer_class = InscripcionEventoSerializer

    def put(self, request, pk, format=None):
        inscripcion = self.get_object()
        serializer = InscripcionEventoSerializer(inscripcion, data=request.data)
        if serializer.is_valid():
            estadoInscripcionNueva = request.data['estado']
            if(estadoInscripcionNueva == inscripcion.ESPERA_APROVACION_OPERADOR):
                preinscripcion = PreInscripcionEvento.objects.get(participante=inscripcion.participante, evento=inscripcion.evento)
                preinscripcion.delete()
            if(estadoInscripcionNueva == inscripcion.RECHAZADO):
                preinscripcion = PreInscripcionEvento.objects.get(participante=inscripcion.participante, evento=inscripcion.evento)
                preinscripcion.delete()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class InscripcionEventoByIdUserIdEvent(generics.ListAPIView):
    queryset = InscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        evento = self.kwargs['evento']
        usuario = self.kwargs['usuario']
        return InscripcionEvento.objects.filter(evento=evento, participante=usuario)

class UsuariosPreInscritosEvento(generics.ListAPIView):
    queryset = PreInscripcionEvento.objects.all().prefetch_related('participante')
    serializer_class = PreInscripcionEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        evento = self.kwargs['evento']
        return PreInscripcionEvento.objects.filter(evento=evento).prefetch_related('participante')

class InscripcionEventByIdUserIdEvent(generics.ListAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        evento = self.kwargs['evento']
        usuario = self.kwargs['usuario']
        return InscripcionEvento.objects.filter(evento=evento, participante=usuario)


class InscripcionesByEvent(generics.ListAPIView):
    queryset = InscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        evento = self.kwargs['evento']
        usuario = self.kwargs['usuario']
        return InscripcionEvento.objects.filter(evento=evento, participante=usuario)
        
class PreinscripcionesConEvento(generics.ListAPIView):
    serializer_class = PreInscripcionEventoConEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        usuario = self.kwargs['usuario']
        return PreInscripcionEvento.objects.filter(participante=usuario)

class EventosSinSeguimiento(generics.ListAPIView):
    serializer_class = EventoSerializer
    def get_queryset(self):
        usuario = self.kwargs['usuario']
        
        return Evento.objects.filter(~Q(usuariosInscritos = usuario), ~Q(usuariosPreinscritos = usuario) )

class InscripcionesConEvento(generics.ListAPIView):
    serializer_class = InscripcionEventoConEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        usuario = self.kwargs['usuario']
        return InscripcionEvento.objects.filter(participante=usuario)