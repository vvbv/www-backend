from django.conf.urls import url 
from eventos import views

urlpatterns = [
    url(r'^eventos/estados/$', views.EventoEstadoChoicesViewSet.as_view(), name='estado_eventos_list'),
    url(r'^eventos/$', views.EventoList.as_view(), name = 'eventos-list'),
    url(r'^noticias/$', views.NoticiasList.as_view(), name = 'noticia-list'),
    url(r'^eventos/preinscripciones/$', views.PreInscripcionEventoList.as_view(), name = 'preinscripciones-list'),
    url(r'^eventos/preinscripciones/(?P<pk>[0-9]+)/$', views.PreInscripcionEventoDetail.as_view(), name = 'preinscripciones-detail'),
    url(r'^eventos/(?P<evento>[0-9]+)/preinscripcionesConUsuario/$', views.PreInscripcionByEventConUsuarios.as_view(), name = 'preinscripciones-detail'),
    url(r'^eventos/(?P<evento>[0-9]+)/preinscripciones/$', views.PreInscripcionByEventApi.as_view(), name = 'preinscripciones-by-event-list'),
    url(r'^eventos/(?P<evento>[0-9]+)/inscripciones/$', views.InscripcionByEventApi.as_view(), name = 'inscripciones-by-event-list'),
    url(r'^eventos/inscripciones/$', views.InscripcionEventoList.as_view(), name = 'inscripciones-list'),
    url(r'^eventos/inscripciones/(?P<pk>[0-9]+)/$', views.InscripcionEventoDetail.as_view(), name = 'inscripciones-detail'),
    url(r'^eventos/(?P<pk>[0-9]+)/$', views.EventoDetail.as_view(), name = 'evento-detail'),
    url(r'^eventos/usuariosPreInscritos/(?P<idEvento>[0-9]+)/$', views.getUsuariosPreinscritosPorEvento, name = 'usuarios-preinscritos-evento'),
    url(r'^noticias/(?P<pk>[0-9]+)/$', views.NoticiaDetail.as_view(), name = 'noticia-detail'),
    url(r'^actividades/(?P<pk>[0-9]+)/$', views.ActividadDetail.as_view(), name = 'actividad-detail'),
    url(r'^actividades/porEvento/(?P<evento>\w+)/$', views.ActividadList.as_view(), name = 'actividad-list'),
    url(r'^evento/(?P<evento>\w+)/usuariosPreinscritos/$', views.getUsuariosPreinscritosPorEvento, name = 'usuariosPreinscritosEventoList'),
    url(r'^getPreinscripcion/porIdUsuarioIdEvento/(?P<usuario>\w+)/(?P<evento>\w+)/$', views.PreInscripcionEventoByIdUserIdEvent.as_view(), name = 'id-preInscripcionIdEventoIdUsuario'),
    url(r'^getInscripcion/porIdUsuarioIdEvento/(?P<usuario>\w+)/(?P<evento>\w+)/$', views.InscripcionEventoByIdUserIdEvent.as_view(), name = 'id-InscripcionIdEventoIdUsuario'),
    url(r'^actividades/crear/$', views.ActivdadCreate.as_view(), name = 'actividad-create'),
    url(r'^actividades/$', views.ActividadAllList.as_view(), name = 'actividad-all-list'),
    url(r'^actividades/byEvent/(?P<evento>[0-9]+)/$', views.ActividadList.as_view(), name = 'actividad-byEvent-list'),
    url(r'^asistencias/$', views.AsistenciaActividadList.as_view(), name = 'asistencia-all-list'),
    url(r'^asistencias/(?P<pk>[0-9]+)/$', views.AsistenciaActividadDetail.as_view(), name = 'asistencia-all-list'),
]