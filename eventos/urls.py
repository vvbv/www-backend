from django.conf.urls import url 
from eventos import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^eventos/estados/$', views.EventoEstadoChoicesViewSet.as_view(), name='estado_eventos_list'),
    url(r'^eventos/$', views.EventoList.as_view(), name = 'eventos-list'),
    url(r'^eventos/preinscripciones/$', views.PreInscripcionEventoList.as_view(), name = 'preinscripciones-list'),
    url(r'^eventos/preinscripciones/(?P<pk>[0-9]+)/$', views.PreInscripcionEventoDetail.as_view(), name = 'preinscripciones-detail'),
    url(r'^eventos/inscripciones/$', views.InscripcionEventoList.as_view(), name = 'inscripciones-list'),
    url(r'^eventos/inscripciones/(?P<pk>[0-9]+)/$', views.InscripcionEventoDetail.as_view(), name = 'inscripciones-detail'),
    url(r'^eventos/(?P<pk>[0-9]+)/$', views.EventoDetail.as_view(), name = 'evento-detail'),
    url(r'^actividades/(?P<pk>[0-9]+)/$', views.ActividadDetail.as_view(), name = 'actividad-detail'),
    url(r'^actividades/porEvento/(?P<evento>\w+)/$', views.ActividadList.as_view(), name = 'actividad-list'),
    url(r'^actividades/crear/$', views.ActivdadCreate.as_view(), name = 'actividad-create'),
]