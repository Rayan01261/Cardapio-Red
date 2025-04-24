from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Comanda, Mesa
from .serializers import ComandaSerializer, MesaSerializer

class ComandaViewSet(ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer

class MesaViewSet(ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
