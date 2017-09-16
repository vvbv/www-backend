from rest_framework import serializers
from .models import Evento, Actividad

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    actividades = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    class Meta: 
        model = Evento
        fields = ('nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion', 'estado', 'actividades')
    
class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion')