from django.conf.urls import url 
from eventos import views

urlpatterns = [
    url(r'^eventos/$', views.EventoList.as_view()),
    url(r'^eventos/(?P<pk>[0-9]+)/$', views.EventoDetail.as_view()),
]