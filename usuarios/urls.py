from django.conf.urls import url 
from usuarios import views

urlpatterns = [
    url(r'^lista$', views.UsuariosList.as_view()),
    url(r'^detalle/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view(), name = 'usuario-detail'),
    url(r'^detalle/(?P<username>[0-9]+)/$', views.UsuarioDetail.as_view(), name = 'usuario-detail'),
]