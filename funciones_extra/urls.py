from django.conf.urls import url 
from funciones_extra import views

urlpatterns = [
    url(r'^sendEmail/$', views.sendEmail, name="funciones-extra-sendEmail"),
]