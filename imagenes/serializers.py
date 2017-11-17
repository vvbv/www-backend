from rest_framework import serializers
from imagenes.models import Imagen

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('id','imagen','fechaHoraRegistro')
        ordering = ['-id']
