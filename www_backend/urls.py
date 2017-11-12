"""www_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('eventos.urls')),
    url(r'^api/v1/usuarios/', include('usuarios.urls')),
    url(r'^api/v1/imagenes/', include('imagenes.urls')),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth-jwt/', obtain_jwt_token),
    url(r'^api/v1/auth-jwt-refresh/', refresh_jwt_token),
    url(r'^api/v1/auth-jwt-verify/', verify_jwt_token),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
