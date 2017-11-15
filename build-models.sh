#!/bin/bash
rm -rf $PWD/www_backend/__pycache__
rm $PWD/www_backend/*.pyc

rm -rf $PWD/eventos/__pycache__
rm $PWD/eventos/migrations/0*
rm $PWD/eventos/*.pyc
rm -rf $PWD/eventos/migrations/__pycache__

rm -rf $PWD/usuarios/__pycache__
rm $PWD/usuarios/migrations/0*
rm $PWD/usuarios/*.pyc
rm -rf $PWD/usuarios/migrations/__pycache__

rm -rf $PWD/imagenes/__pycache__
rm $PWD/imagenes/migrations/0*
rm $PWD/imagenes/*.pyc
rm -rf $PWD/imagenes/migrations/__pycache__
rm $PWD/imagenes/cargas/*

if [ "$1" = "with_sqlite3" ]
then
    rm $PWD/db.sqlite3
    python3.5 manage.py makemigrations usuarios
    python3.5 manage.py makemigrations 
    python3.5 manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('administrator', 'admin@example.com', 'administrator')" | python3.5 manage.py shell
    echo "Usuario: administrator:administrator creado."
    echo "Tarea terminada."
else
    python3.5 manage.py makemigrations
    echo "Tarea terminada."
fi