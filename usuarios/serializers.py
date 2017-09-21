from django.contrib.auth.models import User
from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email')

