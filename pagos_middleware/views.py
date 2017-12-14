from rest_framework import viewsets, generics
from .models import *
from .serializers import *
# Create your views here.


class InfoConeccionPagosDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = InfoConeccionPagos.objects.all()
    serializer_class = InfoConeccionPagosSerializer

class InfoConeccionPagosList(generics.ListCreateAPIView):    
    queryset = InfoConeccionPagos.objects.all().order_by('fecha_vencimiento')
    serializer_class = InfoConeccionPagosSerializer