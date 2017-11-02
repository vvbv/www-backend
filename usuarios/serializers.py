import crypt

from django.contrib.auth.models import User
from rest_framework import serializers
from usuarios.models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model



class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
            'id', 'numero_identificacion', 'username', 'password', 'nombres', 'apellidos',
            'imagenPerfil', 'rol', 'custom_email', 'estadoHabilitado',
            'groups', 'fechaHoraRegistro'
            )
        ordering = ['-id']

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