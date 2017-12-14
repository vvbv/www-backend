from django.conf.urls import url 
from usuarios import views

urlpatterns = [
    url(r'^$', views.UsuariosList.as_view(), name="usuario-api-lista"),
    url(r'^medio-de-pago-por-username/(?P<username>[a-z0-9]+)/$', views.MedioDePagoPorUsuario.as_view(), name = 'medio-pago-por-username'),
    url(r'^registrar-medio-pago/(?P<username>[a-z0-9]+)/(?P<numero_cuenta>[0-9]+)/(?P<password>[a-z0-9]+)/$', views.registrarMedioPago, name ="registrar-medio-pago"),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioPkApi.as_view(), name = 'usuario-pk-api'),
    url(r'^usuario/byUsername/(?P<username>[a-z0-9]+)/$', views.UsuarioUsernameApi.as_view(), name = 'usuario-username-api'),
    url(r'^usuario/nuevo/$', views.UsuarioCreateApi.as_view(), name = 'usuario-api-create'),
]