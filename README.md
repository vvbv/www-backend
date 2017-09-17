# Trabajo final: Aplicaciónes en el Web y redes inalambricas


El actual trabajo corresponde al diseño del backend de el proyecto de Aplicaciones en el web, utilizando django-rest-framework.

Adicionalmente se proveera de una interfaz grafica echa en angular la cual proximamente
se estara desarrollando.

## build-models.sh

Elimina el caché viejo de los modelos y genera uno nuevo.
```Shell
# Limpia el caché y genera las migraciones
sh build-models.sh

# Limpia el caché junto con la base de datos,
# genera las migraciones y las migra a la nueva BD, 
# registra la cuenta administrador.
sh build-models.sh with_sqlite3 
```
