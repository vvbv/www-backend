# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Actividad, Evento 

admin.site.register(Evento)
admin.site.register(Actividad)
# Register your models here.
