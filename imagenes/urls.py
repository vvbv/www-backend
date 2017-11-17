from django.conf.urls import url 
from imagenes import views

urlpatterns = [
    url(r'^$', views.ImagenList.as_view(), name = 'imagen-api'),
    url(r'^imagen/(?P<pk>[0-9]+)/$', views.ImagenApi.as_view(), name = 'imagen-api'),
    url(r'^imagen/nueva/$', views.ImagenCreateApi.as_view(), name = 'usuario-create'),
]