from django.conf.urls import url 
from usuarios import views

urlpatterns = [
    url(r'^$', views.none),
    url(r'^usuario/[0-9]*$', views.obtenerUsuario, name="obtenerUsuario"),
    url(r'^lista$', views.UsuariosList.as_view()),
]