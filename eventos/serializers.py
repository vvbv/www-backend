from rest_framework import serializers
from .models import Evento, Actividad, PreInscripcionEvento


class EventoSerializer(serializers.ModelSerializer):
    actividades = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    def validate(self, attrs):
        instance = Evento(**attrs)
        instance.clean()
        return attrs
    class Meta: 
        model = Evento
        fields = ('idEvento', 'nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion', 'estado', 'actividades')
    def get_estados(self, obj):
        return obj.get_estados_display()
   
class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('idActividad', 'nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion',)

class PreInscripcionEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreInscripcionEvento
        fields = ('idPreInscripcion', 'evento', 'participante', 'fechaPreInscripcion', 'estado')