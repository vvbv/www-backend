# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 02:29
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('id_imagen_perfil', models.CharField(max_length=10, null=True)),
                ('rol', models.IntegerField(choices=[('AD', 'Administrador'), ('GR', 'Gerente'), ('OP', 'Operador'), ('UP', 'Usuario público')])),
                ('estadoHabilitado', models.BooleanField(default=True)),
                ('fechaHoraRegistro', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
