# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import * 

admin.site.register(Evento)
admin.site.register(Actividad)
admin.site.register(PreInscripcionEvento)
admin.site.register(InscripcionEvento)
admin.site.register(AsistenciaActividad)
# Register your models here.
