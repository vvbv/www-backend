from rest_framework import serializers
from .models import * 

class InfoConeccionPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoConeccionPagos
        fields = ('id', 'key', 'fecha_vencimiento')