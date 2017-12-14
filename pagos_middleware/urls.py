from django.conf.urls import url 
from pagos_middleware import views


urlpatterns = [
    url(r'^info-conexion-pagos/$', views.InfoConeccionPagosList.as_view(), name='info-conexion-pagos-list'),
    url(r'^info-conexion-pagos/(?P<pk>[0-9]+)/$', views.InfoConeccionPagosDetail.as_view(), name = 'eventos-list'),
    ]
