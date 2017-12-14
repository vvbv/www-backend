import crypt

from django.contrib.auth.models import User
from rest_framework import serializers
from usuarios.models import Usuario, MedioDePago
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@permission_classes((AllowAny, ))
class UsuarioSerializer(serializers.ModelSerializer):
    permission_classes = (AllowAny,)
    class Meta:
        model = Usuario
        fields = (
            'id', 'numero_identificacion', 'username', 'password', 'nombres', 'apellidos',
            'imagenPerfil', 'rol', 'custom_email', 'estadoHabilitado',
            'groups', 'fechaHoraRegistro'
            )
        ordering = ['fechaHoraRegistro']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                if "pbkdf2" in validated_data['password']:
                    pass
                else:
                    instance.set_password(validated_data['password'])
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class MedioDePagoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MedioDePago
        fields = ('id', 'usuario', 'numero_cuenta') 