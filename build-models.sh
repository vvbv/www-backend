#!/bin/bash

rm -rf $PWD/eventos/__pycache__
rm $PWD/eventos/migrations/0*
rm -rf $PWD/eventos/migrations/__pycache__

rm -rf $PWD/usuarios/__pycache__
rm $PWD/usuarios/migrations/0*
rm -rf $PWD/usuarios/migrations/__pycache__

rm -rf $PWD/imagenes/__pycache__
rm $PWD/imagenes/migrations/0*
rm -rf $PWD/imagenes/migrations/__pycache__
rm $PWD/imagenes/cargas/*

if [ "$1" = "with_sqlite3" ]
then
    rm $PWD/db.sqlite3
    python3.5 manage.py makemigrations
    python3.5 manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('administrator', 'admin@example.com', 'administrator')" | python3.5 manage.py shell
    echo "Usuario: administrator:administrator creado."
    echo "Tarea terminada."
else
    python3.5 manage.py makemigrations
    echo "Tarea terminada."
<<<<<<< HEAD
fi
=======
fi
>>>>>>> 327142930102021982925477a013e4c007a2b714
