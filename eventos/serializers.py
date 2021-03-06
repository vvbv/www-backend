from rest_framework import serializers
from .models import Evento, Actividad


class EventoSerializer(serializers.ModelSerializer):
    actividades = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    def validate(self, attrs):
        instance = Evento(**attrs)
        instance.clean()
        return attrs
    class Meta: 
        model = Evento
        fields = ('nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion', 'estado', 'actividades')
    def get_estados(self, obj):
        return obj.get_estados_display()
   
class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion',)

