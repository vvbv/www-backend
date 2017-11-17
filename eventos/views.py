# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, generics
from .models import Evento, Actividad, PreInscripcionEvento, InscripcionEvento, Noticia, AsistenciaActividad
from .serializers import EventoSerializer, ActividadSerializer, PreInscripcionEventoSerializer, InscripcionEventoSerializer, NoticiaSerializer, AsistenciaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from usuarios.serializers import UsuarioSerializer

class AsistenciaActividadDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = AsistenciaActividad.objects.all()
    serializer_class = AsistenciaSerializer

class AsistenciaActividadList(generics.ListCreateAPIView):    
    queryset = AsistenciaActividad.objects.all()
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

class UsuariosPreinscritosPorEvento(generics.ListAPIView):
    def get_queryset(self):
        evento = kwargs['evento']
        evetoObj = Evento.objects.get(id=evento)
        


class PreInscripcionEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer

    def put(self, request, pk, format=None):
        inscripcion = InscripcionEvento()
        serializer = InscripcionEventoSerializer(inscripcion, data=request.data)
        preInscripcion = self.get_object()
        print(preInscripcion.evento)
        if(preInscripcion.estado == preInscripcion.ACEPTADO):
            inscripcion.evento = preInscripcion.evento
            inscripcion.participante = inscripcion.participante
            inscripcion.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PreInscripcionByEventApi(generics.ListAPIView):
    queryset = PreInscripcionEvento.objects.all()
    def get_queryset(self):
        evento = self.kwargs['evento']
        return  PreInscripcionEvento.objects.filter(evento=evento)
    serializer_class =  PreInscripcionEventoSerializer


class InscripcionByEventApi(generics.ListAPIView):
    def get_queryset(self):
        evento = self.kwargs['evento']
        return  InscripcionEvento.objects.filter(evento=evento)
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
        if(inscripcion.estado == inscripcion.ACEPTADO):
            preinscripcion = PreInscripcionEvento.objects.get(participante=inscripcion.participante, evento=inscripcion.evento)
            preinscripcion.cambiarAEsperaConfirmacionUsuario()
            preinscripcion.save()
        if(inscripcion.estado == inscripcion.PAGADO):
            preinscripcion = PreInscripcionEvento.objects.get(participante=inscripcion.participante, evento=inscripcion.evento)
            preinscripcion.cambiarAPagado()
            preinscripcion.save()
        if(inscripcion.estado == inscripcion.ESPERA_APROVACION):
            preinscripcion = PreInscripcionEvento.objects.get(participante=inscripcion.participante, evento=inscripcion.evento)
            preinscripcion.cambiarAEsperaInscripcion()
            preinscripcion.save()
        if(inscripcion.estado == inscripcion.RECHAZADO):
            preinscripcion = PreInscripcionEvento.objects.get(participante=inscripcion.participante, evento=inscripcion.evento)
            preinscripcion.cambiarAInscripcionRechazada()
            preinscripcion.save()
        if serializer.is_valid():
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
        
class EventosInscritosPorParticipante(generics.ListAPIView):
    queryset = PreInscripcionEvento.objects.all()
    serializer_class = PreInscripcionEventoSerializer
    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        usuario = self.kwargs['usuario']
        return PreInscripcionEvento.objects.filter(evento=evento, participante=usuario).selectRelated('preinscripcionEvento_evento')