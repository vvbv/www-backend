from rest_framework import serializers
from usuarios.serializers import UsuarioSerializer
from .models import Evento, Actividad, PreInscripcionEvento, InscripcionEvento


class EventoSerializer(serializers.ModelSerializer):
    actividades = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    usuariosPreinscritos = UsuarioSerializer(many=True, read_only=True)
    def validate(self, attrs):
        instance = Evento(**attrs)
        instance.clean()
        return attrs
    class Meta: 
        model = Evento
        fields = ('id',     'nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion', 'estado', 'actividades', 'usuariosPreinscritos')
    def get_estados(self, obj):
        return obj.get_estados_display()
   
class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad   
        fields = ('id', 'nombre', 'descripcion', 'fechaInicio', 'fechaFinalizacion',)

class PreInscripcionEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreInscripcionEvento
        fields = ('id', 'evento', 'participante', 'fechaPreInscripcion', 'estado')

class InscripcionEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscripcionEvento
        fields = ('id', 'evento', 'participante', 'estado', 'fechaRegistro', 'fechaModificacion')
